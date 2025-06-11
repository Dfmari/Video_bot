# This is the telegram bot that registers the user and sends out 
import telebot 
from dotenv import load_dotenv
import os
load_dotenv() 

API_KEY = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(API_KEY)
