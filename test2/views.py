from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import smtplib
from test2.models import *
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.db.models import Q
import re
import datetime
from datetime import date

from datetime import datetime
from datetime import timedelta
import os

# Create your views here.

def load_register(request):
    try:
        return render(request,'register.html')
    except Exception as e:
        print(e)

#To create user account
def Register(request):
    try:
        if request.method == "POST":
            name= request.POST['fname']
            print(name)
            email= request.POST['email']
            mobile= request.POST['mobile']
            password= request.POST['password']
            cpassword= request.POST['cpassword']
            sel_type  = request.POST['seltype']
            if password != cpassword:
                messages.success(request, 'Password Mismatch')
                
            elif name == '' or email == '' or mobile == '' or password == '' or cpassword == '' or  sel_type == '' :
                messages.success(request, 'All Fileds Are Mandatory')
                
            elif len(mobile) != 10:
                messages.success(request, 'Mobile Number IS  Not Valid')
               
            elif not email_validation(email):
                messages.success(request, 'Email IS Not Valid')
            else:
                
                check_exist =Register_User.objects.filter(email=email).exists()
                if check_exist == False:

                    user = Register_User(name=name,email=email,mobile=mobile,password=password,selected_type=sel_type,role='users')
                    user.save()
                    if user.id >0:
                            current_site = get_current_site(request)
                            email_subject = 'Activate Your Account'
                            message = render_to_string('activate_account.html', {
                                'user': user,
                                'domain': current_site.domain,
                                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                'token': account_activation_token.make_token(user),
                            })
                            to_email = user.email
                            email = EmailMessage(email_subject, message, to=[to_email])
                            email.send()
                          
                            messages.success(request, 'We have sent you an email, please confirm'
                                                    ' your email address to complete registration')
                else:
                    messages.success(request, 'Email id already exist')
        return JsonResponse({'data':'success'})
    except Exception as e:
        print(e)



def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = Register_User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        Register_User(request, user)
        # return render(request,'login.html')
        return HttpResponseRedirect('/login')
    # return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')

def login(request):
    try:
         
        return render(request, "login.html")
        
    except Exception as e:
        print(e)


# EMAIL VALIDATION FUNCTION
def email_validation(email):
    """
    param:email
    return true or false
    """
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False

# TO SAVE ACTIVITIES TO DATABASE
def save_datas(request):
    try:
        if request.method == "POST":
            activity= request.POST['activity']
            participants= request.POST['participants']
            sel_type= request.POST['type']
            price= request.POST['price']
            accessibility= request.POST['accessibility']
            link= request.POST['link']
            email= request.POST['email']
            created_date=datetime.today().date()
            # if  Activities.objects.filter(Q(activity=activity) & Q(created_by=email)).count() == 0:
            
            Activities.objects.create(created_by=email,activity=activity,created_date=created_date,participants=participants,sel_type=sel_type,price=price,accessibility=accessibility,link=link)
            return JsonResponse({'data':'created'})
            # return JsonResponse({'data':'activity exist'})

        
    except Exception as e:
        print(e)

# TO LOAD ACTIVITY VIEW PAGE    
def Load_Responsepage(request):
    try:
        if request.method == "POST":
           
            email= request.POST['email']
            password= request.POST['password']
            activities_all=Activities.objects.all().distinct()
            check_exist =Register_User.objects.filter(email=email).exists()
            if check_exist == False:
                messages.success(request, 'User not Exist')
                return HttpResponseRedirect('/login')
            login_obj = Register_User.objects.filter(email=email).values('pk','email','password','role')
            request.session['user_id']=login_obj[0]['pk']
            if login_obj[0]['password'] == password:
                activity = Activities.objects.filter(created_by=email).values('pk','activity','participants','sel_type','price','accessibility','link',)
                print(activity)
                if login_obj[0]['role'] == 'admin':
                    return render(request,'adminpage.html',{'activities':activities_all})
                return render(request,'response.html',{'activities':activity,'email':email})
            messages.success(request, 'Wrong password')
           
        return redirect('/login')
    except Exception as e:
        print(e)

# TO CHECK ADDING OF 2 ACTIVITY IS POSSIBLE OR NOT
def check_data_fetch(request):
    try:
        if request.method == "POST":
            email= request.POST['email']
            print(email)
            current_date=datetime.today().date()
            sel_type=Register_User.objects.filter(email=email).values('selected_type')
            sel_type=sel_type[0]['selected_type']
            print(sel_type)
            activity_per_day_count=Activities.objects.filter(Q(created_by=email) & Q(created_date=current_date)).values('pk').count()
            print(activity_per_day_count)
            if activity_per_day_count <= 1:
                return JsonResponse({'data':'permitted','type':sel_type})
            else:
                return JsonResponse({'data': "You crossed daily activity adding limit"})
        return JsonResponse({'data':'creted'})

        
    except Exception as e:
        print(e)

# TO UPDATE ACTIVITIES
def Update_data(request):
    try:
        if request.method == "POST":
            activity= request.POST['activity']
            participants= request.POST['participants']
            sel_type= request.POST['type']
            price= request.POST['price']
            accessibility= request.POST['accessibility']
            link= request.POST['link']
            row_id= request.POST['row_id']
            Activities.objects.filter(pk=row_id).update(activity=activity,participants=participants,sel_type=sel_type,price=price,accessibility=accessibility,link=link) 
        return JsonResponse({'data':'updated'})
    
    except Exception as e:
        print(e)

# DELETE DATA FROM ADMIN PAGE
def Delete_data(request):
    try:
        if request.method == "POST":
            row_id= request.POST['row_id']
            Activities.objects.filter(pk=row_id).delete() 
        return JsonResponse({'data':'deleted'})
    
    except Exception as e:
        print(e)


