from django.shortcuts import render
from news.models import Category
from news.models import News
def home(request):
    context ={
        'ac':Category.objects.all(), # SELECT * From category
        'news':News.objects.all()[::-1]
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')