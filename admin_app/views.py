from django.shortcuts import render

def dashboard(request):
    return render(request, 'admin_app/dashboard.html')
