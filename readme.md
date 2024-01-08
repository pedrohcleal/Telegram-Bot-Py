## PH Telegram Bot

This repository contains two main files, `main.py` and `InfoAPI.py`, which constitute the Telegram bot called "PH Bot". The bot is designed to operate in Telegram groups, responding to specific commands, and sending periodic messages with information about the Bitcoin price in relation to the Dollar (USDT).

### File `main.py`

The `main.py` file is the main script of the bot, responsible for initializing and executing the bot's functionalities on Telegram. Below are the main components of the script:

#### Dependencies

```python
from typing import Final
from telegram import Update, Bot
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio, InfoAPI, os
from dotenv import load_dotenv
from datetime import datetime
```

Make sure to have all the necessary libraries installed before running the script. You can install them using the command:

```bash
pip install python-telegram-bot[asyncio] python-dotenv
```

#### Configurations

- Replace `'TOKEN'` with the token provided by BotFather.
- Set the interval to send periodic messages in seconds (`PERIODIC_MESSAGE_INTERVAL`).
- Replace `'YOUR_GROUP_ID'` with the ID of your group (you can use the `@get_id_bot` to get the group ID).

#### Main Functions

- `start_command`: Start command that responds with a greeting.
- `help_command`: Help command that responds with information about available commands.
- `custom_command`: Custom command that responds with a customizable message.

#### Message Handling

- `handle_responses`: Function to process and respond to specific messages.
- `handle_message`: Function to handle received messages in the desired group.

#### Error Handling

- `error`: Function to handle errors and print information about them.

#### Periodic Messages

- `send_periodic_message`: Function to send periodic messages with the Bitcoin price in relation to the Dollar.

#### Initialization and Execution

- The script creates an instance of the application, adds command, message, and error handlers, and starts the bot.

### File `InfoAPI.py`

The `InfoAPI.py` file contains functionalities related to obtaining information about the Bitcoin price using the Binance API.

#### Dependencies

```python
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json
from dotenv import load_dotenv
import os
```

Make sure to have the `python-binance` library installed:

```bash
pip install python-binance
```

#### Configurations

- Loads Binance API keys from the `.env` file.

#### Main Functions

- `price_btcusdt`: Returns the current price of Bitcoin in relation to the Dollar (USDT).

#### Execution (example)

- Prints the Bitcoin price and additional information if the script is executed directly.

### Execution

Make sure to configure the `.env` file correctly with your Binance API keys and your Telegram bot token before running the `main.py` script.

```bash
python main.py
```

This will start the bot and begin responding to commands, processing messages, and sending periodic updates in the specified group.