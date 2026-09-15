from django.db import models
import uuid
from bookings.models import Booking
# Create your models here.



class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking_id = models.ForeignKey(Booking)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateField()
