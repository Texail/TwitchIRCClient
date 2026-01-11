from dotenv import load_dotenv
import os
import time

from dispatcher import Dispatcher
from handlers import Handlers
from client import IRCClient
from models import UserMessage

# Загрузка переменных среды
def load_config() -> dict:
	load_dotenv()
	
	return {
		"channel" : os.getenv("TWITCH_CHANNEL", "texail01"),
		"server" : os.getenv("TWITCH_SERVER", "irc.chat.twitch.tv"),
		"port" : int(os.getenv("TWITCH_PORT", "6697")),
		"username" : os.getenv("TWITCH_USERNAME", "justinfan44294"),
		"password" : os.getenv("TWITCH_PASS", "SCHMOOPIIE"),
	}


def main() -> None:
	# Загрузка конфигурации
	config = load_config()
	# Создание диспетчера
	dispatcher = Dispatcher()
	# Регистрация обработчиков
	dispatcher.register(UserMessage, Handlers.user_message)
	# Создание и старт IRC клиента
	client = IRCClient(
		channel = config["channel"],
		server = config["server"],
		port = config["port"],
		username = config["username"],
		password = config["password"],
		on_event = dispatcher.dispatch
	)
	client.start()
	# Обработка сигнала прерывания
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		print("Получен сигнал прерывания")
	finally:
		client.stop()
		

if __name__ == "__main__":
	main()
