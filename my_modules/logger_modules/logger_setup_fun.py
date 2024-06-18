import logging
from pathlib import Path



def setup_logger():
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return logging.getLogger(__name__)



def create_log_file():
    log_folder = Path("my_modules") / "logger_modules"
    log_folder.mkdir(parents=True, exist_ok=True)
    log_file = log_folder / "0 Rana LOG FIle.log"
    return log_file



def setup_file_logger():
    log_file = create_log_file()

    rana_logger = logging.getLogger("RANA NAME")
    rana_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("FILE is:%(asctime)s ---Name is %(name)s -- ***%(levelname)s*** - %(message)s")

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    rana_logger.addHandler(file_handler)
    rana_logger.propagate = False
    return rana_logger



def setup_console_logger():
    rico_logger = logging.getLogger("RICO TERMINAL")
    rico_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("CONSOLE is:%(asctime)s ---Name is %(name)s -- ***%(levelname)s*** - %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    rico_logger.addHandler(console_handler)
    rico_logger.propagate = False
    return rico_logger














if __name__ == "__main__":
    print("Running main2logger.py directly.")
