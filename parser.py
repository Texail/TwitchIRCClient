from models import UserMessage, SystemMessage, PingEvent

class Parser:
	def parse(self, raw_message: str) -> object:
		# Заметка: Если переставить местами PRIVMSG и PING может быть нарушена работа программы
		if "PRIVMSG" in raw_message:
			return self._privmsg(raw_message)
		elif "PING" in raw_message:
			return self._ping()
		return None

	def _ping(self, raw_message: str) -> PingEvent:
		return PingEvent(
			text = raw_message
		)

	def _privmsg(self, raw_message: str) -> UserMessage:
		username = raw_message[1:raw_message.find("!")]
		text = raw_message.split(":",2)[2]
		return UserMessage(
			user = username,
			text = text,
		)
