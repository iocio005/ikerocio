from django.contrib import admin
from blog.models import Post, Tag, BlogConfiguration, Categories
from django_markdown.admin import MarkdownModelAdmin

class AdminTag(admin.ModelAdmin):
    list_display = ('slug',)


def set_post_lived(self, request, queryset):
    """ all selected post will be lived    """
    rows_updated = queryset.update(is_live = True)
    if rows_updated == 1:
        message_bit = 'One post has been modified '
    else:
        message_bit = '%s posts has been modified'
    self.message_user(request, '%s successfully' %message_bit)
set_post_lived.short_description = 'Change selected post "live" option'

class AdminPost(MarkdownModelAdmin):
    list_display = ('title', 'get_author_name','publish', 'created', 'send_tweet')
    ordering = ('-created', 'id')
    prepopulated_fields = {'slug':('title',)}


class AdminBlog(admin.ModelAdmin):
    list_display = ('title', 'quote', 'created', 'publish')
    ordering = ('-created',)

admin.site.register(BlogConfiguration, AdminBlog)
admin.site.register(Post, AdminPost)
admin.site.register(Tag, AdminTag)
admin.site.register(Categories)
