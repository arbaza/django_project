from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

#python manage.py makemigrations
#python manage.py migrate
    
#Creating a post in the database through django shell
# python manage.py shell
# from blog.models import Post
# from django.contrib.auth.models import User
# User.objects.all()
# User.objects.first()
# User.objects.filter(username='arbaza')
# user = User.objects.filter(username='arbaza').first()
# user.id or user.pk
# Post.objects.all() check post
# post_1 = Post(title = 'Blog 1', content = 'First Post Content!', author = user)
# post_1.save()
# user.post_set.all()

