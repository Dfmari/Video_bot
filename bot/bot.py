# This is the telegram bot that registers the user and generates jitsi links 
import telebot 
from dotenv import load_dotenv
import os
import jitsi_handler
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

load_dotenv() 

BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')
