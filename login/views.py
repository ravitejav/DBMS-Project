from django.http import Http404
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Notif, Fee_pay, Compliant, Comp_match, Paying, Defuser
from django.db import connection


app_name = 'login'

def index(request):
    return render(request, 'login/login.html')

def adminlog(request):
    return render(request, 'login/admin.html')

def adminlogin(request):
    name = str(request.POST.get('username'))
    password = str(request.POST.get('passa'))
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if(count==1):
        return HttpResponse("<h1>Admin logged in </h1>")
    else:
        return HttpResponse("<h1>Admin not logged in</h1>")

def studentlog(request):
    return render(request, 'login/student.html')