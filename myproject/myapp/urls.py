from django.urls import path
from .views import upload_image,upload_image_form,get_image

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('upload/form/', upload_image_form, name='upload_image_form'),
    path('image/<int:image_id>/', get_image, name='get_image'),
]