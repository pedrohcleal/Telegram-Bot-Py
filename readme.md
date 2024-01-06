 **README.md**

# Telegram Bot for Bitcoin Price Updates

This project creates a Telegram bot that periodically sends Bitcoin price updates to a specified group chat. It also interacts with users through basic commands and simple responses.

## Files

**main.py:**

* Contains the main bot logic.
* Handles commands, messages, and periodic updates.
* Fetches Bitcoin price information from the Binance API.

**InfoAPI.py:**

* Provides a function to retrieve the current Bitcoin price from the Binance API.

## Setup

1. Install required libraries:

   ```bash
   pip install telegram telegram-ext python-binance dotenv
   ```

2. Create a `.env` file in the project directory with the following variables:

   ```
   TOKEN=YOUR_TELEGRAM_BOT_TOKEN
   apikey=YOUR_BINANCE_API_KEY
   secretkey=YOUR_BINANCE_API_SECRET
   GRUPO_ID=YOUR_TELEGRAM_GROUP_ID
   ```

   - Obtain a Telegram bot token from BotFather.
   - Get your Binance API keys from Binance.
   - Find the Telegram group ID using a bot like @get_id_bot.

## Running the Bot

1. Execute the main script:

   ```bash
   python main.py
   ```

## Bot Features

* **Periodic Updates:** Sends the current Bitcoin price to the specified group chat every 5 seconds (adjustable in `main.py`).
* **Commands:**
    - `/start`: Welcome message.
    - `/help`: Provides a help message.
    - `/custom`: Customizable command (currently responds with a fixed message).
* **Simple Responses:** Responds to "ola" with "olá sr(a)".
* **Error Handling:** Prints errors to the console.

## Future Enhancements

* Add more commands and responses.
* Improve error handling and logging.
* Explore additional features and integrations.

**Important:**

* Keep your API keys and token secure.
* Respect Telegram's API usage guidelines.

Feel free to customize and extend this bot to fit your needs!
