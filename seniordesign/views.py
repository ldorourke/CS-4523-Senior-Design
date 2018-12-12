from django.shortcuts               import render, HttpResponseRedirect
from django.http                    import HttpResponse
from django.core.mail               import EmailMessage
from django.shortcuts               import redirect, render
from django.template                import loader
from django                         import forms
from seniordesign.models            import CustomUser, UserProfile, UserManager, uConnectUser
from seniordesign.forms             import createEventForm, UserForm

from django.views                   import View
from django.views.generic           import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.views      import LoginView
from django.contrib.auth            import authenticate, login, logout, get_user
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.db.models               import Q
from django.contrib                 import messages
from django.http                    import HttpResponse, HttpResponseRedirect,HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models     import User
from django.forms.models            import inlineformset_factory
from django.core.exceptions         import PermissionDenied
import os

site_hdr = "uConnect"



class createEventView(TemplateView):
    def __init__(self):
        self.template_name= 'createEvent.html'
    
    def get(self, request):
        form = createEventForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = createEventForm(request.POST)
        if form.is_valid():
            form.save()
            #text = form.cleaned_data['POST']
            form = createEventForm()
            return redirect('seniordesign:viewEvent')

        args = {'form':form, 'text': text}
        return render(request, self.template_name, args)



def index(request):
    return render(request, 'index.html', {'header': site_hdr})

def dashboard(request):
    return render(request, 'dashboard.html', {'header': site_hdr})

def myEvents(request):
    return render(request, 'myEvents.html', {'header': site_hdr})

def explore(request):
    return render(request, 'explore.html', {'header': site_hdr})

def viewEvent(request):
    return render(request, 'viewEvent.html', {'header': site_hdr})

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

@login_required        
def viewProfile(request):
    return render(request, 'account/viewProfile.html', {'header': site_hdr})

@login_required
def editUser(request):
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    user_form = UserForm(instance=request.user)
 
    ProfileInlineFormset = inlineformset_factory(User, uConnectUser, fields=('username', 'university', 'year_in_school'))
    formset = ProfileInlineFormset(instance=request.user)
 
    if request.user.is_authenticated:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=request.user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=request.user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/viewProfile/')

            else:
                print("HI")
 
        return render(request, "account/updateProfile.html", {
            "noodle": request.user,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
 


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

