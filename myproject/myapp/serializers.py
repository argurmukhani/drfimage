from rest_framework import serializers
from .models import image_tbl

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image_tbl
        fields = ['image_id', 'image_data']