from PIL import Image
import exifread
import os


class ImageProcessor:
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

    def __init__(self, upload_dir: str):
        self.upload_dir = upload_dir
        os.makedirs(upload_dir, exist_ok=True)

    def _allowed(self, filename: str) -> bool:
        return "." in filename and \
            filename.rsplit(".", 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def save_and_extract(self, file_storage):
        if not file_storage or not self._allowed(file_storage.filename):
            return {}

        filepath = os.path.join(self.upload_dir, file_storage.filename)
        file_storage.save(filepath)

        metadata = {}

        try:
            with open(filepath, "rb") as f:
                tags = exifread.process_file(f, details=False)

            for tag, value in tags.items():
                if tag.startswith("EXIF") or tag.startswith("GPS"):
                    metadata[tag] = str(value)

        except Exception:
            pass

        try:
            img = Image.open(filepath)
            metadata["resolution"] = f"{img.width}x{img.height}"
            metadata["format"] = img.format
        except Exception:
            pass

        return metadata