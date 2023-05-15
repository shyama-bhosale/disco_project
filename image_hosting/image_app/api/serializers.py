

#code from below is working
from rest_framework import serializers
from image_app.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'user', 'image', 'uploaded_at')



    # class ImageSerializer(serializers.ModelSerializer):
    #     thumbnail_200 = serializers.ImageField(read_only=True)
    #     thumbnail_400 = serializers.ImageField(read_only=True)

    #     class Meta:
    #         model = Image
    #         fields = ('id', 'user', 'image', 'thumbnail_200', 'thumbnail_400', 'created_at')

    # class AccountPlanSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = AccountPlan
    #         fields = ('id', 'name', 'thumbnail_sizes', 'link_to_original', 'generate_expiring_links')