from django.shortcuts import render , redirect
# for creating django user 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout


MESSAGE_TAGS = {
    messages.ERROR:'danger',
    messages.SUCCESS:'success',
}


# Create your views here.
def index(request):
    alluser = User.objects.all()
   

    user = False
    if  request.user.is_authenticated:
        user = True
        context = {"user":user, "alluser":alluser}
        return render(request , "index.html" , context)
    else:
        context ={"user":user}
        return render(request , "index.html" , context)
    
    
    # params = {"user":user}
    # return render(request , "index.html")

def singupUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "you have been successfully singup")
        print(f"user is create username: {username}")
        return redirect("/login")
    else:
        return redirect("/user")


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully login")
            return redirect("/user/")


    return render(request , "login.html")



def logoutUser(request):
    logout(request)
    messages.success(request, "You have been successfully logout")
    return redirect("/user")
