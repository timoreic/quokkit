from django.db import models
import uuid


class Instruction(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
