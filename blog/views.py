from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from blog.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from collections import Counter

# Create your views here.

"""
class BlogIndex(generic.ListView):
    queryset = Post.objects.published()
    template_name = 'post.html'
    paginate_by = 2
"""

class BlogDetail(generic.DetailView):
    model = Post
    template_name = 'post-detail.html'


def posts(request, tag='default', category='default', page=1):
    blog_config = BlogConfiguration.objects.get(publish=True)

    if tag is not 'default':
        posts_list = get_list_or_404(Post, tags__slug=tag)
    elif category is not 'default':
        posts_list = get_list_or_404(Post, category__slug=category)
    else:
        posts_list = Post.objects.all()
    tag_objects = []
    category_objects = []
    z = [tag_objects.append(ta.slug)for t in posts_list for ta in t.tags.all() ]
    z = [category_objects.append(ca.slug)for c in posts_list for ca in c.category.all()]
    tag_counter = dict(Counter(tag_objects))
    cat_counter = dict(Counter(category_objects))
    paginator = Paginator(posts_list, 10) # Show 10 posts per page

    number_pages = range(1, paginator.count+1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    data = {"posts_list" : posts, "number_pages" : number_pages, 'blog': blog_config, 'tags':tag_counter , 'categories': cat_counter}
    return render_to_response('post.html', data, context_instance=RequestContext(request))