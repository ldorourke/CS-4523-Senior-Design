from django.shortcuts               import render
from django.http                    import HttpResponse
from django.core.mail               import EmailMessage
from django.shortcuts               import redirect, render
from django.template                import loader
from django                         import forms
from seniordesign.models            import CustomUser, UserProfile, UserManager

from django.views                   import View
from django.views.generic           import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.views      import LoginView
from django.contrib.auth            import authenticate, login, logout, get_user
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.db.models               import Q
from django.contrib                 import messages
from django.http                    import HttpResponse, HttpResponseRedirect,HttpRequest

site_hdr = "Senior Design"

def index(request):
    return render(request, 'index.html', {'header': site_hdr})

def dashboard(request):
    return render(request, 'dashboard.html', {'header': site_hdr})

def interests(request):
    return render(request, 'search_interests.html', {'header': site_hdr})

def logout_view(request):
    logout(request)
    return redirect('login')


def isEmailPresent(email):
    return User.objects.filter(email=email).exists()
    
def isUsernamePresent(username):
    return UserProfile.objects.filter(username=username).exists()
    #weird error here, userprofile should be one to one with user

def isPasswordValid(password):
    if len(password) in range(8,15):
        return True
    else:
        return False



def userCreate(request):
    if request.method == 'POST':
        fName           = str(request.POST.get('fName', ''))
        lName           = str(request.POST.get('lName', ''))
        university      = str(request.POST.get('university', ''))
        email           = str(request.POST.get('email', ''))
        username        = str(request.POST.get('username', ''))
        password        = str(request.POST.get('password', ''))
        confirmPassword = str(request.POST.get('confirmPassword', ''))
        '''
        print(fName)
        print(lName)
        print(email)
        print(username)
        '''
        # now for some form validation
        #first check database for existing userid and email since these need to be unique to each user

                    
        if isEmailPresent(email):
            messages.error(request,"This email is already registered to an existing user!")
            

        if isUsernamePresent(username):
            messages.error(request,"This username already belongs to an existing user!")
            


        if not isEmailPresent(email) and not isUsernamePresent(username):
            # this is checking to make sure first name and last name only include letters
            isFNameValid        = fName.isalpha()  
            isLNameValid        = lName.isalpha()
            isUserNameValid     = True if username.isalnum() and len(username) in range(5,12)   else False
            isNyuEmail          = True if "@nyu.edu" in email                                   else False   #Currently only serves NYU
            passwordsMatch      = True if password == confirmPassword                           else False

            if not isFNameValid: messages.error(request,"The First Name Entered is not Valid!")
            
            if not isLNameValid: messages.error(request,"The Last Name Entered is not Valid!")

            if not isUserNameValid: messages.error(request,"Username should only include letters and numbers and be between 5 and 12 characters long!")
            
            if not isNyuEmail: messages.error(request, "Please use the email associated with your university!")
            
            if not passwordsMatch: messages.error(request, "Please make sure that the passwords match!")
            
            elif passwordsMatch: #already confirmed that they match, now checking if it's valid
                isValid = isPasswordValid(password)
                if not isValid:
                    messages.error(request, "Passwords should be between 8 and 15 characters!")

            if isFNameValid and isLNameValid and isUserNameValid and isNyuEmail and passwordsMatch and isPasswordValid(password):
                #create instance of user and save to db
                print("here")
                newUser = User(email=email)
                newUser.set_password(password)
                newUser.save()

                newUserProfile = UserProfile()
                newUserProfile.user = newUser
                newUserProfile.firstName = fName
                newUserProfile.lastName = lName
                newUserProfile.username = username
                newUserProfile.university = university
                newUserProfile.save()
                

                user = authenticate(username = email, password = password)
                login(request, user)
                return HttpResponseRedirect('')
                #Need Redirect to be filled ^^

