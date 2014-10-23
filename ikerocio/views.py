from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from ikerocio.forms import ContactForm
from ikerocio.models import ContactMessage, Configuration, WelcomePage, FirstSection, SecondSection, ThirdSection, FourthSection, FifthSection
from django.http import HttpResponseRedirect
#from forms import ContactForm
def select_bg(data):
    if data.background.background:
        return data.background.background.url
    else:
        return data.background.color

def home(request):
    config = Configuration.objects.get(publish=True)
    welcome_page = WelcomePage.objects.get(publish=True)
    welcome_page.bg = select_bg(welcome_page)
    aboutme_page = FirstSection.objects.get(publish=True)
    aboutme_page.bg = select_bg(aboutme_page)
    cv_page = SecondSection.objects.get(publish=True)
    cv_page.bg = select_bg(cv_page)
    print cv_page.background.color
    print aboutme_page.background
    blog_page = ThirdSection.objects.get(publish=True)
    blog_page.bg = select_bg(blog_page)
    picture_page = FourthSection.objects.get(publish=True)
    picture_page.bg = select_bg(picture_page)
    contact_page = FifthSection.objects.get(publish=True)
    contact_page.bg = select_bg(contact_page)
    form = ContactForm()
    data = {'config': config, 'welcome_page': welcome_page, 'second_page': aboutme_page, 'third_page': cv_page,
           'blog_page': blog_page, 'picture_page': picture_page, 'contact_page': contact_page, 'form': form}

    return render_to_response('index.html', data, context_instance=RequestContext(request))

def check_form(request):
    if request.is_ajax():
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        print name+email+body
        #r = ContactMessage(name=name, email=email, body=body).save()
    return HttpResponse(content_type='text')