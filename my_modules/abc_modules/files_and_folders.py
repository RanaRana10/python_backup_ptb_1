

import datetime
from pathlib import Path

def now_time_file_name_1(suffix:str = ""):
    '''Generate a file name of current time human readable'''
    now = datetime.datetime.now()
    now_str = now.strftime("%Y_%m_%d_%H_%M_%S")
    if suffix:
        now_str = f"{now_str}_{suffix}"
    else:
        now_str = f"{now_str}"

    if suffix is not None:
        now_str = f"{now_str}"

    print(now_str)



def now_time_file_name(suffix: str = ""):
    '''Generate a file name of current time human readable
    Format:   %Y_%m_%d_%H_%M_%S
    '''
    now = datetime.datetime.now()
    now_str = now.strftime("%Y_%m_%d_%H_%M_%S")

    if suffix:
        now_str = f"{now_str}_{suffix}"

    print(now_str)
    return now_str



def get_filenames_by_extension(folder_path: Path = "",
                               file_extension: str = "png"):

    folder_path = Path(folder_path)
    files = folder_path.glob("*" + file_extension)
    file_names = [file.name for file in files]
    total_string = "\n".join(file_names)
    return total_string




def count_files_by_pattern(folder_path: Path = "", file_extension: str = "png"):

    folder_path = Path(folder_path)
    pattern = "*" + file_extension
    matching_files = list(folder_path.glob(pattern))
    num_files = len(matching_files)
    
    return num_files

















if __name__ == "__main__":
    now_time_file_name()
    now_time_file_name(suffix= "")