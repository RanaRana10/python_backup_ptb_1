import segno
from pathlib import Path
from my_modules.abc_modules.files_and_folders import now_time_file_name


def upi_qrcode_generate(upi_id="TelegramBot@apl",
                        am=99,
                        pn="Connecting%20to%20Official%20Server...",
                        tn="Online%20Bot%20Service%20Used%20Plans%20Running%20Online%20Server",
                        folder: Path = Path(
                            "files_and_media") / "upi_generate_folder",
                        scale: str = 10,
                        ):
    '''
    If i will not pass any folder it will be using images/ upi_qr_code
    returns qr path which is the image path, to use it in image place
    Scale is for pixel per one littel square dot
    '''
    qr_saving_folder = Path(folder)
    qr_saving_folder.mkdir(parents=True, exist_ok=True)

    upi_link = f"upi://pay?pa={upi_id}&am={am}&pn={pn}&tn={tn}"
    qr = segno.make(upi_link, error="m")

    now_time_str = now_time_file_name()
    qr_code_name = now_time_str + f"_am_{am}_" + ".png"
    qr_path = qr_saving_folder / qr_code_name

    qr.save(qr_path, scale= scale)
    # qr.show()

    return qr_path






