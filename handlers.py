from models import UserMessage

class Handlers:
	@staticmethod
	def user_message(user_message: UserMessage) -> None:
		print(f"{user_message.user}: {user_message.text}")