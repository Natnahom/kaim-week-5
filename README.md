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

# Task 2: Named Entity Recognition (NER) for Amharic Text

## Overview
This project aims to perform Named Entity Recognition (NER) on Amharic text data. The goal is to identify and label entities such as products, prices, and locations from a dataset of messages. The labeled data will be formatted in the CoNLL format, which is commonly used for NER tasks.

# requirements
pip install pandas

## Dataset
The input dataset should be in CSV format (preprocessed_data.csv) and should contain the following columns:

- channel: The communication channel.
- sender: The sender of the message.
- timestamp: The time the message was sent.
- content: The text message containing entities to be labeled.
- tokens: Tokenized version of the content.

## Usage
Prepare your dataset in CSV format and save it as preprocessed_data.csv in the project directory.
Run the script to read the dataset, label the entities, and save the output in CoNLL format:

Call the function as it is in the analysis file.

The labeled data will be saved as labeled_data.conll in the same directory.

## Code Structure
read_subset_df(data): Reads the CSV file and selects a random subset of messages from the content column.
label_entities(message): Labels entities in a given message based on predefined logic.
label_data(subset_df): Processes the subset of messages, applies entity labeling, and saves the results in CoNLL format.
Example Output
The output file labeled_data.conll will contain labeled entities in the following format:

Baby    B-Product
bottle  I-Product

Addis   B-LOC
abeba   I-LOC

ዋጋ    B-PRICE
1000    I-PRICE
ብር     I-PRICE

# License
This project is licensed under the MIT License. See the LICENSE file for more information.
