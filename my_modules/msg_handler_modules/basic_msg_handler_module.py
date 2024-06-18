import random

from telegram import Update
from telegram.ext import ContextTypes





async def echo_all_upper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message. with upper"""
    await update.message.reply_text(update.message.text.upper())

async def echo_all_lower(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message.with lower"""
    await update.message.reply_text(update.message.text.lower())

async def echo_reverse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text[::-1].upper())



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    
    functions = [echo_all_lower, echo_all_upper, echo_reverse]
    random_fun = random.choice(functions)

    function_name = random_fun.__name__
    await update.message.reply_text(f"{function_name} will execute")
    await random_fun(update, context)















