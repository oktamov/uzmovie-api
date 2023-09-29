from rest_framework import serializers

from common.serializers import CategoryListSerializer
from movies.models import Movie, Review


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "full_name", "comment", "parent",)


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    liked = serializers.SerializerMethodField()
    category = CategoryListSerializer(many=True)

    def get_liked(self, obj):
        user = self.context['request'].user
        return obj.liked.filter(id=user.id).exists()

    class Meta:
        model = Movie
        fields = (
            'id', 'name', 'slug', 'movie_year', 'duration', 'country', 'video_url', 'img_url', 'poster_url',
            'description',
            'created_at', 'liked', 'num_likes', 'category', 'reviews')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data["category"] = instance.category.name
    #     return data


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", 'name', 'slug', 'img_url', 'movie_year')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", 'full_name', 'comment', 'parent')
