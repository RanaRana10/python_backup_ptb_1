
from pathlib import Path

from telegram import Update
from telegram.ext import ContextTypes

from my_modules.abc_modules.files_and_folders import now_time_file_name

async def download_photo(update: Update,
                         context: ContextTypes.DEFAULT_TYPE,
                         download_folder: Path = Path("images") / "download_photo"
                         ) :
    """
    Download The Photo Directly
    This will return the image path after successful download
    """

    user = update.message.from_user

    image_saving_folder = Path(download_folder)
    image_saving_folder.mkdir(parents=True, exist_ok= True)

    now_time_str = now_time_file_name()
    photo_name = now_time_str + "_" + str(user.username)[:20] + ".jpg"
    photo_path = image_saving_folder / photo_name

    file_id = update.message.photo[-1].file_id
    photo_file = await context.bot.get_file(file_id)
    await photo_file.download_to_drive(photo_path)

    print("Download Successful")
    return photo_path



TG_IMAGE_FILE_ID = "AgACAgUAAxkBAAJn22YUvDdDZdVGxiroRr5qgmep3sKzAAKkwDEbgpipVKe81qVH1j6BAQADAgADeAADNAQ"
async def download_photo_from_file_id(context: ContextTypes.DEFAULT_TYPE,
                                      file_id:str = TG_IMAGE_FILE_ID,
                                      download_folder: Path = Path("images") / "download_photo",
                                      suffix_name: str | int = "",
                                      ):
    '''Just Pass the file_id of the photo media it will download
    this & returns the path after successful download
    '''
    image_saving_folder = Path(download_folder)
    image_saving_folder.mkdir(parents= True, exist_ok= True)
    now_time_str = now_time_file_name()
    
    photo_name = now_time_str + ".jpg"
    if suffix_name:
        photo_name = now_time_str + f"_{str(suffix_name)}_" + ".jpg"
    photo_path = image_saving_folder / photo_name

    photo_file = await context.bot.get_file(file_id= file_id)
    await photo_file.download_to_drive(photo_path)
    print("Download Successful", photo_path)
    return photo_path




TG_IMAGE_FILE_ID = "AgACAgUAAxkBAAJn22YUvDdDZdVGxiroRr5qgmep3sKzAAKkwDEbgpipVKe81qVH1j6BAQADAgADeAADNAQ"
async def download_photo_from_file_id(context: ContextTypes.DEFAULT_TYPE,
                                      file_id:str = TG_IMAGE_FILE_ID,
                                      download_folder: Path = Path("images") / "download_photo",
                                      suffix_name: str | int = "",
                                      ):
    '''Just Pass the file_id of the photo media it will download
    this & returns the path after successful download
    '''
    image_saving_folder = Path(download_folder)
    image_saving_folder.mkdir(parents= True, exist_ok= True)
    try:
        now_time_str = now_time_file_name()
        
        photo_name = now_time_str + ".jpg"
        if suffix_name:
            photo_name = now_time_str + f"_{str(suffix_name)}_" + ".jpg"
        photo_path = image_saving_folder / photo_name

        photo_file = await context.bot.get_file(file_id)
        await photo_file.download_to_drive(photo_path)
        
        print("Download Successful:", photo_path)
        return photo_path
    
    except Exception as e:
        print("Error downloading photo:", e)
        return None








successful_downloads = 0
async def download_photo_from_file_id_count(context: ContextTypes.DEFAULT_TYPE,
                                      file_id: str = TG_IMAGE_FILE_ID,
                                      download_folder: Path = Path("images") / "download_photo",
                                      suffix_name: str | int = "",
                                      ):
    '''Just Pass the file_id of the photo media it will download
    this & returns the path after successful download
    this is just for checking of multiple photo download by bot
    '''
    global successful_downloads  # Use the global counter variable
    
    image_saving_folder = Path(download_folder)
    image_saving_folder.mkdir(parents=True, exist_ok=True)
    
    try:
        now_time_str = now_time_file_name()
        
        photo_name = now_time_str + ".jpg"
        if suffix_name:
            photo_name = now_time_str + f"_{str(suffix_name)}_" + ".jpg"
        photo_path = image_saving_folder / photo_name

        photo_file = await context.bot.get_file(file_id)
        await photo_file.download_to_drive(photo_path)
        
        # Increment the global counter on successful download
        successful_downloads += 1
        
        print(f"Download {successful_downloads} Successful:", photo_path)
        return photo_path
    
    except Exception as e:
        print("Error downloading photo:", e)
        return None






