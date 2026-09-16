import cloudinary
import cloudinary.uploader
from src.config import settings

# Настройка Cloudinary (можно перенести в config, если захотите)
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret",
    secure=True
)

class UploadImage:
    @staticmethod
    def upload_image(file, public_id: str):
        r = cloudinary.uploader.upload(file, public_id=public_id, overwrite=True)
        return r
