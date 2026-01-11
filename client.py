import socket
import ssl
import threading
import time
from parser import Parser
from models import PingEvent
from collections.abc import Callable

class IRCClient:
	def __init__(
			self,
			server: str,
			port: int,
			password: str,
			username: str,
			channel: str,
			on_event: Callable[[object], None]
		) -> None:
		self.server = server
		self.port = port
		self.password = password
		self.username = username
		self.channel = channel

		self.on_event = on_event
	
		self.sock = None
		self.reader_thread = None
		self.parser = None
	
	def start(self) -> None:
		self._create_socket()
		self._connect()
		# Создание потока для чтения ответов
		self.reader_thread = threading.Thread(
			target = self._read_loop,
			daemon = True,
		)
		self.reader_thread.start()
		# Создание парсера
		self.parser = Parser()
		# Авторизация
		self._authorization()

	def stop(self) -> None:
		if self.reader_thread:
			self.reader_thread.join(timeout=2)

		if self.sock:
			try:
				self.sock.shutdown(socket.SHUT_RDWR)
			except Exception:
				pass
			self.sock.close()

	def _create_socket(self) -> None:
		# Создание сокета
		raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Оборачивание сокета в SSL
		context = ssl.create_default_context()
		self.sock = context.wrap_socket(raw_socket, server_hostname = self.server)
		
	def _connect(self) -> None:
		# Подключение к серверу
		self.sock.connect((self.server, self.port))

	def _read_loop(self) -> None:
		# Создаем буфер
		buffer = ""

		while True:
			try:
				# Получаем сообщение от сервера
				chunk = self.sock.recv(1024)
				# Проверка на закрытие соединения | b"" -> соединение закрыто
				if not chunk:
					break
				# Запись в буфер полученных данных
				buffer += chunk.decode(encoding="utf-8", errors="ignore")
				
				while "\r\n" in buffer:
					line, buffer = buffer.split("\r\n", 1) # Отделяем 1 строку
					# print(line) # Debug
					event = self.parser.parse(line) # Парсим полученные данные и оформляем в класс
					# Ответ на ping
					if isinstance(event, PingEvent): 
						self._ping_pong()
					# Отправка данных на callback функцию
					self.on_event(event)

			except Exception:
				break

	def _authorization(self) -> None:
		# self._send("CAP REQ :twitch.tv/membership")
		# self._send("CAP REQ twitch.tv/tags")
		# self._send("CAP REQ twitch.tv/commands")
		self._send(f"PASS {self.password}")
		self._send(f"NICK {self.username}")
		self._send(f"JOIN #{self.channel}")

	def _send(self, text: str) -> None:
		# print(text) # Debug
		self.sock.sendall(f"{text}\r\n".encode(encoding="utf-8", errors="ignore"))
	
	def _ping_pong(self) -> None:
		self._send("PONG :tmi.twitch.tv")
