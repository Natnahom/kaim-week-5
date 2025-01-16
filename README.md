## This is week-5 of 10 academy

# Task 1: Data Ingestion and Preprocessing from Telegram Channels

## Overview

This project aims to ingest messages from specified Telegram channels and preprocess the data for further analysis. The collected data will be saved in JSON format and then processed to create a CSV file, preserving Amharic characters.

## Requirements

- Python 3.7 or higher
- Required Python packages:
  - `telethon`
  - `pandas`
  - `python-dotenv`

You can install the required packages using pip:

```bash
pip install telethon pandas python-dotenv
```

# Create a .env File:
- Create a file named .env in the root directory of your project.
- Add your API credentials in the following format:

    - API_ID=your_api_id_here
    - API_HASH=your_api_hash_here

# Usage
Run the Data Ingestion Script:
Execute the script to collect messages from the specified channels:
python telegram_data_ingestion.py

# Output
The collected messages will be stored in telegram_messages.json.
The preprocessed data will be saved in preprocessed_data.csv, preserving Amharic characters.

# Important Notes
Ensure compliance with Telegram's Terms of Service to avoid account bans.
Be mindful of rate limits when collecting data from Telegram channels.
You may need to log in to your Telegram account the first time you run the script, and a session file will be created for subsequent runs.

# License
This project is licensed under the MIT License. See the LICENSE file for more information.

# Acknowledgments
Telethon - Python Telegram client.
Pandas - Data manipulation and analysis library.