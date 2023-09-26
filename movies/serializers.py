from rest_framework import serializers

from movies.models import Movie, Review


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "full_name", "comment", "parent",)


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    liked = serializers.SerializerMethodField()

    def get_liked(self, obj):
        user = self.context['request'].user
        return obj.liked.filter(id=user.id).exists()

    class Meta:
        model = Movie
        fields = (
            'id', 'name', 'movie_year', 'duration', 'country', 'video_url', 'img_url', 'poster_url', 'description',
            'created_at', 'liked', 'num_likes', 'category', 'reviews')


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", 'name', 'slug', 'img_url', 'movie_year')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", 'full_name', 'comment', 'parent')
