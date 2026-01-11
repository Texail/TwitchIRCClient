from collections.abc import Callable


from models import UserMessage


class Dispatcher:
	def __init__(self) -> None:
		# Словарь {Тип события : [Список обработчиков]}
		self._handlers: dict[type, list[Callable[[object, None]]]] = {}

	# Регистрация обработчика
	def register(
			self,
			event_type: type,
			handler: Callable[[object], None]
		) -> None:
		# Проверка на наличие такого типа события
		if not event_type in self._handlers:
			# Создание ключа для добавления обработчиков
			self._handlers[event_type] = []
		# Добавить обработчик к списку обработчиков типа события 
		self._handlers[event_type].append(handler)

	def dispatch(self, event: object) -> None:
		handled = False
		# Обработка событий
		for event_type in self._handlers:
			# Определение типа события
			if isinstance(event, event_type):
				# Вызов всех обработчиков привязанных к событию
				for handler in self._handlers[event_type]:
					handler(event)
				handled = True
		# Событие не обработано
		if not handled:
			self._handle_unhandled(event)

	# Обработчик событий, которые не имеют обработчиков
	def _handle_unhandled(self, event: object) -> None:
		pass
	