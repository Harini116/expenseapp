from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'mywebsite/about.html')
def indexexp(request):
    return render(request,'mywebsite/expense.html')
def indexmyexp(request):
    return render(request,'mywebsite/myexpense.html')