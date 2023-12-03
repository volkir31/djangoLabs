import requests
from django.shortcuts import render, redirect

from . import models


def index(request):
    return render(request, 'index.html', {'users': models.User.objects.all()})


def find_user(request):
    with open('./main/accessKey.txt') as f:
        access_key = f.readline()
    vk_id = request.GET.get('userId')
    response = requests.get(f"https://api.vk.com/method/users.get?user_ids={vk_id}&access_token={access_key}&v=5.131")

    response = Data(response.json()['response'][0])

    if not models.User.objects.filter(vk_id=response.id).exists():
        user = models.User(name=response.first_name, surname=response.last_name, vk_id=response.id)
        user.save()
        photos = requests.get(
            f"https://api.vk.com/method/photos.get?owner_id={response.id}&album_id=profile&extended=1&access_token={access_key}&v=5.131").json()[
            'response']['items']
        for photo in photos:
            sizes = photo['sizes']
            photo = models.UserImages(user_id=user.id, url=sizes[-1]['url'])
            photo.save()
    else:
        user = models.User.objects.get(vk_id=response.id)
    return redirect(f"/user/{user.id}")


def user_card(request, user_id: int):
    user = models.User.objects.get(id=user_id)
    photos = models.UserImages.objects.filter(user_id=user.id).all()

    return render(request, 'user.html', {
        'user': user,
        'photos': photos
    })


class Data:
    id: int
    first_name: str
    last_name: str
    can_access_closed: bool
    is_closed: bool

    def __init__(self, array: dict):
        self.id = array['id']
        self.first_name = array['first_name']
        self.last_name = array['last_name']
        self.can_access_closed = array['can_access_closed']
        self.is_closed = array['is_closed']
