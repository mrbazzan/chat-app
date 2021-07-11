
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Message(models.Model):
    user_message = models.CharField(max_length=100000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} in {str(self.room)}"
