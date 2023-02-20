from django.shortcuts import render,HttpResponse
from django.contrib import messages
from home.models import subject,chapter,cheetsheet,Contact

# Create your views here.

def homePage(request):
    Subject = subject.objects.all()
    Chapter = chapter.objects.all()
    context={'Subject':Subject,'Chapter':Chapter}
    return render(request,'home/home.html',context)

def course(request,subject,slug):
    # add subject and chhapter
    # Subject = subject.objects.all()
    Chapter = chapter.objects.all()
    post = chapter.objects.get(slug=slug)

    context = {'post':post,'Chapter':Chapter}
    return render(request,'home/blog.html',context)

def cheetSheet(request):
    CheetSheet = cheetsheet.objects.all()
    context = {'CheetSheet':CheetSheet}
    return render(request,'home/cheetsheet.html',context)

def project(request):
    return render(request,'home/project.html')    

def blog(request,slug):
    
    post = cheetsheet.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'home/blog.html',context)

def aboutMe(request):
    return render(request,'home/aboutme.html')


def contectus(request):
    # messages.success(request,'welcome to contact')
    if request.method=='POST':
        email = request.POST['email']
        name  = request.POST['name']
        content  = request.POST['suggestion']
        # print(name,email)

        if len(name)<2 or len(email)<2 or len(content)<3:
            messages.error(request,'enter valid info')
        else:
            contact = Contact(name=name,email=email,content=content)
            contact.save()
            messages.success(request,'successfull')
    # print("i am working\n\n\nok")
    return render(request,'home/contactus.html')

def search(request):
    query = request.GET['query']
    searchPost = subject.objects.filter(course__contains=query)
    searchTopic = chapter.objects.filter(title__contains=query )
    cheet = cheetsheet.objects.filter(Subject__contains=query)
    Chapter = chapter.objects.all()
    context = {'searchPost':searchPost,'Chapter':Chapter,'query':query,'searchTopic':searchTopic,'cheetS':cheet}
    return render(request,'home/search.html',context)

