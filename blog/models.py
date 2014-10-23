from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from webapi.twitter import twitter_api
from datetime import datetime
class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.slug


class Categories(models.Model):
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    slug = models.SlugField('slug', max_length=200, help_text = 'nombre URL')
    body = HTMLField('Post Body')
    author = models.ManyToManyField(User, verbose_name = 'User')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()
    tags = models.ManyToManyField(Tag, verbose_name = 'Tag')
    category = models.ManyToManyField(Categories, verbose_name='Category')
    publish = models.BooleanField('Is Live', default=False, help_text='If False, not will be appear on the blog')
    send_tweet = models.BooleanField('Send Post Tweet', default=False, help_text='Do you want to send tweet about post?')

    def save(self, *args, **kwargs):
        if self.send_tweet:
            twitter_api(self.title, self.slug)
        ''' After save, send tweet '''
        super(Post, self).save(*args, **kwargs)
        #TO DO only tweet if is the first modification


    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'slug': self.slug})

    def get_author_name(self):
        return self.author.get().first_name

    class Meta:
        ordering = ['-created']
        verbose_name, verbose_name_plural = 'Blog Entry', 'Blog Entries'

    def __str__(self):
        return '%s' %(self.title)

    get_author_name.short_description = "Autor Name"


class BlogConfiguration(models.Model):
    title = models.CharField('Title', max_length=10, help_text='Title of Blog')
    quote = models.CharField('Short Quote', max_length=100, help_text='Short quote for Blog', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField('Publish?', default=False)