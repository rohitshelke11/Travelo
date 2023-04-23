from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already register')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=pass1, email=email , first_name=first_name, last_name=last_name)
                user.save();
                print("user created")
                return redirect('login')
            
        else:
           print('password not matching....') 
        return redirect('/')    
            
    else:
        return render(request, 'register.html')

def login(request):
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(username=username,password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'invalid credentials')
                    return redirect('login')
            else:
                return render(request, 'login.html')        

def logout(request):
    auth.logout(request)
    return redirect('/')