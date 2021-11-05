import os

from ideaproject_test import settings
from PIL import Image
from .models import Img
from .serializers import ImgSerializer
from django.core.files import File
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError


class ImgViewSet(viewsets.ModelViewSet):
    queryset = Img.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImgSerializer

    @action(detail=True, methods=['POST'], name='resize')
    def resize(self, request, *args, **kwargs):
        # Получаем родительскую картинку
        parent_picture_id = self.kwargs.get('pk')
        queryset = Img.objects.filter(pk=parent_picture_id)
        try:
            new_picture = queryset[0]
        except IndexError:
            raise ParseError('Wrong File ID')
        # new_picture = copy.deepcopy(picture)

        # new values
        new_picture.parent_picture = parent_picture_id
        # размеры для изменения картинки
        new_picture.width = request.data.get('width', new_picture.width)
        new_picture.height = request.data.get('height', new_picture.height)

        # изменяем картинку
        img = Image.open(new_picture.picture)
        new_size = (int(new_picture.width), int(new_picture.height))
        img.thumbnail(new_size)

        # сохраняем новые размеры
        new_picture.width, new_picture.height = img.size
        # сохраняем новую картинку
        my_path = os.path.dirname(os.path.dirname(__file__))
        temp_name = f'{new_picture.name}_{new_picture.width}_{new_picture.height}_temp.jpg'
        img.save(f'{my_path}{settings.MEDIA_URL}{temp_name}')

        # сохраняем новый объект
        with open(f'{my_path}{settings.MEDIA_URL}{temp_name}', 'rb') as f:
            new_picture.name = f'{new_picture.name}_{new_picture.width}_{new_picture.height}.jpg'

            new_picture.picture = File(file=f, name=new_picture.name)
            new_picture.save()
            serializer = self.get_serializer([new_picture], many=True)
        os.remove(f'{my_path}{settings.MEDIA_URL}{temp_name}')
        return Response(serializer.data)
