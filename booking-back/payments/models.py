from django.db import models
from bookings.models import Booking
import uuid
from enum import Enum
# Create your models here.



class Status(Enum):
    PENDING = "Pending"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    REFUNDED = "Refunded"




class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking_id = models.ForeignKey(Booking)
    idempotency_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=2)
    status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Status])    
    provider_payment_id = models.TextField(max_length=155)
