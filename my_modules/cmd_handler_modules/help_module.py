from telegram import Update
from telegram.ext import ContextTypes

admin_user_ids = [1895194333, 5393096971]


async def help_fun_1(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    chat = update.message.chat
    text = f"Hello {user.full_name} This is the /help Section of this bot, you can Use This bot for your personal Use Case"

    await context.bot.send_message(chat.id, text)
    text = "You are a admin, You dont need HELPP 🍌🍌🍌"


async def help_fun_2(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    chat = update.message.chat
    if user.id in admin_user_ids:
        text = "You are an admin, You don't need HELP 🍌🍌🍌"
    else:
        text = f"Hello {user.full_name}, This is the /help Section of this bot. You can Use This bot for your personal Use Case"

    await context.bot.send_message(chat.id, text)





async def handle_admin_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    chat = update.message.chat
    
    text = "You are an admin, You don't need HELP 🍌🍌🍌"
    await context.bot.send_message(chat.id, text)




async def handle_regular_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    chat = update.message.chat
    
    text = (f"Hello {user.full_name}, This is the /help Section of this bot. "
        f"\nYou can Use This bot for your personal Use Case")

    text = f"Hello {user.full_name}, This is the /help Section of this bot. You can Use This bot for your personal Use Case"

    await context.bot.send_message(chat.id, text)
    await context.bot.send_message(chat.id, text.upper())




async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will execute when /help will come to bot in private msg'''
    user = update.message.from_user
    chat = update.message.chat
    
    if user.id in admin_user_ids:
        # Execute admin action 🍌🍌🍌
        await handle_admin_help(update, context)
    else:
        # Execute regular user action
        await handle_regular_help(update, context)



async def help_cmd_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is triggers when a user send /help in a group msg'''
    chat = update.message.chat
    text_0 = (
    f"I cannot help you in this {chat.title}\n"
    "Please Go To private Chat with me and then "
    "send /help to get more help of how to use me 😜😜😜"
    )
    text = f"I cannot help you in this <b>{chat.title}</b>\nPlease Go To private Chat with me and then send /help to get more help of how to ues me😜😜😜"
    
    await context.bot.send_message(chat.id, text, parse_mode= "html")


