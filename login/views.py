from django.http import Http404, HttpResponseRedirect
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Notif, Fee_pay, Compliant, Comp_match, Paying, Defuser
from django.db import connection
from datetime import datetime

app_name = 'login'

#admin functions here


def index(request):
    query1 = "SELECT added_date,expiry_date,posted_by_id_id,data,head,user_name FROM login_notif,login_defuser WHERE expiry_date >= '" + datetime.now().strftime("%Y-%m-%d") + "' AND user_id=posted_by_id_id"
    cursor2 = connection.cursor()
    cursor2.execute(query1)
    row2 = cursor2.fetchall()
    return render(request, 'login/login.html', {'data':row2})

def adminlog(request):
    return render(request, 'login/admin.html')

def adminlogin(request):
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
    return HttpResponseRedirect('/log')

def addnoti(request):
    if (request.session['username']):
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
    if (count == 1):
        return render(request, 'login/addnoti.html', {'name': request.session.get("username")})
    else:
        return render(request, 'login/admin.html')

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
        cursor = connection.cursor()
        query = "SELECT name,father_name,mother_name,pass_word,year,sem,branch,admission_number,ten_res,puc_res,reg_no,phone,email,fee,rank,Temp_address,per_address,studying_year,gender FROM login_user WHERE reg_no='" + str(request.POST.get("search")) + "'"
        cursor.execute(query)
        row = cursor.fetchall()
        count = int(len(row))
        if (count == 1):
            return render(request, 'login/updatestd.html', {'name': name, 'row' : row, 'namea' : row[0][0],'pass' :  row[0][1],'father' :  row[0][2],'mother' :  row[0][3],'year' :  row[0][4],'sem' :  row[0][5],'branch' : row[0][6],'add_no' : row[0][7],'ten_res' : row[0][8],'puc_res' : row[0][9],'regno' : row[0][10],'phone' : row[0][11],'email' : row[0][12],'fee' : row[0][13],'rank' : row[0][14],'t_add' : row[0][15],'p_add' : row[0][16],'a_year' : row[0][17],'gender' : row[0][18]})
        else:
            return HttpResponseRedirect('/log/admin/addstd')
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
        newuser.admission_number = str(request.POST.get('add_no'))
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
        if (newuser.save()):
            return render(request, 'login/addstd.html', {'name': name})
        else:
            return render(request, 'login/addstd.html', {'name': name, 'error': "Fill all details and submit"})
    else:
        return render(request, 'login/admin.html')

def addnotification(request):
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
        cursor1 = connection.cursor()
        newnoti = Notif()
        myDate = datetime.now()
        newnoti.added_date = myDate.strftime("%Y-%m-%d")
        newnoti.expiry_date = str(request.POST.get('ex_date'))
        newnoti.posted_by_id = Defuser.objects.only('user_id').get(user_id=row[0][2])
        newnoti.head = str(request.POST.get('subject'))
        newnoti.data =str(request.POST.get('noti'))
        newnoti.save()
        return render(request, 'login/addnoti.html', {'error_message':"", 'name': request.session.get("username")})
    else:
        return render(request, 'login/admin.html')

def fee(request):
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
        return render(request, 'login/fee.html', {'name': request.session.get("username")})
    else:
        return render(request, 'login/admin.html')

def feefetch(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        query1 = "SELECT * FROM login_fee_pay WHERE trans_id in (SELECT pay_id_id FROM login_paying WHERE std_id_id='" + str(request.POST.get('search')) + "')"
        cursor2 = connection.cursor()
        cursor2.execute(query1)
        row2 = cursor2.fetchall()
        return render(request, 'login/feefetch.html', {'name': request.session.get("username"), 'data':row2})
    else:
        return render(request, 'login/admin.html')


def feefetchsem(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        query1 = "SELECT * FROM login_fee_pay,login_user,login_paying WHERE trans_id in (SELECT pay_id_id FROM login_paying WHERE std_id_id in (SELECT reg_no FROM login_user WHERE sem=" + str(request.POST.get('search')) + " )) and login_paying.pay_id_id=login_fee_pay.trans_id and login_paying.std_id_id=login_user.reg_no"
        cursor2 = connection.cursor()
        cursor2.execute(query1)
        row2 = cursor2.fetchall()
        return render(request, 'login/feefetchsem.html', {'name': request.session.get("username"), 'data':row2})
    else:
        return render(request, 'login/admin.html')


def logout(request):
    del request.session['username']
    del request.session['passa']
    return render(request, 'login/admin.html')


def viewcomp(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        query1 = "SELECT match_id_id,regno_id,add_date,status,explain,about,sub,comp_id FROM login_compliant,login_comp_match,login_user WHERE reg_no=regno_id AND match_id_id=comp_id AND status!='Solved'"
        cursor2 = connection.cursor()
        cursor2.execute(query1)
        row2 = cursor2.fetchall()
        return render(request, 'login/newcomp.html', {'name': request.session.get("username"), 'data':row2})
    else:
        return render(request, 'login/admin.html')

def updatecompsol(request):
    if (request.session['username']):
        password = request.session['passa']
        name = request.session['username']
    else:
        return render(request, 'login/admin.html')
    cursor = connection.cursor()
    query = "SELECT * FROM login_defuser WHERE user_name='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        query1 = "SELECT match_id_id FROM login_compliant,login_comp_match,login_user WHERE reg_no=regno_id AND match_id_id=comp_id AND status!='Solved'"
        cursor2 = connection.cursor()
        cursor2.execute(query1)
        row2 = cursor2.fetchall()
        forw = ""
        for x in row2:
            status = str(request.POST.get(str(x[0])))
            query1 = "UPDATE login_compliant SET status='" + status + "' WHERE comp_id=" + str(x[0]) + " "
            cursor2 = connection.cursor()
            cursor2.execute(query1)
        return HttpResponseRedirect('http://127.0.0.1:8000/log/admin/viewcomp')
    else:
        return render(request, 'login/admin.html')


#student functions here

def stdlogin(request):
    name = str(request.POST.get('username'))
    password = str(request.POST.get('passa'))
    cursor = connection.cursor()
    query = "SELECT * FROM login_user WHERE reg_no='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        request.session['name_std'] = row[0][0]
        request.session['user_std'] = name
        request.session['pass_std'] = password
        return render(request, 'login/std_logged.html', {'name': row[0][0], 'fee':row[0][12]})
    else:
        return HttpResponseRedirect("/log")


def stdlogout(request):
    del request.session['name_std']
    del request.session['user_std']
    del request.session['pass_std']
    return HttpResponseRedirect('/log/')

def addcomp(request):
    name = request.session['user_std']
    password = request.session['pass_std']
    cursor = connection.cursor()
    query = "SELECT * FROM login_user WHERE reg_no='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        return render(request, 'login/comp.html', {'name': row[0][0], 'fee':row[0][12]})
    else:
        return HttpResponseRedirect("/log")

def addstdcomp(request):
    name = request.session['user_std']
    password = request.session['pass_std']
    cursor = connection.cursor()
    query = "SELECT * FROM login_user WHERE reg_no='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        newcomp =Compliant()
        newcomp.about = str(request.POST.get('about'))
        newcomp.sub = str(request.POST.get('subject'))
        newcomp.explain = str(request.POST.get('data'))
        newcomp.add_date = datetime.now().strftime("%Y-%m-%d")
        newcomp.status = "Not checked yet"
        newcomp.save()
        newreg = Comp_match()
        newreg.match_id = Compliant.objects.only('comp_id').get(comp_id=newcomp.comp_id)
        newreg.regno = User.objects.only('reg_no').get(reg_no=row[0][9])
        newreg.save()
        return render(request, 'login/comp.html', {'name': row[0][0], 'fee':row[0][12]})
    else:
        return HttpResponseRedirect("/log")

def dopayment(request):
    name = request.session['user_std']
    password = request.session['pass_std']
    cursor = connection.cursor()
    query = "SELECT * FROM login_user WHERE reg_no='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        if 'transid' in request.session:
            var=request.session['transid']
            del request.session['transid']
            var1=request.session['amt1']
            del request.session['amt1']
            return render(request, 'login/payment.html', {'name': row[0][0], 'fee':row[0][12], 'trans': var, 'amt11':var1})
        else:
           return render(request, 'login/payment.html', {'name': row[0][0], 'fee': row[0][12]})
    else:
        return HttpResponseRedirect("/log")

def donepayment(request):
    name = request.session['user_std']
    password = request.session['pass_std']
    cursor = connection.cursor()
    query = "SELECT * FROM login_user WHERE reg_no='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        newfee = Fee_pay()
        newfee.card_no = str(request.POST.get('card'))
        newfee.fee_paid = str(request.POST.get('amt'))
        newfee.paid_date = datetime.now().strftime("%Y-%m-%d")
        newfee.save()
        var = newfee.trans_id
        newfeed = Paying()
        newfeed.pay_id = Fee_pay.objects.only('trans_id').get(trans_id=var)
        newfeed.std_id = User.objects.only('reg_no').get(reg_no=row[0][9])
        newfeed.save()
        query = "UPDATE login_user SET fee=" + str(int(row[0][12])-int(newfee.fee_paid)) + " WHERE reg_no='" + row[0][9]+ "'"
        cursor1 = connection.cursor()
        cursor1.execute(query)
        request.session['amt1']=str(request.POST.get('amt'))
        request.session['transid']=var;
        return render(request, 'login/paying.html', {'var':row[0][9], 'fee':row[0][12]})
    else:
        return HttpResponseRedirect("/log")

def stdcomp(request):
    name = request.session['user_std']
    password = request.session['pass_std']
    cursor = connection.cursor()
    query = "SELECT * FROM login_user WHERE reg_no='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        query1 = "SELECT match_id_id,regno_id,add_date,status,explain,about,sub,comp_id FROM login_compliant,login_comp_match,login_user WHERE reg_no='"+name+"' AND match_id_id=comp_id AND status!='Solved'"
        cursor2 = connection.cursor()
        cursor2.execute(query1)
        row2 = cursor2.fetchall()
        return render(request, 'login/complain.html', {'name': row[0][0],'data':row2, 'fee':row[0][12]})
    else:
        return HttpResponseRedirect("/log")

def stdchange(request):
    name = request.session['user_std']
    password = request.session['pass_std']
    cursor = connection.cursor()
    query = "SELECT * FROM login_user WHERE reg_no='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        return render(request, 'login/change.html', {'name': row[0][0], 'fee': row[0][12]})
    else:
        return HttpResponseRedirect("/log")

def changedone(request):
    name = request.session['user_std']
    password = request.session['pass_std']
    cursor = connection.cursor()
    query = "SELECT * FROM login_user WHERE reg_no='" + name + "' AND pass_word='" + password + "'"
    cursor.execute(query)
    row = cursor.fetchall()
    count = int(len(row))
    if (count == 1):
        cur_pass = str(request.POST.get('current_password'))
        new_pass = str(request.POST.get('new_password'))
        con_pass = str(request.POST.get('confirm_password'))
        if (password == cur_pass):
            if new_pass == con_pass:
                query1 = "UPDATE login_user SET pass_word='" + new_pass + "' WHERE reg_no='" + name + "'"
                cursor1 = connection.cursor()
                cursor1.execute(query1)
                return render(request, 'login/change.html', {'name': row[0][0], 'fee': row[0][12], 'error1': "successfully changed"})
            else:
                return render(request, 'login/change.html', {'name': row[0][0], 'fee': row[0][12], 'error1': "new Passwords mismatch"})
        else:
            return render(request, 'login/change.html', {'name': row[0][0], 'fee': row[0][12], 'error1': "Current password is mismatched"})
    else:
        return HttpResponseRedirect("/log")