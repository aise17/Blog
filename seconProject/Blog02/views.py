# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from Blog02.models import Category, Post, Comment
import datetime
from Blog02.form import PostForm, CommentForm




list_category = Category.objects.all()
fecha_actual = datetime.datetime.now()



# Create your views here.
def welcome(request):
	
	return render(request, 'welcome.html', {'list_category': list_category,'fecha_actual': fecha_actual})


def post(request):
	
	list_post = Post.objects.all()

	return render(request, 'post_filter.html',{'list_post': list_post, 'list_category': list_category,'fecha_actual': fecha_actual})


def posts_by_filter(request, final):
	try: 
		final = str(final) 
	except ValueError: 
		raise Http404()  
	#list_post = Post.objects.filter(category__id = final)

	category = Category.objects.get( id = final)#selecionamos el post que nos da offset con el que estan relacionados los comentarios

	list_post = category.post_set.all()#del post sellecionado cojemos todos sus comentarios

	return render(request, "post_filter.html",{'list_post':list_post, 'list_category':list_category,'fecha_actual': fecha_actual})


def comment_by_post(request, final):
	try: 
		final = str(final) 
	except ValueError: 
		raise Http404()
	#list_comment = Comment.objects.filter(post__id = final)

	post = Post.objects.get(id = final) #selecionamos el post que nos da offset con el que estan relacionados los comentarios

	list_comment = post.comment_set.all()	#del post sellecionado cojemos todos sus comentarios

	return render(request, "comment_filter.html",{'list_comment':list_comment, 'post': post, 'list_category':list_category,'fecha_actual': fecha_actual})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form': form, 'list_category':list_category,'fecha_actual': fecha_actual})


def comment_new(request, final):
	try: 
		final = int(final) 
	except ValueError: 
		raise Http404()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			cooment.post = final
			comment.save()
			
	else:
		form = CommentForm()
	return render(request, 'comment_edit.html', {'form': form, 'list_category':list_category,'fecha_actual': fecha_actual})