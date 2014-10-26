from django.shortcuts import render_to_response, HttpResponse, get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from ikerocio.forms import ContactForm
from ikerocio.models import ContactMessage, Configuration, WelcomePage, FirstSection, SecondSection, ThirdSection, FourthSection, FifthSection
from cv.models import Project
from django.http import HttpResponseRedirect
#from forms import ContactForm
def select_bg(data):
    if data.background:
        return data.background.background.url
    else:
        return data.background_color

def home(request):
    config = get_object_or_404(Configuration, publish=True)
    welcome_page = get_object_or_404(WelcomePage, publish=True)
    welcome_page.bg = select_bg(welcome_page)
    aboutme_page = get_object_or_404(FirstSection, publish=True)
    aboutme_page.bg = select_bg(aboutme_page)
    project_page = get_list_or_404(Project, publish=True)
    cv_page = get_object_or_404(SecondSection, publish=True)
    cv_page.bg = select_bg(cv_page)
    blog_page = get_object_or_404(ThirdSection, publish=True)
    blog_page.bg = select_bg(blog_page)
    picture_page = get_object_or_404(FourthSection, publish=True)
    picture_page.bg = select_bg(picture_page)
    contact_page =get_object_or_404(FifthSection, publish=True)
    contact_page.bg = select_bg(contact_page)
    form = ContactForm()
    data = {'config': config, 'welcome_page': welcome_page, 'aboutme_page': aboutme_page, 'project_page': project_page, 'cv_page': cv_page,
           'blog_page': blog_page, 'picture_page': picture_page, 'contact_page': contact_page, 'form': form}

    return render_to_response('index.html', data, context_instance=RequestContext(request))


@csrf_exempt
def check_form(request):
    if request.is_ajax():
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        r = ContactMessage(name=name, email=email, body=body).save()
    return HttpResponse(content_type='text')