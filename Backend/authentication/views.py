from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']

        #if User.objects.filter(username=username):
            #messages.error(request, "username already exists, please try something else")
            #return redirect('home')
        
        # if User.objects.filter(email=email):
           # messages.error(request, "email already exists, please login")
            #return redirect('signin')
        
        #if len(username)>15:
            #messages.error(request, "username is too long, please try something else")
           
        # if pass1 != pass2:
            # messages.error(request, "passwords do not match")
        
        #if not username.isalnum():
            #message.error(request, "username nust be alpha numeric")
            #return redirect('home')
      
        

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        messages.success(request, "account created succesfully")

        return redirect('signin')
    
    
    return render(request, 'authentication/register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
    
        if user is not None:
            login(request, user)
            fname= user.first_name
            return render(request,  'authentication/index.html',{'fname':fname})
        
        else:
            messages.error(request, "incorrect credentials")
            return redirect('home')
    
    return render(request, 'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "logout successful")
    return redirect('home')
