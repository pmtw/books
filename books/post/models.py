from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_id = models.IntegerField(null=True, blank=True)
    owner = models.CharField(max_length=10)
    author_fn = models.CharField(max_length=10)
    author_sn = models.CharField(max_length=14)
    title = models.CharField(max_length=64)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True)
#    tags = models.CharField(
#   verbose_name=u'Related tags', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['-created']

    @property
    def number_of_comments(self):
        return self.comment_set.count()

    def __unicode__(self):  # __str__ on Python 3
        return u'{}...'.format(self.title[:10])

    
class Comment(models.Model):
    post=models.ForeignKey('post.Post')
    content = models.TextField()
    author = models.ForeignKey(User, null=True)
    
    def __unicode__(self):
        return self.content
