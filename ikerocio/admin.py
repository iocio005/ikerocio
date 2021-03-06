from django.contrib import admin
from ikerocio.models import WelcomePage, FirstSection, SecondSection, ThirdSection, FourthSection, FifthSection, WebImages, Configuration, Icon, ContactMessage
from django_markdown.admin import MarkdownModelAdmin

class AbstractSectionAdmin(MarkdownModelAdmin):
    fields = ('body', 'background', 'background_color', 'publish')
    class Meta:
        abstract = True


class AdminWelcome(AbstractSectionAdmin):
    fields = ('body', 'undertitle', 'background', 'publish')
    list_display = ['body', 'undertitle', 'publish', 'background', 'created']
    pass

class AdminSecPage(AbstractSectionAdmin):
    list_display = ['created', 'publish','body']

class AdminThirdPage(AbstractSectionAdmin):
    list_display = ['created', 'publish','body']

class AdminFourPage(AbstractSectionAdmin):
    list_display = ['created', 'publish','body']

class AdminFifthPage(AbstractSectionAdmin):
    list_display = ['created', 'publish','body']

class AdminBackgroundImage(AbstractSectionAdmin):
    fields = ('title', 'background', 'path')
    list_display = ['title', 'background' ,'path']

class AdminSixthPage(AbstractSectionAdmin):
    list_display = ['created', 'publish','body']

class AdminConfiguration(MarkdownModelAdmin):
    fields = ('favicon', 'web_title', 'welcome_title', 'welcome_icon', 'publish')
    list_display = ['favicon', 'web_title', 'publish', 'created']

class AdminContactMessage(MarkdownModelAdmin):
    fields = ('name', 'email', 'body')
    list_display = ('name','email','body','created')
admin.site.register(WelcomePage, AdminWelcome)
admin.site.register(FirstSection, AdminSecPage)
admin.site.register(SecondSection, AdminThirdPage)
admin.site.register(ThirdSection, AdminFourPage)
admin.site.register(FourthSection, AdminFifthPage)
admin.site.register(WebImages, AdminBackgroundImage)
admin.site.register(FifthSection, AdminSixthPage)
admin.site.register(Configuration, AdminConfiguration)
admin.site.register(Icon)
admin.site.register(ContactMessage, AdminContactMessage)