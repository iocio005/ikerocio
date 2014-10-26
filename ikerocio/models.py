from django.db import models
from tinymce.models import HTMLField
from webapi.models import EasyMail as Mail
from django.conf import settings
from webapi.easymail import EasyMail
import thread


def get_upload_path():
    return settings.STATIC_URL + '/upload/images/'


class WebImages(models.Model):
    title = models.CharField('Title', max_length=30)
    background = models.FileField('Background', upload_to='static/upload/images/', default='', blank=True)
    path = models.CharField('Image URL', blank=True, max_length=200)

    def save(self, *args, **kwargs):
        self.path = self.background.url
        super(WebImages, self).save(*args, **kwargs)

    class Meta:
        verbose_name, verbose_name_plural = 'Picture', 'Pictures'

    def __str__(self):
        return self.title


class Icon(models.Model):
    icon = models.CharField('Fa Icon', default='', max_length=20)

    def __str__(self):
        return self.icon


class Configuration(models.Model):
    favicon = models.ForeignKey(WebImages)
    web_title = models.CharField('Web Title', default='Iker Ocio - Web Developer', max_length=30)
    welcome_title = models.CharField('Welcome Name', default='Iker Ocio', max_length=40)
    welcome_icon = models.ForeignKey(Icon)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField('Publish?', default=False)


    def __str__(self):
        return '%s' % (self.favicon)


class Page(models.Model):
    body = HTMLField(max_length=1000, default='Lorem Ipsum')
    background = models.ForeignKey(WebImages, blank=True, null=True)
    background_color = models.CharField('Background color', default='#FFFFFF', help_text='HEX color', max_length=50)
    publish = models.BooleanField('Publish?', default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s' % (self.body.encode('ascii', 'ignore')[:30])


class WelcomePage(Page):
    undertitle = models.CharField('Under Title', max_length=50, default='')

    class Meta:
        verbose_name, verbose_name_plural = '1 Welcome Page', '1 Welcome Page'


class FirstSection(Page):
    class Meta:
        verbose_name, verbose_name_plural = '2 About Me', '2 About Me'


class SecondSection(Page):
    class Meta:
        verbose_name, verbose_name_plural = '3 CV', '3 CV'


class ThirdSection(Page):
    class Meta:
        verbose_name, verbose_name_plural = '4 Blog', '4 Blog'


class FourthSection(Page):
    class Meta:
        verbose_name, verbose_name_plural = '5 Pictures', '5 Pictures'


class FifthSection(Page):
    class Meta:
        verbose_name, verbose_name_plural = '6 Contact me', '6 Contact me'


def send_email(name, email, body):
    print 'asdsad'
    mail = Mail.objects.get()
    mail_inst = EasyMail.loggin(mail.username, mail.password)
    mail_inst.send(mail.username, '[http://ikerocio.com]-%s'%name, "Nombre: %s - Mail: %s\n%s" %(name, email, body))

class ContactMessage(models.Model):
    name = models.CharField('Name', max_length=30)
    email = models.EmailField('Email', max_length=30)
    body = models.TextField('Message', max_length=30)
    has_read = models.BooleanField('Are has read?', default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.email)

    def save(self, *args, **kwargs):
        super(ContactMessage, self).save(*args, **kwargs)
        try:
            thread.start_new_thread(send_email(self.name, self.email, self.body),'arg')
        except Exception as e:
            print e
