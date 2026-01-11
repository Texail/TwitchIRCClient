[RU](#ru-language) [ENG](#eng-language)
<a name="eng-language"></a>
# Twitch IRC Client
## 📖 Description
A simple IRC client for connecting to Twitch chat with SSL support and an event-driven system via a dispatcher.
## ✨ Features
- Event handling system (user messages, PINGs)
- Extensible architecture with an event dispatcher
- Support for handlers for different event types
- Automatic PONG response to PING messages
- Configuration via environment variables
## 🚀 Quick Start
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) by following their instructions.
2. Set up your .env file, replacing the TWITCH_CHANNEL value with your target channel.
3. Open a terminal and run the command:
```
uv run main.py
```
> [!NOTE]
> uv will install the required packages and start the application.
---
<a name="ru-language"></a>
# Twitch IRC Client
## 📖 Описание
Простой IRC-клиент для подключения к Twitch чату с поддержкой SSL и системой обработки событий через диспетчер.
## ✨ Особенности
- Система обработки событий (сообщения пользователей, пинги)
- Расширяемая архитектура с диспетчером событий
- Поддержка обработчиков для разных типов событий
- Автоматический ответ на PING-сообщения
- Конфигурация через переменные окружения
## 🚀 Быстрый старт
1. Установите [uv](https://docs.astral.sh/uv/getting-started/installation/) по их инструкции.
2. Настройте .env, заменив значение TWITCH_CHANNEL на целевой канал.
3. Откройте терминал и выполните команду:
```
uv run main.py
```
> [!NOTE]
> uv установит необходимые пакеты и запустит приложение.
