from django.conf import settings
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name_tag = models.CharField(max_length=50)

    class Meta:
        ordering = ['name_tag']

    def __str__(self):
        return self.name_tag

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag, related_name='posts')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Command(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commands")
    title_command = models.CharField(max_length=50)
    command = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title_command