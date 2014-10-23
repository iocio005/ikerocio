from django.contrib.sites.models import models

class TwitterApi(models.Model):
    consumer_key = models.CharField('Consumer Key', max_length=300, help_text='Consumer Key (Api Key)')
    consumer_secret = models.CharField('Consumer Secret', max_length=300, help_text='Consumer Secret (Api Key)')
    access_token = models.CharField('Access Token', max_length=300, help_text='Access Token')
    access_token_secret = models.CharField('Access Token Secret', max_length=300)
    default_word = models.CharField('Default words for new tweet', max_length=200, help_text='***: "Titulo del Post" en http://ikerocio.com')
    default_word_long = models.CharField('Default words for new tweet long', max_length=200, help_text='*** en http://ikerocio.com/url-del-post')

    def __str__(self):
        return self.default_word.encode('ascii', 'ignore')
