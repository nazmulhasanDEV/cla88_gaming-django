from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from user.models import User, UserProfile
from adminPanel.models import *
from django.contrib.staticfiles.storage import FileSystemStorage


# admin panel login/register
def ap_login_register(request):

    if request.method == 'POST':
        namesignup             = request.POST.get('namesignup')
        usernamesignup         = request.POST.get('usernamesignup')
        emailsignup            = request.POST.get('emailsignup')
        passwordsignup         = request.POST.get('passwordsignup')
        passwordsignup_confirm = request.POST.get('passwordsignup_confirm')

        if passwordsignup == passwordsignup_confirm:
            if len(passwordsignup) < 6:
                messages.warning(request, "Password must be at least 8 characters!")
                return redirect('apLoginRegister')
            else:
                if len(User.objects.filter(email=emailsignup)) != 0:
                    messages.warning(request, "We already know this email! Try with different one!")
                    return redirect('apLoginRegister')
                elif len(User.objects.filter(username=usernamesignup)) != 0:
                    messages.warning(request, "We already know this username! Try with different one!")
                    return redirect('apLoginRegister')
                else:
                    user = User.objects.create_user(email=emailsignup, username=usernamesignup, password=passwordsignup)
                    user.name = namesignup
                    user.is_admin = True
                    user.is_a_staff = False
                    user.is_active = True
                    user.save()
                    messages.warning(request, "Thanks! Account has been created successfully!")
                    return redirect('apLoginRegister')
        else:
            messages.warning(request, "Password didn't match")
            return redirect('apLoginRegister')

    return render(request, 'back-end/login_register/login-register.html')


# admin panel login
def ap_login(request):

    if request.method == 'POST':
        emailsignup            = request.POST.get('emailsignup')
        username               = request.POST.get('username')
        passwordsignup         = request.POST.get('password')

        try:
            user = User.objects.get(email=emailsignup)
            if user:
                if user.username == username:
                    if user.is_active == True and (user.is_admin == True or user.is_a_staff == True):
                        authenticate_user = authenticate(request, email=emailsignup, password=passwordsignup)
                        if authenticate_user:
                            login(request, authenticate_user)
                            return redirect('apHome')
                        else:
                            messages.success(request, "Wrong Password!")
                            return redirect('apLoginRegister')
                    else:
                        messages.warning(request, "Your account is not activated yet!")
                        return redirect('apLoginRegister')
                else:
                    messages.warning(request, "Username not found! Try again!")
                    return redirect('apLoginRegister')
            else:
                messages.warning(request, "This email is not a registered email! Try again!")
                return redirect('apLoginRegister')
        except:
            messages.warning(request, "This email is not a registered email! Try again!")
            return redirect('apLoginRegister')


    return render(request, 'back-end/login_register/login-register.html')

# admin panel logout
def ap_logout(request):
    logout(request)
    return redirect('apLogin')


# user account/profile
# @login_required(login_url='/apLoginRegister/')
def ap_userProfile(request):

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()
    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'userProfile' : userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/user-account.html', context)

# change user name
# @login_required(login_url='/apLoginRegister/')
def ap_ChangeUserName(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        name     = request.POST.get('new_name')

        if username and name:
            user = get_object_or_404(User, username=username)
            user.name = name
            user.save()
            messages.success(request, "Your name has been updated successfully!")
            return redirect('apUserProfile')
        else:
            messages.error(request, "There is somethng wrong! Please try again")
            return redirect('apUserProfile')

    return render(request, 'back-end/admin_panel/user-account.html')

# change user name
# @login_required(login_url='/apLoginRegister/')
def ap_ChangeUserPassword(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        old_pass    = request.POST.get('old_password')
        new_pass    = request.POST.get('new_password')

        if email and old_pass:
            authenticate_user = authenticate(request, email=email, password=old_pass)
            if authenticate_user is not None:
                user = get_object_or_404(User, email=email)
                user.set_password(new_pass)
                user.save()
                messages.success(request, "Your password has been changed successfully! Please log in here!")
                return redirect('apLogin')
        else:
            messages.error(request, "There is somethng wrong! Please try again")
            return redirect('apUserProfile')

    return render(request, 'back-end/admin_panel/user-account.html')


# change user name
# @login_required(login_url='/apLoginRegister/')
def ap_ChangeUserProfilePic(request):

    if request.method == "POST":
        pic = request.FILES['profile_pic']

        if pic:
            if len(UserProfile.objects.filter(user=request.user)) > 0:
                userProfile = get_object_or_404(UserProfile, user=request.user)
                # deleting previous image
                fs = FileSystemStorage()
                fs.delete(userProfile.profile_pic.name)

                # updating with new image
                userProfile.user = request.user
                userProfile.profile_pic = pic
                userProfile.save()
                messages.success(request, "Your profile picture updated successfully!")
                return redirect('apUserProfile')
            else:
                userProfile = UserProfile(user=request.user, profile_pic=pic)
                userProfile.save()
                messages.success(request, "Your profile picture updated successfully!")
                return redirect('apUserProfile')
        else:
            messages.warning(request, "Something wrong! Try again!")
            return redirect('apUserProfile')

    return render(request, 'back-end/admin_panel/user-account.html')
