from django.db import models
import uuid
from listings.models import Listing
# Create your models here.


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing_id = models.ForeignKey(Listing)
    guest_id = models.ForeignKey()