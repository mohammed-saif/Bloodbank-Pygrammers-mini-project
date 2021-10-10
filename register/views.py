
from register.models import Doner
from django.http import response,JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
persons=[]

def login(request):
    if 'username' in request.session:
        return redirect ('display')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
           
            request.session['username'] = username
            
            return JsonResponse(
                {'success':True},
                safe=False
            )

        else:
            
            return JsonResponse(
                {'success':False},
                safe=False
            )
    else:
        return render(request,'login.html')
    

def signup(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                
                return JsonResponse(
                    {'success':'username'},
                    safe=False
                )
            elif User.objects.filter(email=email).exists():
                return JsonResponse(
                    {'success':'email'},
                    safe=False
                )
            else:
                user = User.objects.create_user(username=username,password=pass1,email=email)
                user.save();
                print('user created')
                return JsonResponse(
                    {'success':'go'},
                    safe=False
                )
        else:
            messages.info(request,'password not matching')
            return redirect('signup')
        
    else:
        return render(request,'signup.html')



def add_donor(request):
    
    
        if request.method=='POST':
            name=request.POST['name']
            age=request.POST['age']
            blood=request.POST['blood']
            phno=request.POST['phno']

            doner=Doner.objects.create(name=name,age=age,bloodgroup=blood,phno=phno)
            doner.save();

            
            persons=Doner.objects.all()
            return render(request,'display.html',{'persons':persons})
        
        else:
            return render(request,'index.html')

    


def display(request):
    if 'username' in request.session:
        persons=Doner.objects.all()
        return render(request,'display.html',{'persons':persons})
    
    else:
        return redirect('login')


def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')