

import random

from telegram import Update
from telegram.ext import ContextTypes

from my_modules.working_with_images.upi_qr_code_module import upi_qrcode_generate

async def plans_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This /plans when a user send a amount aftere the plan this execute and do all work'''

    user = update.message.from_user

    if context.args:
        money = context.args[0]
        image_path = upi_qrcode_generate(am = money)
        await context.bot.send_photo(user.id, image_path)
    else:
        await context.bot.send_message(user.id, "Pls send any like, /plans 45")





async def plan_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This /plans when a user send a amount aftere the plan this execute and do all work'''

    user = update.message.from_user

    if context.args:
        money = context.args[0]
        image_path = upi_qrcode_generate(am = money)
        await context.bot.send_photo(user.id, image_path)
    else:
        money = random.randint(1,1999)
        image_path = upi_qrcode_generate(am = money)
        await context.bot.send_photo(user.id, image_path)











