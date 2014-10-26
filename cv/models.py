from django.db import models
from ikerocio.models import Icon, WebImages

class Milestone(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    year = models.IntegerField('Year')

    class Meta:
        ordering = ['-year']
        abstract = True

    def __str__(self):
       return self.title.encode('ascii', 'ignore')

class ExperienceMilestone(Milestone):
    work_name = models.CharField('Work', max_length=30)

class EducationMilestone(Milestone):
    pass

class FontIcon(models.Model):
    name = models.CharField("Icon Name", max_length=30, help_text="Short description about")
    f_icon = models.CharField('Font awesome', max_length=50, help_text="Font Awesome Icon. Set content value")

    def __str__(self):
        return self.name

class Contact(models.Model):
    icon = models.ForeignKey(Icon)
    contact = models.CharField('Contact Name', max_length=100)
    description = models.CharField('Contact Description', max_length=200, blank=True)

    def __str__(self):
        return self.contact.encode('ascii', 'ignore')

class Skill(models.Model):
    name = models.CharField('Skill Name', max_length=50)
    percent = models.FloatField('Knowledge percent', help_text='Value between 0 and 1')

    def __str__(self):
        return self.name.encode('ascii', 'ignore')

class Language(models.Model):
    language = models.CharField('Language', max_length=50)
    percent = models.FloatField('Language percent', blank=True, default=0.5)

    def __str__(self):
        return self.language.encode('ascii', 'ignore')

class Hobbies(models.Model):
    hobbie = models.CharField('Hobbie', max_length=50)
    font_icon = models.ManyToManyField(FontIcon)

    def __str__(self):
        return self.hobbie.encode('ascii', 'ignore')

class Conferences(models.Model):
    name = models.CharField('Conference name',max_length=50)
    place = models.CharField('Conference place to be', blank=True, max_length=50)
    year = models.IntegerField('Year')

    def __str__(self):
        return self.name.encode('ascii', 'ignore')

    class Meta:
        ordering = ['-year']

class ProjectType(models.Model):
    type = models.CharField('Type', max_length=40)

    def __str__(self):
        return self.type

class Project(models.Model):
    title = models.TextField('Title', max_length=70)
    picture = models.ForeignKey(WebImages)
    url = models.URLField('URL')
    description = models.TextField('Description about project')
    publish = models.BooleanField('Is Visible?', default=False)
    type = models.ManyToManyField(ProjectType)
    slug = models.SlugField('slug')

    def __str__(self):
        return '%s' % self.title

class CV(models.Model):
    first_presentation = models.TextField('Presentation', help_text='Presentation')
    about_me = models.TextField('About me', help_text='About me')
    education = models.ManyToManyField(EducationMilestone)
    experience = models.ManyToManyField(ExperienceMilestone)
    contact = models.ManyToManyField(Contact)
    skill = models.ManyToManyField(Skill)
    language = models.ManyToManyField(Language)
    hobbies = models.ManyToManyField(Hobbies)
    conferences = models.ManyToManyField(Conferences)
    publish = models.BooleanField('Publish?', default=False)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.first_presentation.encode('ascii', 'ignore')


