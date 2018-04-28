from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage
from .models import Category, Good

def index(request):
  cats = Category.objects.all()
  return render(request, "good/index.html", {"cats": cats})
  
  
def category(request, cat_id=1):
  try:
    cat = Category.objects.get(pk=cat_id)
  except Category.DoesNotExist:
    raise Http404
  goods = Good.objects.filter(category=cat).order_by("name")
  
  return render(request, "good/category.html", {"cat": cat, "goods": goods})

def good(request, good_id):
  try:
    good = Good.objects.get(pk=good_id)
  except Good.DoesNotExist:
    raise Http404
 
  return render(request, "good/good.html", {"good": good})

def goods(request):  
  try:
    page_num = request.GET["page"]
  except KeyError:
    page_num = 1
  paginator = Paginator(Good.objects.all().order_by("name"), 5)
  try:
    goods = paginator.page(page_num)
  except InvalidPage:
    raise Http404
  return render(request, "good/goods.html", {"goods": goods})