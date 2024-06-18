"""This is my own made class for some user related information with most need"""

from telegram.ext import ContextTypes

class UserInfo:
    '''This class take update.message.from_user 
    like parameter and here is some common users use 
    case mothods to call and get the appropriate things easily
    '''
    def __init__(self, user):
        self.first_name:str = user.first_name
        self.last_name = user.last_name
        self.user_id = user.id
        self.username = user.username
        self.is_premium = user.is_premium
        self.opposite_name = user.first_name[::-1]

    def reverse_name(self):
        return self.first_name[::-1]
    
    def full_name(self) -> str:
        if self.last_name:
            return f"{self.first_name} {self.last_name}".upper()
        return self.first_name
    
    def name_and_id_old(self) ->str:
        return self.full_name() + " " + str(self.user_id)
    

    def name_and_id(self, repeat: int = 3) -> str:
        """Return the concatenated name and ID repeated 'repeat' times."""
        if repeat <= 0:
            return "This is 0 Value no Work is for this"

        result = f"{self.full_name()} {self.user_id}"
        return result * repeat
    
    @property
    def name_and_id_html_bold(self) -> str:
        ''' if i use it i dont need to use <b> like this to bold my text of full name'''
        bold_name = f"<b>{self.full_name()}</b>"
        return bold_name
    
    @property
    def name_and_id_html_spoil(self) -> str:
        ''' if i use it i dont need to use <spoil> like this to bold my text of full name'''
        spoil_name = f'<tg-spoiler>{self.full_name()}</tg-spoiler>'
        return spoil_name




    async def count_user_photo(self, context: ContextTypes.DEFAULT_TYPE):
        try:
            profile_pic_details = await context.bot.get_user_profile_photos(self.user_id)
            number = profile_pic_details.total_count
            return number
        
        except Exception as e:
            print(e)
            return 0



    async def get_profile_photo_id_1(self, context):
        try:
            abc = await context.bot.get_user_profile_photos(self.user_id)
            abc_photos = abc.photos
            if abc_photos:
                file_id = abc_photos[0][-1].file_id  # First 0 is first image, then -1 is last hd high quality image
                return file_id
            else:
                return None
        except Exception as e:
            print(e)
            return None
        


    async def get_profile_photo_file_id(self, context: ContextTypes.DEFAULT_TYPE, photo_index: int = 0):
        '''This will return the file id if exists of any specific pic'''
        profile_photo_obj = await context.bot.get_user_profile_photos(self.user_id)
        photos = profile_photo_obj.photos
        if photos:
            file_id = photos[photo_index][-1]
            return file_id
        else:
            return None
            # await context.bot.send_message(self.user_id, file_id)






