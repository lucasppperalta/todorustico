from django.shortcuts import render 

def Index(request):
    return render(request, "index.html")
def about(request):
    return render(request, 'proximamente.html')
def causes(request):
    return render(request, 'causes.html')
def vista(request):
    return render(request, 'vistadetallada.html')
def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')