from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from app.models import blogItem,contactMessage,Category,commentItem
from django.core.paginator import Paginator
from libgravatar import Gravatar

# Create your views here.
def recentitem():
    recentitem=blogItem.objects.all().order_by('-id')[:4]
    return recentitem


def index(request):
    b=Category.objects.all()
    a=blogItem.objects.all()
    paginator= Paginator(a, 5) 
    page =request.GET.get('page')
    a=paginator.get_page(page)
    return render(request,'blog/blog.html',{"bgi": a,"cat":b,"recentitem":recentitem()})


def contact(request):
     if request.method=='POST':
         mail = request.POST['email']
         name = request.POST['name']
         subject = request.POST['subject']
         msg = request.POST['message']
         a=contactMessage(name=name,email=mail,subject=subject,message=msg)
         a.save()
         return HttpResponseRedirect('/contact/')
     else:
         b=Category.objects.all
         return render(request, 'blog/contact.html',{"cat":b})


def single(request):
    bid= request.GET['bid']
    item=blogItem.objects.filter(id=bid)
    comments=commentItem.objects.filter(blog=bid)
    b=Category.objects.all
    return render(request,'blog/blog_details.html',{"item":item,"cat":b,"recentitem":recentitem(),"comments":comments,"blog":bid})


def categoryfun(request):
    cate=request.GET['cate']
    item=blogItem.objects.filter(category__name__contains=cate)
    paginator= Paginator(item, 5) 
    page =request.GET.get('page')
    item =paginator.get_page(page)
    b=Category.objects.all
    return render(request,'blog/category.html',{"item":item,"cat":b,"cate":cate,"recentitem":recentitem()})

def search(request):
    searchitems=request.GET['searchitems']
    si=blogItem.objects.filter(name__icontains=searchitems)
    paginator= Paginator(si, 5) 
    page =request.GET.get('page')
    si =paginator.get_page(page)
    b=Category.objects.all
    return render(request, 'blog/search.html',{"item":si,"cat":b,"searchitems":searchitems,"recentitem":recentitem()})

def addcomment(request):
    if request.method=='POST':
         email = request.POST['email']
         name = request.POST['name']
         comment = request.POST['comment']
         blog= request.POST['blog']
         bid=blog
         blog=blogItem.objects.get(id=blog)
         g = Gravatar(email)
         a=commentItem(name=name,email=email,comment=comment,blog=blog,image=g.get_image())
         a.save()
         blog.commentcount += 1
         blog.save()
         return  HttpResponseRedirect('/single/?bid='+bid)
    else:
        return HttpResponse("error please go back and refresh")
    
def likeblog(request):
    blogid=request.GET['id']
    page =request.GET['page']
    print(blogid)
    item=blogItem.objects.get(id=blogid)
    item.like += 1
    item.save()
    print(item.like)
    return  HttpResponseRedirect('/?page='+page)

    
def like(request):
    blogid=request.GET['id']
    print(blogid)
    item=blogItem.objects.get(id=blogid)
    item.like += 1
    item.save()
    print(item.like)
    return  HttpResponseRedirect('/single/?bid='+blogid)

def error_500(request):
    return render(request, '500.html')
    
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)