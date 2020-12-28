import os
import django
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from crawl_perfume.perfume.models import Image, Nhom_huong, Mui_huong, Pha_che, Thuong_hieu, Nuoc_hoa, Gia, Blog

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawl_perfume.settings')
django.setup()


def crawl_image(ten, url):
    image = Image.objects.create(ten=ten, image=url.split('/')[0])
    path = image.imagte.path
    content = requests.get(url=url).content
    default_storage(path, ContentFile(content))
    return image
