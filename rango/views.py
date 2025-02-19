from django.shortcuts import render
from django.http import HttpResponse
#Import the Category model
from rango.models import Category
#Chapter 6: import Page model
from rango.models import Page

def index(request):
  #Query database for list off ALL categories currently stored.
  #ORder categories by number of likes in descending order
  #Retrieve op 5 only -- or all if less then 5
  #Place list in context_dict dictionary (boldmessage) that will be passed to template engine
  
  #order_by('-likes'): order by number of likes in descending order (prefix -)
  #[:5] index up to 5 items, using list operator []
  category_list = Category.objects.order_by('-likes')[:5]
  pages_list = Page.objects.order_by('-views')[:5]

  context_dict = {}
  context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
  context_dict['categories'] = category_list
  context_dict['pages'] = pages_list

  return render(request, 'rango/index.html', context = context_dict)

def about(request):
  context_dict = {'boldmessage': 'This tutorial has been put together by Yongwoo'}
  return render(request, 'rango/about.html', context = context_dict)

def show_category(request, category_name_slug):
  #create context dict which we can pass to the template rendering engine
  context_dict = {}

  try:
    #if we can't find category name slug with given name, .get() method raises DoesNotExist Exception
    category = Category.objects.get(slug=category_name_slug)

    #Retrieve all associated pates. The filter() will return list of page objects OR and empty list.
    pages = Page.objects.filter(category=category)

    #Add result list to the template context under name pages
    context_dict['pages'] = pages

    #Also add category object from database to context dictionary. Use in template to verify that category exists.
    context_dict['category'] = category

  except Category.DoesNotExist:
    #Don't do anything, template will display "no category" message
    context_dict['category'] = None
    context_dict['pages'] = None
  
  return render(request, 'rango/category.html', context=context_dict)