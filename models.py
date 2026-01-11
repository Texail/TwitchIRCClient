from dataclasses import dataclass

@dataclass
class UserMessage:
	user: str
	text: str

@dataclass
class SystemMessage:
	text: str

@dataclass
class PingEvent(SystemMessage):
	pass