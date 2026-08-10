from pathlib import Path
import shutil

UPLOAD_FOLDER = Path("data/uploads")


class FileService:

    @staticmethod
    def save_file(file):
        """
        Save uploaded file to disk.
        """

        UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

        file_path = UPLOAD_FOLDER / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return file_path