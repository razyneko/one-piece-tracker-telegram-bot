# Telegram Episode Tracker Bot

A Telegram bot to manage and track episodes of One Piece. This bot provides an easy way to set, track, and navigate episodes, ensuring you never lose track of where you left off.  

## Features
- Set the current episode.
- Move to the next episode with a single command.
- Retrieve the current episode and a direct link to watch.
- Handles unrecognized commands gracefully by prompting valid options.

## Commands Overview
| Command           | Description                                    |
|-------------------|------------------------------------------------|
| `/set_ep <n>`     | Sets the current episode to `<n>`.            |
| `/next`           | Moves to the next episode.                    |
| `/current`        | Displays the current episode with a watch link. |
| Invalid commands  | Prompts usage instructions for valid commands.|

## Screenshots
### 1. `/set_ep` Command
![Set Episode](![01](https://github.com/user-attachments/assets/59972315-8abc-4324-a851-3bed3265ae95)
)

### 2. `/next` Command
![Next Episode](![03](https://github.com/user-attachments/assets/4835103e-6f3a-4e48-8755-73e5c6018ed5)
)

### 3. `/current` Command
![Current Episode](![02](https://github.com/user-attachments/assets/65ff6f9c-5bda-4ef2-a796-15748d8a774b)
)

### 4. Invalid Command Handling
![Invalid Command](![04](https://github.com/user-attachments/assets/8a134c89-bf74-43a2-a2a7-69ecbbac405f)
)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/telegram-episode-tracker.git
   cd telegram-episode-tracker
   ```

2. Install dependencies:
   ```bash
   pip install pyTelegramBotAPI python-dotenv
   ```

3. Create a `.env` file in the project root with your API token and channel ID:
   ```
   API_TOKEN=your_telegram_api_token
   CHANNEL_ID=your_channel_id
   ```

4. Ensure `episodes.json` exists or will be created automatically:
   - If missing, the bot initializes `episodes.json` with the first episode set to 1.

5. Run the bot:
   ```bash
   python bot.py
   ```

## Project Directory Structure
```
telegram-episode-tracker/
├── bot.py           # Main bot script
├── .env             # Environment variables (API token and channel ID)
├── episodes.json    # JSON file to store the current episode
├── README.md        # Project documentation
```

## Usage
1. Add the bot to your Telegram and start the chat.
2. Use `/set_ep <n>` to set the current episode.
3. Use `/next` to move to the next episode.
4. Use `/current` to view the current episode and a direct watch link.
5. If an invalid command is sent, the bot will guide you with valid options.

## Error Handling
- **Missing or invalid commands:** The bot gracefully handles invalid inputs and prompts the user with correct usage instructions.
- **First run setup:** Automatically initializes `episodes.json` if missing or empty.
