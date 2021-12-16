from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import User, UserProfile
from adminPanel.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import uuid
import re



# admin panel index
@login_required(login_url='/ap/login/register')
def ap_index(request):
    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context = {
        'userProfile': userProfile,
        'site_logo' : site_logo,
    }

    return render(request, 'back-end/admin_panel/index.html', context)

# admin panel home
@login_required(login_url='/ap/login/register')
def ap_home(request):
    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    user_list = User.objects.all()

    context = {
        'user_list' : user_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }


    return render(request, 'back-end/admin_panel/home.html', context)


# remove user
@login_required(login_url='/ap/login/register')
def ap_removeUser(request, pk):

    try:
        user = User.objects.get(pk=pk)
        user.delete()
        messages.success(request, "Successfully reoved user!")
        return redirect('apHome')
    except:
        messages.warning(request, "Can't be removed user! Try again!")
        return redirect('apHome')

    return redirect('apHome')


# admin panel edit breaking news
@login_required(login_url='/ap/login/register')
def ap_addSiteLogo(request):

    if request.method == 'POST':

        logo = request.FILES['upload_logo']

        list_of_logo_extension = str(logo).split('.')
        allowed_logo_extensions = ['png', 'jpg', 'jpeg', 'webp']

        if list_of_logo_extension[len(list_of_logo_extension)-1] in allowed_logo_extensions:
            site_logo_model = SiteLogo(logo=logo)
            site_logo_model.save()
            messages.success(request, "Successfully uploaded!")
            return redirect('apAddSiteLogo')
        else:
            messages.warning(request, "Can't be uploaded logo! Please tyr again!")
            return redirect('apAddSiteLogo')

    # grab all logos
    logo_list = SiteLogo.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()
    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'logo_list': logo_list,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add-logo.html', context)


# admin panel delete breaking news
@login_required(login_url='/ap/login/register')
def ap_delSiteLogo(request, logo_id):

    try:
        logo_by_its_id = get_object_or_404(SiteLogo, pk=logo_id)
        fs = FileSystemStorage()
        fs.delete(logo_by_its_id.logo.name)
        logo_by_its_id.delete()
        messages.success(request, "Successfully deleted!")
        return redirect("apAddSiteLogo")
    except:
        messages.warning(request, "Can't deleted! Please try again!")
        return redirect("apAddSiteLogo")

    return redirect('apAddSiteLogo')

# admin panel delete breaking news
@login_required(login_url='/ap/login/register')
def ap_editSiteLogo(request, logo_id):

    if request.method == 'POST':
        logo = request.FILES['edit_site_logo']
        list_of_logo_extension = str(logo).split('.')
        allowed_logo_extensions = ['png', 'jpg', 'jpeg', 'webp']

        if list_of_logo_extension[len(list_of_logo_extension) - 1] in allowed_logo_extensions:
            try:
                site_logo_model = get_object_or_404(SiteLogo, pk=logo_id)
                fs = FileSystemStorage()
                fs.delete(site_logo_model.logo.name)
                site_logo_model.logo = logo
                site_logo_model.save()
                messages.success(request, "Site logo updated successfully!")
                return redirect('apAddSiteLogo')
            except:
                messages.warning(request, "Site logo can't update! Please try again!")
                return redirect('apAddSiteLogo')
        else:
            messages.warning(request, "Logo can't be updated! Please try again!")
            return redirect('apAddSiteLogo')

    return redirect('apAddSiteLogo')


# header banner
@login_required(login_url='/ap/login/register')
def ap_addheaderBanner(request):

    if request.method == "POST":
        img = request.FILES['banner']
        link = request.POST['url']

        if img:
            save_to_db = HeaderBanner(img=img, link=link)
            save_to_db.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddHeaderBanner')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddHeaderBanner')

    # grabing header banner lilst
    header_bnnr_list = HeaderBanner.objects.all().order_by('-pk')

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context = {
        'header_bnnr_list': header_bnnr_list,

        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_headerBanner.html', context)


# header banner
@login_required(login_url='/ap/login/register')
def ap_deleteHeaderBanner(request, pk):
    try:
        header_bnr = HeaderBanner.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(header_bnr.img.name)
        header_bnr.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddHeaderBanner')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddHeaderBanner')

    return redirect('apAddHeaderBanner')


# header right icon
@login_required(login_url='/ap/login/register')
def ap_addHeader_rightIcon(request):

    if request.method == "POST":
        img = request.FILES['header_right_icon']
        link = request.POST['url']

        if img:
            header_right_icon = HeaderRightIcon(img=img, link=link)
            header_right_icon.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddHeaderIconright')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddHeaderIconright')

    # grabing header right icon list
    header_right_iconList = HeaderRightIcon.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'header_right_iconList' : header_right_iconList,

        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_header_right_icon.html', context)


# del header banner right icon
@login_required(login_url='/ap/login/register')
def ap_deleteHeaderRightIcon(request, pk):

    try:
        del_icon = HeaderRightIcon.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_icon.img.name)
        del_icon.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddHeaderIconright')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddHeaderIconright')

    return redirect('apAddHeaderIconright')


# header banner slider
@login_required(login_url='/ap/login/register')
def ap_add_banner_slider(request):

    if request.method == "POST":
        img = request.FILES['header_below_slider']
        link = request.POST['url']

        if img:
            header_banner_slider = BannerSlider(img1=img, link=link)
            header_banner_slider.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddBannerSlider')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddBannerSlider')

    # grabing header right icon list
    header_banner_slider = BannerSlider.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'header_banner_slider' : header_banner_slider,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/bannerSlider.html', context)


# del header banner slider
@login_required(login_url='/ap/login/register')
def ap_deleteHeaderBannerSlider(request, pk):

    try:
        del_bnr_slider = BannerSlider.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_bnr_slider.img1.name)
        del_bnr_slider.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddBannerSlider')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddBannerSlider')

    return redirect('apAddBannerSlider')


# add welcome banner
@login_required(login_url='/ap/login/register')
def ap_add_welcome_banner(request):

    if request.method == "POST":
        img = request.FILES['header_below_slider']
        link = request.POST['url']

        if img:
            welcome_banner = WelcomeBanner(img=img, link=link)
            welcome_banner.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddWelcomeBanner')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddWelcomeBanner')

    # grabing header right icon list
    welcome_banner_list = WelcomeBanner.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'welcome_banner_list' : welcome_banner_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/welcome_banner.html', context)

# del welcome banner
@login_required(login_url='/ap/login/register')
def ap_deleteWelcomeBanner(request, pk):

    try:
        del_welcome_bnnr = WelcomeBanner.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_welcome_bnnr.img.name)
        del_welcome_bnnr.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddWelcomeBanner')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddWelcomeBanner')

    return redirect('apAddBannerSlider')


# add welcome banner slider one
@login_required(login_url='/ap/login/register')
def ap_add_welcome_banner_sliderOne(request):

    if request.method == "POST":
        img = request.FILES['welcome_bnr_slider_1']
        link = request.POST['url']

        if img:
            welcome_banner_slider_1 = Welcome_bnner_Slider1(img=img, link=link)
            welcome_banner_slider_1.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddWelcomeBannerSliderOne')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddWelcomeBannerSliderOne')

    # grabing header right icon list
    welcome_banner_slider_1_list = Welcome_bnner_Slider1.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'welcome_banner_slider_1_list' : welcome_banner_slider_1_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/welcome_banner_sliderOne.html', context)


# del welcome banner slider one
@login_required(login_url='/ap/login/register')
def ap_deleteWelcomeBnrSliderTwo(request, pk):

    try:
        del_welcome_bnnr_slider_2 = Welcome_bnner_Slider2.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_welcome_bnnr_slider_2.img.name)
        del_welcome_bnnr_slider_2.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddWelcomeBannerSliderTwo')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddWelcomeBannerSliderTwo')

    return redirect('apAddWelcomeBannerSliderTwo')


# add welcome banner slider two
@login_required(login_url='/ap/login/register')
def ap_add_welcome_banner_sliderTwo(request):

    if request.method == "POST":
        img = request.FILES['welcome_bnr_slider_2']
        link = request.POST['url']

        if img:
            welcome_banner_slider_2 = Welcome_bnner_Slider2(img=img, link=link)
            welcome_banner_slider_2.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddWelcomeBannerSliderTwo')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddWelcomeBannerSliderTwo')

    # grabing header right icon list
    welcome_banner_slider_2_list = Welcome_bnner_Slider2.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'welcome_banner_slider_2_list' : welcome_banner_slider_2_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/welcome_banner_sliderTwo.html', context)


# del welcome banner slider two
@login_required(login_url='/ap/login/register')
def ap_deleteWelcomeBnrSliderOne(request, pk):

    try:
        del_welcome_bnnr_slider_1 = Welcome_bnner_Slider1.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_welcome_bnnr_slider_1.img.name)
        del_welcome_bnnr_slider_1.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddWelcomeBannerSliderOne')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddWelcomeBannerSliderOne')

    return redirect('apAddWelcomeBannerSliderOne')


# add how to play banner
@login_required(login_url='/ap/login/register')
def ap_add_howTo_play_banner(request):

    if request.method == "POST":
        img = request.FILES['howToPlayBanner']
        link = request.POST['url']

        if img:
            howTo_play_Bnnr = HowToPlayBanner(img=img, link=link)
            howTo_play_Bnnr.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddHowToPlayBanner')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddHowToPlayBanner')

    # grabing header right icon list
    howTo_play_bnner_list = HowToPlayBanner.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'howTo_play_bnner_list' : howTo_play_bnner_list,

        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/how_toPlay_banner.html', context)


# del how to play banner
@login_required(login_url='/ap/login/register')
def ap_deleteHow_toPlay_banner(request, pk):

    try:
        del_how_to_playBnnr = HowToPlayBanner.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_how_to_playBnnr.img.name)
        del_how_to_playBnnr.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddHowToPlayBanner')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddHowToPlayBanner')

    return redirect('apAddHowToPlayBanner')




# add min max withdraw banner
@login_required(login_url='/ap/login/register')
def ap_add_min_max_withdraw_bannr(request):

    if request.method == "POST":
        img = request.FILES['minMaxWithdrawBnr']
        link = request.POST['url']

        if img:
            min_max_withdrawBnr = MinMaxWithdrawBanner(img=img, link=link)
            min_max_withdrawBnr.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddMinMaxWithdrawBnnr')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddMinMaxWithdrawBnnr')

    # grabing header right icon list
    min_max_withdraw_bnr = MinMaxWithdrawBanner.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'min_max_withdraw_bnr' : min_max_withdraw_bnr,

        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/min_mx_withdrawBnnr.html', context)


# del welcome banner slider two
@login_required(login_url='/ap/login/register')
def ap_deleteMinMaxWithDrawBanner(request, pk):

    try:
        del_min_max_withdraw_amnt = MinMaxWithdrawBanner.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_min_max_withdraw_amnt.img.name)
        del_min_max_withdraw_amnt.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddMinMaxWithdrawBnnr')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddMinMaxWithdrawBnnr')

    return redirect('apAddMinMaxWithdrawBnnr')


# add gallery below withdraw banner
@login_required(login_url='/ap/login/register')
def ap_add_gallery_below_withdraw_bnr(request):

    if request.method == "POST":
        img = request.FILES['galleryBnr']
        link = request.POST['url']

        if img:
            gallery_withdrawBnr = GalleryBelowWithdrawBanner(img=img, link=link)
            gallery_withdrawBnr.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddGalleryBelowWithdrawBanner')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddGalleryBelowWithdrawBanner')

    # grabing header right icon list
    gallery_withdraw_bnr_list = GalleryBelowWithdrawBanner.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'gallery_withdraw_bnr_list' : gallery_withdraw_bnr_list,

        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_gallery_below_withdraw_bnr.html', context)


# delete gallery below withdraw banner
@login_required(login_url='/ap/login/register')
def ap_delete_Gallery_below_withdraw_bnr(request, pk):

    try:
        del_gallery_below_withdrawBnr = GalleryBelowWithdrawBanner.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_gallery_below_withdrawBnr.img.name)
        del_gallery_below_withdrawBnr.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddGalleryBelowWithdrawBanner')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddGalleryBelowWithdrawBanner')

    return redirect('apAddGalleryBelowWithdrawBanner')


# add gallery below withdraw banner
@login_required(login_url='/ap/login/register')
def ap_add_gallery_games(request):

    if request.method == "POST":
        img = request.FILES['galleryBnr']
        link = request.POST['url']

        if img:
            gallery_games = GalleryGames(img=img, link=link)
            gallery_games.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddGalleryGames')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddGalleryGames')

    # grabing header right icon list
    gallery_games_list = GalleryGames.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'gallery_games_list' : gallery_games_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_gallery_games.html', context)


# delete gallery below withdraw banner
@login_required(login_url='/ap/login/register')
def ap_delete_Gallery_games(request, pk):

    try:
        del_gallery_games = GalleryGames.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_gallery_games.img.name)
        del_gallery_games.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddGalleryGames')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddGalleryGames')

    return redirect('apAddGalleryGames')


# add gallery below withdraw banner
@login_required(login_url='/ap/login/register')
def ap_add_payment_method(request):

    if request.method == "POST":
        img = request.FILES['payment_method']
        link = request.POST['url']

        if img:
            payment_method_bnr = PaymentMethodsBanner(img=img, link=link)
            payment_method_bnr.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddPaymentMethod')
        else:
            messages.warning(request, "Something wrong. Try again!")
            return redirect('apAddPaymentMethod')

    # grabing header right icon list
    payment_method_list = PaymentMethodsBanner.objects.all().order_by('-pk')[:5]

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    context =  {
        'payment_method_list' : payment_method_list,
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/add_payment_method.html', context)


# delete gallery below withdraw banner
@login_required(login_url='/ap/login/register')
def ap_delete_payment_method(request, pk):

    try:
        del_payment_method = PaymentMethodsBanner.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(del_payment_method.img.name)
        del_payment_method.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddPaymentMethod')
    except:
        messages.warning(request, "Something wrong. Try again!")
        return redirect('apAddPaymentMethod')

    return redirect('apAddPaymentMethod')


# about us
@login_required(login_url='/ap/login/register')
def ap_aboutUs(request):

    if request.method == 'POST':
        about_us_txt = request.POST['about_us']

        if about_us_txt:
            about_us_model = AboutUs(about_us=about_us_txt)
            about_us_model.save()
            messages.success(request, "Successfully added!")
            return redirect('apAboutUs')
        else:
            messages.warning(request, "Can't be added! Try again!")
            return redirect('apAboutUs')

    # about us model
    aboutUs = AboutUs.objects.filter().first()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'about_us' : aboutUs,
        # user profile
        'userProfile': userProfile,
        'site_logo': site_logo,
    }

    return render(request, 'back-end/admin_panel/about_us.html', context)

# delete about us
@login_required(login_url='/apLoginRegister/')
def ap_delAboutUs(request, pk):

    try:
        about_us_model = AboutUs.objects.get(pk=pk)
        about_us_model.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAboutUs')
    except:
        messages.warning(request, "Try again!")
        return redirect('apAboutUs')

    return redirect('apAboutUs')

# edit about us
@login_required(login_url='/ap/login/register')
def ap_editAboutUs(request, pk):

    if request.method == 'POST':
        about_us = request.POST['about_us']

        if about_us:
            about_us_model_byPK = AboutUs.objects.get(pk=pk)
            about_us_model_byPK.about_us = about_us
            about_us_model_byPK.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAboutUs')
        else:
            messages.warning(request, "Try again!")
            return redirect('apAboutUs')

    return redirect('apAboutUs')

# msg list
@login_required(login_url='/ap/login/register')
def ap_VisitorMsgList(request):

    # msg model
    msg_list = Message.objects.all()

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()


    context = {
        'msg_list' : msg_list,
        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }

    return render(request, "back-end/admin_panel/msg_list.html", context)

# msg delete
@login_required(login_url='/ap/login/register')
def ap_DelVisitorMsg(request, pk):

    try:
        msg = Message.objects.get(pk=pk)
        msg.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apVisitorMessageList')
    except:
        messages.warning(request, "Something wrong! Try again!")
        return redirect('apVisitorMessageList')

    return redirect('apVisitorMessageList')


# add social media link
@login_required(login_url='/ap/login/register')
def ap_addSocialMediaLink(request):

    # user profile
    userProfile = UserProfile.objects.filter(user=request.user).first()

    # logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    if request.method == 'POST':
        fb = request.POST['fb_link']
        tw = request.POST['tw_link']
        insta = request.POST['insta_link']
        linkedIn = request.POST['linkIn_link']

        if fb != '' or tw != '' or insta != '' or linkedIn != '':
            socialMediaLink_model = SocailMediaLinks(fb=fb, tw=tw, insgrm=insta,linkedin=linkedIn)
            socialMediaLink_model.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddSocialMediaLink')

        else:
            messages.warning(request, "Something wrong! Try again!")
            return redirect('apAddSocialMediaLink')

    existing_links = SocailMediaLinks.objects.filter().first()

    context = {
        'social_media_links' : existing_links,

        # user profile
        'userProfile': userProfile,

        'site_logo': site_logo,
    }


    return render(request, 'back-end/admin_panel/add_social_media_link.html', context)


# delete social media link
@login_required(login_url='/ap/login/register')
def ap_delSocialMediaLink(request, pk):

    try:
        social_media_link_model = SocailMediaLinks.objects.get(pk=pk)
        social_media_link_model.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apAddSocialMediaLink')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apAddSocialMediaLink')

    return redirect('apAddSocialMediaLink')


# edit social media link
@login_required(login_url='/ap/login/register')
def ap_editSocialMediaLink(request, pk):

    if request.method == 'POST':
        fb_link = request.POST['fb_link']
        tw_link = request.POST['tw_link']
        insta_link = request.POST['insta_link']
        linkIn_link = request.POST['linkIn_link']

        if fb_link != '' or tw_link != '' or insta_link != '' or linkIn_link != '':
            social_media_model = SocailMediaLinks.objects.get(pk=pk)
            social_media_model.fb = fb_link
            social_media_model.tw = tw_link
            social_media_model.insgrm = insta_link
            social_media_model.linkedin = linkIn_link

            social_media_model.save()
            messages.success(request, "Successfully updated!")
            return redirect('apAddSocialMediaLink')
        else:
            messages.warning(request, "Can't be updated! Try again!")
            return redirect('apAddSocialMediaLink')


    return redirect('apAddSocialMediaLink')













