from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from alx_travel_app.listings.models import Listing, Booking, Review
from django.utils import timezone
import random
from datetime import timedelta

class Command(BaseCommand):
    help = "Seed the database with sample Listings, Bookings, and Reviews"

    def handle(self, *args, **kwargs):
        # Create demo users if not exists
        users = []
        for i in range(3):
            username = f"user{i}"
            user, created = User.objects.get_or_create(username=username, defaults={"email": f"{username}@example.com"})
            user.set_password("password123")
            user.save()
            users.append(user)

        # Create Listings
        listings_data = [
            {"title": "Beach House", "description": "A lovely house by the beach.", "price_per_night": 120.50, "location": "Miami"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.", "price_per_night": 80.00, "location": "Aspen"},
            {"title": "City Apartment", "description": "Modern apartment downtown.", "price_per_night": 100.00, "location": "New York"},
        ]

        listings = []
        for data in listings_data:
            listing, _ = Listing.objects.get_or_create(**data)
            listings.append(listing)

        # Create Bookings and Reviews
        for listing in listings:
            for user in users:
                start_date = timezone.now().date() + timedelta(days=random.randint(1, 30))
                end_date = start_date + timedelta(days=random.randint(2, 5))

                Booking.objects.get_or_create(
                    listing=listing,
                    user=user,
                    start_date=start_date,
                    end_date=end_date
                )

                Review.objects.get_or_create(
                    listing=listing,
                    user=user,
                    rating=random.randint(1, 5),
                    comment=f"Sample review by {user.username}"
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
