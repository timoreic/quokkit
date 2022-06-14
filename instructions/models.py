from django.db import models
from django.contrib.auth import get_user_model
import uuid


class Instruction(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Step(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    number = models.IntegerField()
    instruction = models.ForeignKey(
        Instruction,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    amount = models.CharField(max_length=200)
    instruction = models.ForeignKey(
        Instruction,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.ManyToManyField(Instruction)

    def __str__(self):
        return self.title
