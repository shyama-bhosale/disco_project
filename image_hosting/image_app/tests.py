from django.test import TestCase

# Create your tests here.


# from django.contrib.auth.models import User
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Image
# from api.serializers import ImageSerializer


# class ImageTests(APITestCase):
#     def setUp(self):
#         self.user1 = User.objects.create_user(
#             username='testuser1', password='testpass1')
#         self.user2 = User.objects.create_user(
#             username='testuser2', password='testpass2')

#         self.image1 = SimpleUploadedFile(
#             "test1.png", b"file_content", content_type="image/png")
#         self.image2 = SimpleUploadedFile(
#             "test2.png", b"file_content", content_type="image/png")
#         self.image3 = SimpleUploadedFile(
#             "test3.png", b"file_content", content_type="image/png")

#         Image.objects.create(user=self.user1, image=self.image1)
#         Image.objects.create(user=self.user2, image=self.image2)

#         self.client.force_authenticate(user=self.user1)

#     def test_upload_image(self):
#         url = reverse('image-list')
#         data = {'image': self.image3}
#         response = self.client.post(url, data, format='multipart')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Image.objects.count(), 3)
#         self.assertEqual(Image.objects.last().user, self.user1)

#     def test_list_images(self):
#         url = reverse('image-list')
#         response = self.client.get(url)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_retrieve_image(self):
#         image_id = Image.objects.first().id
#         url = reverse('image-detail', args=[image_id])
#         response = self.client.get(url)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['id'], image_id)
#         self.assertEqual(response.data['user'], self.user1.id)

#     def test_delete_image(self):
#         image_id = Image.objects.first().id
#         url = reverse('image-detail', args=[image_id])
#         response = self.client.delete(url)

#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Image.objects.count(), 1)

#     def test_update_image(self):
#         image_id = Image.objects.first().id
#         url = reverse('image-detail', args=[image_id])
#         data = {'image': self.image3}
#         response = self.client.patch(url, data, format='multipart')

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Image.objects.count(), 2)
#         self.assertEqual(Image.objects.last().image.name, 'images/test1.png')

