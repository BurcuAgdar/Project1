from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

    return render(request,"home.html",{"number":7})
def about(request):
    return render(request,"about.html")
def student(request):
    return render(request,"Student.html")