import requests

from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from tempfile import NamedTemporaryFile
from rest_framework.exceptions import ValidationError


class Img(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to='', blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    parent_picture = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.pk}, {self.name}, {self.parent_picture}'

    def save(self, *args, **kwargs):
        if not self.parent_picture:
            # Обрабатываем ошибку (url + img)
            if self.url and self.picture:
                raise ValidationError(detail={"__all__": "Two field"}, code=400)

            if self.url:
                # Если есть адрес - запрашиваем картинку и сохраняем ее
                response = requests.get(self.url)
                img = Image.open(BytesIO(response.content))
                name = self.url.split('/')[-1]
    
                self.name = name
                self.width, self.height = img.size
    
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()
                self.picture = File(file=img_temp, name=name)
    
                super(Img, self).save(*args, **kwargs)
                return
    
            if self.picture:
                self.name = self.picture.file.name
                self.width, self.height = self.picture.width, self.picture.height
                super(Img, self).save(*args, **kwargs)
                return
        # Resize
        self.pk = None
        super(Img, self).save(*args, **kwargs)




