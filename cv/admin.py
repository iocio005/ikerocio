from django.contrib import admin
from cv.models import CV, EducationMilestone, ExperienceMilestone, Language, Skill, Conferences, Hobbies, Contact, FontIcon, Project, ProjectType
from django_markdown.admin import MarkdownModelAdmin

class AdminCV(MarkdownModelAdmin):
    pass

class AdminEducation(MarkdownModelAdmin):
    fields = ('title', 'year', 'description')

class AdminExperience(MarkdownModelAdmin):
    fields = ('title', 'year', 'work_name', 'description')

class AdminProject(MarkdownModelAdmin):
    fields = ('title', 'picture', 'description', 'url', 'publish', 'slug', 'type')
    list_display = ['title', 'picture', 'url', 'publish', 'slug']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(CV, AdminCV)
admin.site.register(EducationMilestone, AdminEducation)
admin.site.register(ExperienceMilestone, AdminExperience)
admin.site.register(Language)
admin.site.register(Skill)
admin.site.register(Conferences)
admin.site.register(Hobbies)
admin.site.register(Contact)
admin.site.register(FontIcon)
admin.site.register(Project, AdminProject)
admin.site.register(ProjectType)
