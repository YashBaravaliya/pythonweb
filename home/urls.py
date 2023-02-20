from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homePage,name='home'),
    path('cheetsheet/',views.cheetSheet,name='cheetsheet'),
    path('project/',views.project,name='project'),
    path('contactus/',views.contectus,name='contactus'),
    path('aboutMe/',views.aboutMe,name='aboutMe'),
    path('search/',views.search,name='search'),
    path('cheetsheet/<str:slug>/',views.blog,name='blog'),
    path('<str:subject>/<str:slug>/',views.course,name='blog'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
