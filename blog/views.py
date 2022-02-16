from django.shortcuts import render
from blog.forms import CommentForm
from blog.models import Post
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from news.models import New
from django.core.paginator import Paginator
from main.models import contact_us,footer_comment,navbar_basic,navbar_up,NavbarUnder,service,comment_center
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.urls import reverse

class blog_index(TemplateView):
    template_name = "blog_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by("-created_on")
        context['menus'] = navbar_basic.objects.all()
        context['navbarunder'] = NavbarUnder.objects.all()
        context['contact_us'] = contact_us.objects.all()
        context['header'] = navbar_up.objects.all()
        context['service'] = service.objects.all()
        context['footer_comments'] = footer_comment.objects.all()
        context['news'] = New.objects.all().order_by("-created_on")
        return context

def index(request):
    posts = Post.objects.all().order_by("-created_on")
    contact = contact_us.objects.all()
    menu = navbar_basic.objects.all()  
    footer_comments = footer_comment.objects.all()
    contact_uss = contact_us.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,
                  'index.html',
                  {'items': posts,'contacts': contact,'menu':menu,'footer_comments':footer_comments,'contact_us':contact_uss})      
    
def blog_detail_old(request, pk):
    post = Post.objects.get(pk=pk)
    posts = Post.objects.all()
    menu = navbar_basic.objects.all() 
    contact = contact_us.objects.all()
    footer_comments = footer_comment.objects.all()
    comments = Comment.objects.filter(post=post)
    services = service.objects.filter(post=post)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return redirect('blog_detail',pk)
            #return HttpResponseRedirect(reverse('blog_detail',pk) )
    context = {"post": post,"items": posts,'menu':menu,"contacts": contact,"footer_comments": footer_comments, "comments": comments, "form": form}
    return render(request, "blog_detail.html", context)

def blog_detail(request,pk):
    posts= Post.objects.get(pk=pk)
    news = New.objects.all().order_by("-created_on")
    contact = contact_us.objects.all()
    header = navbar_up.objects.all()
    menu = navbar_basic.objects.all() 
    navbarunder = NavbarUnder.objects.all()
    footer_comments = footer_comment.objects.all()
    post = Post.objects.all()
    services = service.objects.all()
    comment_centers = comment_center.objects.all()
    return render(request,
                  'blog_detail.html',
                  {'item':posts,'items': news,'contacts': contact,'comment_center': comment_centers,'service': services,'header': header,'menus':menu,'navbarunder':navbarunder,'footer_comments':footer_comments,'post':post,})