import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "giphyclone.settings")
django.setup()

from main.models import Gif
from django.conf import settings

payload = {'api_key': settings.GIPHY_API_KEY}
total = 50
for i in range(0, total):
    data = requests.get('http://api.giphy.com/v1/gifs/random', params=payload).json()['data']
    gif = Gif.objects.create(url=data['fixed_height_downsampled_url'], uploader_name='system_admin', title=data['title'])
    print(f"gif number {i+1}/{total} created successfully")

