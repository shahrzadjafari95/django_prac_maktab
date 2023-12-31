from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    tag = TaggableManager()
    category = models.ManyToManyField(Category)  # any post possible have several category and any category possible
    # have several posts
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # any author possible have several posts but
    # any post have one author
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return "{}-{}".format(self.title, self.pk)

    # return self.title

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # any post possible have many comments
    # If a post is deleted, all its comments will also be deleted :on_deleted = cascade
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
