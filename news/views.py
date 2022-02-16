from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from news.models import New
from main.models import contact_us,footer_comment,navbar_basic,navbar_up,NavbarUnder,service,comment_center
from blog.models import Post,Comment
from django.core.paginator import Paginator
from django.urls import reverse

# Create your views here.
class new_index(TemplateView):
    template_name = "new_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = navbar_basic.objects.all()
        context['navbarunder'] = NavbarUnder.objects.all()
        context['contact_us'] = contact_us.objects.all()
        context['footer_comments'] = footer_comment.objects.all()
        context['news'] = New.objects.all().order_by("-created_on")
        return context
        
def index(request):
    news = New.objects.all().order_by("-created_on")
    contact = contact_us.objects.all()
    menu = navbar_basic.objects.all() 
    footer_comments = footer_comment.objects.all()
    post = Post.objects.all()
    header = navbar_up.objects.all()
    services = service.objects.all()
    navbarunder = NavbarUnder.objects.all()
    comment_centers = comment_center.objects.all()
    paginator = Paginator(news, 4)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request,
                  'new_index.html',
                  {'items': news,'contacts': contact,'comment_center': comment_centers,'service': services,'header': header,'menus':menu,'navbarunder':navbarunder,'footer_comments':footer_comments,'post':post,}) 
         
def new_detail(request,title):
    news = New.objects.get(title=title)
    newsall = New.objects.all()
    contact = contact_us.objects.all()
    header = navbar_up.objects.all()
    menu = navbar_basic.objects.all() 
    navbarunder = NavbarUnder.objects.all()
    footer_comments = footer_comment.objects.all()
    post = Post.objects.all()
    services = service.objects.all()
    comment_centers = comment_center.objects.all()
    context = {"items": news,"itemall": newsall,"contacts": contact,"comment_center": comment_centers,"service": services,"header": header,"menus":menu,"navbarunder":navbarunder,"footer_comments":footer_comments,"post":post}
    return render(request, "new_detail.html", context)              
# class new_detail(TemplateView):
    # template_name = "new_detail.html"

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['menu'] = navbar_basic.objects.all()
        # context['contact_us'] = contact_us.objects.all()
        # context['footer_comments'] = footer_comment.objects.all()
        # context['news'] = New.objects.all().order_by("-created_on")
        # return context