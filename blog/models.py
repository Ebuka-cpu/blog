from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='post_pics')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class Comment(models.Model):
    content = models.TextField(max_length=150, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Comment by {}  {}'.format(self.author, self.content)






