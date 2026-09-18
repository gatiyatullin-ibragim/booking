from django.db import models
from django.urls import reverse
# Create your models here.

class booking(models.Model):
    id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey()
    guest_id = models.ForeignKey()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()


def __str__(self):
    return self.id