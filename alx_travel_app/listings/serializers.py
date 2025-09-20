from rest_framework import serializers
from .models import Listing, Booking, Review

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'created_at', 'bookings', 'reviews_count']

    def get_reviews_count(self, obj):
        return obj.reviews.count()
