

from PIL import Image
from pathlib import Path
from my_modules.abc_modules.files_and_folders import now_time_file_name


def resize_img_png_1(path:str|Path = "images/a.png"):
    '''This will resize image to 512 pixel in both and returns .png
    by save this and give the Path of this image
    '''

    im = Image.open(path)
    im = im.resize((512, 512))
    im.show()
    im.save(f"{now_time_file_name()}_a.png")


def resize_img_png(path: str | Path = "images/a.png",
                   new_size: tuple = (512, 512),
                   output_folder: Path = Path("images") / "after_resized",
                   ):
    '''This will resize image to 512 pixel in both and returns .png
    by save this and give the Path of this image
    '''

    im = Image.open(path)
    im = im.resize(new_size)
    
    original_filename = Path(path).stem
    print(original_filename)

    
    resized_filename = f"{original_filename}_{new_size[0]}_{new_size[1]}.png"

    output_folder.mkdir(parents= True, exist_ok= True)
    resized_filepath = output_folder / resized_filename

    im.save(resized_filepath)
    return resized_filepath


def resize_img_png(new_size: tuple = (512, 512),
                   input_image: Path = "",
                   output_folder: Path = Path("images") / "after_resize",
                   suffix: str = "",
                   ):
    '''This will take input folder & output folder
    it will take the image size and then resize it and then return the output Path
    '''
    if input_image is None:
        return None
    
    im = Image.open(input_image)
    im = im.resize(new_size)

    original_filename = Path(input_image).stem
    print("Original Filename")

    resized_filename = f"{original_filename}_{new_size[0]}_{new_size[1]}.png"
    if suffix:
        resized_filename = f"{original_filename}_{suffix}_{new_size[0]}_{new_size[1]}.png"
    print(resized_filename)
    output_folder.mkdir(parents= True, exist_ok= True)
    resized_filepath = output_folder / resized_filename
    im.save(resized_filepath)
    return resized_filepath





def resize_img_png_3(new_size: tuple = (512, 512),
                   input_image: Path = "",
                   output_folder: Path = Path("images") / "after_resize",
                   suffix: str = "",
                   ):
    
    '''This function resizes an input image and saves the resized image to the output folder.
    Args:
        new_size (tuple): The new size of the image (width, height).
        input_image (Path): The path to the input image file.
        output_folder (Path): The folder where the resized image will be saved.
        suffix (str, optional): A suffix to append to the filename. Defaults to "".
    Returns:
        Path: The path to the resized image file.
    '''
    if not input_image:
        return None
    
    try:
        im = Image.open(input_image)
        im = im.resize(new_size)
        original_filename = Path(input_image).stem
        resized_filename = f"{original_filename}_{suffix}_{new_size[0]}_{new_size[1]}.png"
        output_folder.mkdir(parents=True, exist_ok=True)
        resized_filepath = output_folder / resized_filename
        im.save(resized_filepath)
        return resized_filepath
    
    except Exception as e:
        print("Exception Occured", e)
        return None








def resize_img_png_for_512_higher(max_size: int = 512,
                   input_image: Path = "",
                   output_folder: Path = Path("images") / "after_resize",
                   suffix: str = "",
                   ):
    '''Problem for less than 512 images sizes
    This will take max size to change and make other part les than 512
    '''

    if not input_image:
        return None
    
    try:
        im = Image.open(input_image)
        width, height = im.size
        if width == height:
            new_width = max_size
            new_height = max_size

        elif width > height:
            new_width = 512
            ratio_change = width // 512
            new_height = height // ratio_change

        elif height > width:
            new_height = 512
            ratio_change = height // 512
            new_width = width // ratio_change

        new_size = (new_width, new_height)
        im = im.resize(new_size)

        original_filename = Path(input_image).stem
        resized_filename = f"{original_filename}_{suffix}_{new_size[0]}_{new_size[1]}.png"
        output_folder.mkdir(parents=True, exist_ok=True)
        resized_filepath = output_folder / resized_filename
        im.save(resized_filepath)
        return resized_filepath
    
    except Exception as e:
        print("Exception Occured", e)
        return None





def resize_img_png(max_size: int = 512,
                   input_image: Path = "",
                   output_folder: Path = Path("images") / "after_resize",
                   suffix: str = "",
                   ):
    '''This will take max size to change and make other part les than 512'''

    if not input_image:
        return None
    
    try:
        im = Image.open(input_image)
        width, height = im.size
        if width == height:
            new_width = max_size
            new_height = max_size

        elif width > height:
            new_width = 512
            ratio_change = width / 512
            new_height = int(height / ratio_change)

        elif height > width:
            new_height = 512
            ratio_change = height / 512
            new_width = int(width / ratio_change)

        new_size = (new_width, new_height)
        im = im.resize(new_size)

        original_filename = Path(input_image).stem
        resized_filename = f"{original_filename}_{suffix}_{new_size[0]}_{new_size[1]}.png"
        output_folder.mkdir(parents=True, exist_ok=True)
        resized_filepath = output_folder / resized_filename
        im.save(resized_filepath)
        return resized_filepath
    
    except Exception as e:
        print("Exception Occured", e)
        return None
















if __name__ == "__main__":
    resize_img_png()














