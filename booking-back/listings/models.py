import uuid

from django.db import models
from users.models import User
from django.contrib.gis.db import models

# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.PointField(
        srid=4336,
        geography=True,
        spatial_index=True,
        null=True,
        blank=True,
        verbose_name="Координаты"
    )

    class Meta:
        db_table="listings"