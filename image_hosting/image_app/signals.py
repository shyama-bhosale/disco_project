# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.files import File
# from django.conf import settings
# from .models import Image
# from PIL import Image as PILImage
# import os

# @receiver(post_save, sender=Image)
# def generate_thumbnail_images(sender, instance, created, **kwargs):
#     if created:
#         image_path = instance.image.path
#         with PILImage.open(image_path) as img:
#             thumbnail_200 = img.copy()
#             thumbnail_400 = img.copy()

#             thumbnail_200.thumbnail(settings.THUMBNAIL_SIZE_200)
#             thumbnail_400.thumbnail


##delete this whole file if moving to the last code