from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from cv.models import CV
def index(request):
    cv = CV.objects.get(publish = True)
    for percent in cv.skill.all():
        percent.percent = float(str(percent.percent).replace(',','.'))
    data = {'cv': cv}
    return render_to_response('cv.html', data,context_instance=RequestContext(request))