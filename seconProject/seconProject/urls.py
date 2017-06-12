"""seconProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Blog02.views import welcome, post, posts_by_filter, comment_by_post, post_new, comment_new
from Blog02 import views

urlpatterns = [
	url(r'^admin/', admin.site.urls,),
	url(r'^$', welcome),
	url(r'^post/', post),
	url(r'^post_filter/(\d{1,2})/$', posts_by_filter),        
	url(r'^comment/(\d{1,2})/$', comment_by_post),
	url(r'^newPost/$', post_new),
	url(r'^newComment/(\d{1,2})/$', comment_new),
	
]
