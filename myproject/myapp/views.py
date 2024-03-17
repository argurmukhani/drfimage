from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import image_tbl
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseServerError

from .serializers import ImageSerializer

def upload_image_form(request):
    return render(request, 'upload.html')

@api_view(['POST'])
def upload_image(request):
    try:
        image_file = request.FILES.get('image')
        if image_file:
            image_data = image_file.read()
            image = image_tbl(image_data=image_data)
            image.save()
            return Response('Image uploaded successfully', status=status.HTTP_201_CREATED)
        else:
            return Response('No image provided', status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_image(request, image_id):
    try:
        image = image_tbl.objects.get(pk=image_id)
        image_data = image.image_data
        if image_data:
            return HttpResponse(image_data, content_type='image/jpeg')
        else:
            return HttpResponseNotFound('Image not found')
    except image_tbl.DoesNotExist:
        return HttpResponseNotFound('Image not found')
    except Exception as e:
        return HttpResponseServerError(str(e))