from enum import Enum

from django.db import models
import uuid
from listings.models import Listing
from users.models import User
# Create your models here.



class Status(Enum):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    PAID = 'Paid'
    CANCELED = 'Canceled'
    COMPLETED = 'Completed'



class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing_id = models.ForeignKey(Listing)
    guest_id = models.ForeignKey(User)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=3)
    status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Status])    
    created_at = models.DateField()