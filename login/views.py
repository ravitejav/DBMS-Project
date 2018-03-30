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
    if(request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        name = str(request.POST.get('username'))
        password = str(request.POST.get('passa'))
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    row2 = list(row)
    count = int(len(row))
    if(count==1):
        request.session['username'] = name
        request.session['passa'] = password
        return render(request, 'login/admin_logged.html', {'name': request.session.get("username")})
    else:
        return render(request, 'login/admin.html')

def studentlog(request):
    return render(request, 'login/student.html')

def addstd(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    row2 = list(row)
    count = int(len(row))
    if (count == 1):
        return render(request, 'login/addstd.html', {'name':name})
    else:
        return render(request, 'login/admin.html')

def updatestd(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    row2 = list(row)
    count = int(len(row))
    if (count == 1):
        return render(request, 'login/upstd.html', {'name':name})
    else:
        return render(request, 'login/admin.html')

def upsearch(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    row2 = list(row)
    count = int(len(row))
    if (count == 1):
        newmap = {
                    'name' : 'name',
                    'father' : 'father_name',
                    'mother' : 'mother_name',
                    'pass' : 'pass_word',
                    'year' : 'year',
                    'sem' : 'sem',
                    'branch' : 'branch',
                    'add_no' : 'admission_number',
                    'ten_res' : 'ten_res',
                    'puc_res' : 'puc_res',
                    'regno' : 'reg_no',
                    'phone' : 'phone',
                    'email' : 'email',
                    'fee' : 'fee',
                    'rank' : 'rank',
                    't_add' : 'Temp_address',
                    'p_add' : 'per_address',
                    'a_year' : 'studying_year',
                    'gender' : 'gender',
        }
        cursor = connection.cursor()
        query = "SELECT name,father_name,mother_name,pass_word,year,sem,branch,admission_number,ten_res,puc_res,reg_no,phone,email,fee,rank,Temp_address,per_address,studying_year,gender FROM login_user WHERE reg_no='" + str(request.POST.get("search")) + "'"
        cursor.execute(query)
        row = cursor.fetchall()
        return render(request, 'login/updatestd.html', {'name': name, 'row' : row, 'namea' : row[0][0],'pass' :  row[0][1],'father' :  row[0][2],'mother' :  row[0][3],'year' :  row[0][4],'sem' :  row[0][5],'branch' : row[0][6],'add_no' : row[0][7],'ten_res' : row[0][8],'puc_res' : row[0][9],'regno' : row[0][10],'phone' : row[0][11],'email' : row[0][12],'fee' : row[0][13],'rank' : row[0][14],'t_add' : row[0][15],'p_add' : row[0][16],'a_year' : row[0][17],'gender' : row[0][18]})
    else:
        return render(request, 'login/admin.html')


def addstddb(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    row2 = list(row)
    count = int(len(row))
    if (count == 1):
        newuser = User()
        newuser.name = str(request.POST.get('first_name'))
        newuser.name = newuser.name + str(request.POST.get('second_name'))
        newuser.father_name = str(request.POST.get('father_name'))
        newuser.mother_name = str(request.POST.get('mother_name'))
        newuser.year = int(request.POST.get('year'))
        newuser.sem = int(request.POST.get('sem'))
        newuser.branch = str(request.POST.get('branch'))
        newuser.addmission_number = str(request.POST.get('add_no'))
        newuser.ten_res = float(request.POST.get('ten_res'))
        newuser.puc_res = float(request.POST.get('puc_res'))
        newuser.reg_no = str(request.POST.get('regno'))
        newuser.phone = str(request.POST.get('phone'))
        newuser.email = str(request.POST.get('email'))
        newuser.fee = int(request.POST.get('fee'))
        newuser.rank = int(request.POST.get('rank'))
        newuser.gender = str(request.POST.get('gender'))
        newuser.Temp_address = str(request.POST.get('temp_add'))
        newuser.per_address = str(request.POST.get('per_add'))
        newuser.studying_year = str(request.POST.get('a_year'))
        newuser.pass_word = str(request.POST.get('passa'))
        if(newuser.save()):
            return render(request, 'login/addstd.html', {'name': name})
        else:
            return render(request, 'login/addstd.html', {'name':name, 'error':"Fill all details and submit"})
    else:
        return render(request, 'login/admin.html')

def updatestddone(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    row2 = list(row)
    count = int(len(row))
    if (count == 1):
        newuser= User.objects.get(reg_no=str(request.POST.get('regno')))
        newuser.name = str(request.POST.get('first_name'))
        newuser.name = newuser.name + str(request.POST.get('second_name'))
        newuser.father_name = str(request.POST.get('father_name'))
        newuser.mother_name = str(request.POST.get('mother_name'))
        newuser.year = int(request.POST.get('year'))
        newuser.sem = int(request.POST.get('sem'))
        newuser.branch = str(request.POST.get('branch'))
        newuser.addmission_number = str(request.POST.get('add_no'))
        newuser.ten_res = float(request.POST.get('ten_res'))
        newuser.puc_res = float(request.POST.get('puc_res'))
        newuser.reg_no = str(request.POST.get('regno'))
        newuser.phone = str(request.POST.get('phone'))
        newuser.email = str(request.POST.get('email'))
        newuser.fee = int(request.POST.get('fee'))
        newuser.rank = int(request.POST.get('rank'))
        newuser.gender = str(request.POST.get('gender'))
        newuser.Temp_address = str(request.POST.get('temp_add'))
        newuser.per_address = str(request.POST.get('per_add'))
        newuser.studying_year = str(request.POST.get('a_year'))
        newuser.pass_word = str(request.POST.get('passa'))
        if (newuser.save()):
            return render(request, 'login/addstd.html', {'name': name})
        else:
            return render(request, 'login/addstd.html', {'name': name, 'error': "Fill all details and submit"})
    else:
        return render(request, 'login/admin.html')