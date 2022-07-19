# posts/serializers.py
from rest_framework import serializers
from .models import Post,Author

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    # author=AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('__all__')
        depth=1
        

        