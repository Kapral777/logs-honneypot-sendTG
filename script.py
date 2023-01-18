{\rtf1\ansi\ansicpg1251\cocoartf2707
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\csgray\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs28 \cf2 \CocoaLigature0 #!/usr/bin/env python3\
import time\
import os\
from telegram import Bot\
\
# Telegram bot token and chat ID\
bot_token = \'91*************************\'92\
chat_id = \'91*****************\'92\
\
# Path to the file\
file_path = \'91*******************\'92\
\
# Get the number of lines in the file\
previous_lines = sum(1 for line in open(file_path, 'r', encoding='utf-8', errors='ignore'))\
\
while True:\
    # Sleep for a certain amount of time\
    time.sleep(5)\
\
    # Get the current number of lines in the file\
    current_lines = sum(1 for line in open(file_path, 'r', encoding='utf-8', errors='ignore'))\
\
    # Check if the number of lines has changed\
    if current_lines > previous_lines:\
        # Open the file and read the new lines\
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:\
            new_lines = f.readlines()[previous_lines:]\
\
        # Join the new lines into a single message\
        message = '\\n'.join(new_lines)\
        message = message.replace(",", "\\n")\
\
        # Send the message to Telegram\
        bot = Bot(token=bot_token)\
        bot.send_message(chat_id=chat_id, text=message)\
\
        # Update the previous number of lines\
        previous_lines = current_lines\
}