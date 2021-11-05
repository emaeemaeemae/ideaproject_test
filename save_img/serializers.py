from rest_framework import serializers

from .models import Img


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = '__all__'

    # def to_representation(self, data):
    #     data = super(ImgSerializer, self).to_representation(data)
    #     data['parent_picture'] = 0 if data.get('id') % 2 else 1
    #     return data
