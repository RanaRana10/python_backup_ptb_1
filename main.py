'''
This is a example code

# pip install sqlalchemy
# pip install segno
# pip install pillow

'''



import sys
sys.dont_write_bytecode = True

import random


from telegram import  Update, InputSticker
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, PicklePersistence

from my_modules.cmd_handler_modules.start_module import start_cmd, start_cmd_group
from my_modules.cmd_handler_modules.help_module import help_cmd, help_cmd_group

from my_modules.msg_handler_modules.basic_msg_handler_module import echo

from my_modules.logger_modules.logger_setup_fun import setup_logger

from my_modules.conv_handler_modules.ptb_conv_1 import get_conv_handler_1
from my_modules.conv_handler_modules.ptb_conv_2 import get_conv_handler_2, get_user_data_dict
from my_modules.conv_handler_modules.ptb_conv_3 import get_conv_handler_3

from my_modules.database_modules.user_data_module import add_user_and_return_id, create_tables, check_user_existence_by_user_id, get_user_by_id, update_user_data, count_total_users, get_all_users

from my_modules.class_making_modules.user_info_class import UserInfo

from my_modules.cmd_handler_modules.plans_module import plans_cmd, plan_cmd
from my_modules.working_with_images.image_download_module import download_photo, download_photo_from_file_id, download_photo_from_file_id_count
from my_modules.working_with_images.image_editing_module import resize_img_png
from my_modules.abc_modules.files_and_folders import count_files_by_pattern



logger = setup_logger()

create_tables()
ADMIN = [1895194333, 000]
CHANNEL_1_ID = -1001911844095  # This is 00 Public Channel Rana 3 Bot
PRIVATE_CHANNEL_1_ID = -1002076959288
PRIVATE_CHANNEL_2_ID = -1002095108076
PRIVATE_CHANNEL_3_ID = -1002054038515




async def start_check_1(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    text = f"You Have Send Me: {update.message.text}"
    text += f"Your Data is saving into the database"
    await context.bot.send_message(user.id, text)

    existing_user_row_id = check_user_existence_by_user_id(user.id)

    if existing_user_row_id:
        print("User already exists with ID:", existing_user_row_id)
        await context.bot.send_message(user.id, f"User already exists with row ID: {existing_user_row_id}, You have Token: {get_user_by_id(user.id).token_}")
        
    else:
        id_after_insert = add_user_and_return_id(user.id, user.username, user.full_name, update.message.date)
        print("New user added with ID:", id_after_insert)
        await context.bot.send_message(user.id, f"New user added with ID: {id_after_insert}")

# CHECK_MEMBER_NOT_AVAILABLE = f"Hello {user.full_name} You Have Not Joined The Channel, You Need To Join This Channel To Use This Bot & Store Your Files"


async def start_check(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    chat = update.message.chat
    user_class = UserInfo(update.message.from_user)

    text = f"Hello {user.full_name} {user_class.name_and_id_html_spoil} You Have Not Joined The Channel, You Need To Join This Channel To Use This Bot & Store Your Files"

    chat_member = await context.bot.get_chat_member(CHANNEL_1_ID, user.id)

    if chat_member.status not in ["creator", "administrator", "member"]:
        await context.bot.send_message(user.id, text = f"{text}", parse_mode= "html")

    else:
        await context.bot.send_message(user.id, "You Can Use This Bot")
        profile_pic_file_id = await user_class.get_profile_photo_id(context= context)
        await context.bot.send_photo(user.id,
                                     profile_pic_file_id,
                                     caption= f"You Are Allowed to use this Bot 😎😎😎")


# async def count_pro_pic_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = update.message.from_user
#     abc = await context.bot.get_user_profile_photos(user.id)
#     total_photo = abc.total_count
#     if total_photo > 0:
#         random_photo_no = random.randint(0, total_photo - 1)
#         await context.bot.send_message(user.id, f"{random_photo_no}")
#     else:
#         await context.bot.send_message(user.id, f"No Photo Found")


async def count_pro_pic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    # abc = await context.bot.get_user_profile_photos(user.id)
    # total_photo = abc.total_count

    user_class = UserInfo(update.message.from_user)
    total_photo = await user_class.count_user_photo(context)

    # total_photo = await UserInfo(update.message.from_user).count_user_photo(context)

    if total_photo > 0:
        random_photo_no = random.randint(0, total_photo - 1)
        await context.bot.send_message(user.id, f"You will received {random_photo_no}th image in a second")
        random_photo_file_id = await user_class.get_profile_photo_file_id(context, random_photo_no)
        await context.bot.send_photo(user.id, random_photo_file_id, f"This is Your {random_photo_no} th Profile Pic")
    else:
        await context.bot.send_message(user.id, f"No Photo Found")






async def all_msghandler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f"{update}")
    ...



async def update_token_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    if len(context.args) != 2:
        await update.message.reply_text("Usage: /update_token <user_id> <new_token>")
        return
    try:
        user_id_to_update = int(context.args[0])
        token_to_change = int(context.args[1])
    except ValueError:
        await update.message.reply_text("Invalid user ID or token. Both should be integers.")
        return
    # user_id_to_update = context.args[0]
    # token_to_change = context.args[1]
    # update_user_data(user_id_to_update, token_ = token_to_change)
    result_message = update_user_data(user_id_to_update, token_=token_to_change)
    await update.message.reply_text(result_message)



async def count_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_list_no = get_all_users()
    await context.bot.send_message(user.id, f"{user_list_no}")

    



async def sticker_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will execute for any type of sticker send to bot'''

    user = update.message.from_user
    sticker = update.message.sticker
    sticker_id = sticker.file_id

    await context.bot.send_message(user.id, f"{update}")
    await context.bot.send_sticker(user.id, sticker_id)



# async def sticker_fun_2_(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     '''/s to execute this fun'''
#     user = update.message.from_user

#     # sticker_file = await context.bot.upload_sticker_file(user.id, "2.png", "static")
#     # sticker_file_id = sticker_file.file_id
#     # await context.bot.send_message(user.id, f"{sticker_file_id}\n{sticker_file.file_size}")

#     s_sticker_msg = await context.bot.send_sticker(user.id, f"0.png")
#     await context.bot.send_message(user.id, f"<code>{s_sticker_msg.sticker.file_id}</code>", parse_mode= "html")
#     s_sticker_msg = await context.bot.send_sticker(user.id, f"1.png")
#     await context.bot.send_message(user.id, f"<code>{s_sticker_msg.sticker.file_id}</code>", parse_mode= "html")
#     s_sticker_msg = await context.bot.send_sticker(user.id, f"2.png")
#     await context.bot.send_message(user.id, f"<code>{s_sticker_msg.sticker.file_id}</code>", parse_mode= "html")
#     s_sticker_msg = await context.bot.send_sticker(user.id, f"3.png")
#     await context.bot.send_message(user.id, f"<code>{s_sticker_msg.sticker.file_id}</code>", parse_mode= "html")
#     s_sticker_msg = await context.bot.send_sticker(user.id, f"4.png")
#     await context.bot.send_message(user.id, f"<code>{s_sticker_msg.sticker.file_id}</code>", parse_mode= "html")
#     #Below is create new sticker set
#     file_id_list = ["CAACAgUAAxkDAAJnWWYSmwob3MDwqTCCBNW2_LS5bUtgAAJoDQACSqiRVFd4tIPC0nUbNAQ",
#                     "CAACAgUAAxkDAAJnV2YSmwaL_ryuJiTd33z2dnC3AAEy1wACZw0AAkqokVSzU1F9jrPzOjQE",
#                     "CAACAgUAAxkDAAJnVWYSmwNs4G1_sWqac0z0ln_S3F-4AAJmDQACSqiRVAx1GBkyWNB6NAQ",
#                     "CAACAgUAAxkDAAJnU2YSmwHACowKn0lUjEoyS0EDobDuAAJlDQACSqiRVPWZktpzTX07NAQ",
#                     "CAACAgUAAxkDAAJnUWYSmv71J8K1WfxKMKRDM-8482WTAAJkDQACSqiRVCdjt_RQxwskNAQ"]
#     input_sticker_1 = InputSticker(file_id_list[0], ["😕","💩","💪"])




a1_sticker = "CAACAgUAAxkBAAJ8c2Zw-WDrMTN0MuwhzaDV2N2Ry21oAAI3BQACyNHhVvg2sV72yKqLNQQ"
a2_sticker = "CAACAgIAAxkBAAJ8dGZw-WbLIZTjMs-mvmt6lDt1XLmbAAIBAAPANk8TGC5zMKs_LVE1BA"
a3_sticker = "CAACAgIAAxkBAAJ8dWZw-WgRPwQFPBxF15Oroim3rRcfAAITAAPANk8TqrOH9384yqU1BA"
a4_sticker = "CAACAgIAAxkBAAJ8dmZw-WpE-pN0D4YuCj7q1X6wqL1tAAIbAAPANk8Tfb2Kg8tETWo1BA"
a5_sticker = "CAACAgIAAxkBAAJ8d2Zw-WtC0yZQq64XgUjmSkK7JEalAAIOAAPANk8TI1cURIdu1mU1BA"




async def sticker_fun_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''/s to execute this fun'''
    user = update.message.from_user

    if context.args:
        file_id = context.args[0]
        await context.bot.send_sticker(user.id, file_id)
    else:
        await context.bot.send_message(user.id, f"Pls send the sticker file id after this command, example: /sticker /s")
        await context.bot.send_chat_action(user.id, "choose_sticker")
        sti_files_list = [a1_sticker, a2_sticker, a3_sticker, a4_sticker, a5_sticker]
        random_sticker = random.choice(sti_files_list)
        s_sticker_msg = await context.bot.send_sticker(user.id, random_sticker)
        await context.bot.send_message(user.id, f"Random Sticker file name:\n<code>{s_sticker_msg.sticker.file_id}</code>", parse_mode= "html")




async def photo_processing_fun_1(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    photo = update.message.photo[-1]
    file_id = photo.file_id
    image_path = await download_photo(update, context)
    await context.bot.send_document(user.id, image_path)


async def photo_processing_fun_2(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    photo = update.message.photo[-1]
    file_id = photo.file_id
    if user.username:
        suffix_name = user.username
    else:
        suffix_name = user.id
    image_path = await download_photo_from_file_id(context= context, file_id= file_id, suffix_name= suffix_name)

    if image_path:
        await context.bot.send_document(user.id, image_path)
    else:
        await context.bot.send_message(user.id, "Some Error in image path") 




async def photo_processing_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    photo = update.message.photo[-1]
    file_id = photo.file_id
    await context.bot.send_chat_action(user.id, "upload_photo")

    image_path = await download_photo_from_file_id(context= context, file_id= file_id)
    resized_image_path = resize_img_png(input_image= image_path)
    await context.bot.send_chat_action(user.id, "upload_document")

    await context.bot.send_document(user.id, resized_image_path)



async def count_files_by_pattern_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    if user.id not in ADMIN:
        await context.bot.send_message(user.id, "You are not a admin")
        return

    if context.args:
        if len(context.args) != 2:
            text = f"Pls send appropriate data with first args as file path second as file extension"
            await context.bot.send_message(user.id, text = text)
            return
        else:
            folder_name = context.args[0]
            extension = context.args[1]

    if user.id in ADMIN:
        number = count_files_by_pattern(folder_name, extension)
        await context.bot.send_message(user.id, number)















def main() -> None:
    """Start the bot."""
    persistence = PicklePersistence(filepath= "zzz_pickle_file")

    application = Application.builder().persistence(persistence).token("6780033449:AAFKWBuWlPcBHLm303owSEvDriPZjCxs9ZU").build()


    application.add_handler(get_conv_handler_1())
    application.add_handler(get_conv_handler_2())
    application.add_handler(get_conv_handler_3())

    application.add_handler(CommandHandler(["a", "b", "about"], start_check))
    application.add_handler(CommandHandler(["c", "count"], count_pro_pic))
    application.add_handler(CommandHandler(["s", "sticker"], sticker_fun_2))
    application.add_handler(CommandHandler(["2r"], get_user_data_dict))
    application.add_handler(CommandHandler(["count_files_by_pattern"], count_files_by_pattern_check))

    application.add_handler(CommandHandler("update_token", update_token_admin, filters= filters.Chat(ADMIN)))
    application.add_handler(CommandHandler("count_total_users", count_user, filters= filters.Chat(ADMIN)))

    application.add_handler(CommandHandler("start", start_cmd, filters=filters.ChatType.PRIVATE, block= False))
    application.add_handler(CommandHandler("start", start_cmd_group, filters=filters.ChatType.GROUPS, block= False))

    application.add_handler(CommandHandler("help", help_cmd, filters= filters.ChatType.PRIVATE))
    application.add_handler(CommandHandler("help", help_cmd_group, filters= filters.ChatType.GROUPS))

    application.add_handler(CommandHandler("plans", plans_cmd, filters= filters.ChatType.PRIVATE))
    application.add_handler(CommandHandler("plan", plan_cmd, filters= filters.ChatType.PRIVATE))



    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.Sticker.ALL, sticker_fun))
    application.add_handler(MessageHandler(filters.PHOTO, photo_processing_fun))
    application.add_handler(MessageHandler(filters.ALL,all_msghandler))


    application.run_polling(allowed_updates=Update.ALL_TYPES)






if __name__ == "__main__":
    
    main()