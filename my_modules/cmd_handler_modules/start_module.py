from telegram import Update
from telegram.ext import ContextTypes

from my_modules.logger_modules.logger_setup import rana_logger, rico_logger


async def start_fun_with_logger(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """This Function is for checking of usecase of Logging """
    user = update.effective_user
    await update.message.reply_html(f"Hi {user.mention_html()}!")
    
    rana_logger.info("RANA LOGGER")
    rico_logger.info("New Console From Rico")



async def start_fun_sep_old(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    chat = update.message.chat
    first_name = user.first_name
    last_name = user.last_name
    user_id = user.id
    username = user.username
    is_premium = user.is_premium

    text = f"Hello Boss {user.full_name} Thanks to start this bot\nSome of your information is: \n{first_name}, \n{last_name}, \n{user_id}, \n{username}, \n{is_premium}"
    await context.bot.send_message(user.id, text)






async def start_cmd(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''This is for simple /start from private users to bot'''
    user = update.message.from_user
    text = f"Hello Boss {user.full_name} Thanks to start this bot send /a, /b, /c, /start1 for making new conversation with me"
    await context.bot.send_message(user.id, text)


async def start_cmd_group(update:Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''This is triggers when bot received /start form a group'''
    chat = update.message.chat
    text = f"This start will work for Groups Only"
    await context.bot.send_message(chat.id, text)







if __name__ == "__main__":
    print(f"This Start Fun will store in this module")


