# views.py

#code below is working
from rest_framework import generics, permissions
from image_app.models import Image
from .serializers import ImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# from image_app.models import Image, AccountPlan, ExpiringLink
# from .serializers import ImageSerializer, AccountPlanSerializer
from datetime import datetime, timedelta
import random
import string

class ImageList(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Image.objects.filter(user=self.request.user)
        return queryset



# class ImageViewSet(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     parser_classes = [MultiPartParser, FormParser]

#     def create(self, request):
#         account_plan = request.user.account_plan

#         if account_plan is None:
#             return Response({'error': 'User does not have an account plan.'}, status=status.HTTP_400_BAD_REQUEST)

#         if 'image' not in request.data:
#             return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

#         image = Image.objects.create(user=request.user, image=request.data['image'])
#         image.thumbnail_200 = image.image
#         image.save()

#         if account_plan.name == 'Premium' or account_plan.name == 'Enterprise':
#             image.thumbnail_400 = image.image
#             image.save()

#         if account_plan.name == 'Enterprise':
#             token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
#             expiry_time = datetime.now() + timedelta(seconds=request.data.get('expiry_time', 300))
#             expiring_link = ExpiringLink.objects.create(image=image, token=token, expiry_time=expiry_time)
#             expiring_link.save()

#             return Response({'expiring_link': request.build_absolute_uri('/images/' + str(image.id) + '/link/')}, status=status.HTTP_201_CREATED)

#         return Response({'thumbnail_200': request.build_absolute_uri(image.thumbnail_200.url





