from django.db import models


class Instruction(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
