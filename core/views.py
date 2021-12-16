from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from adminPanel.models import *


def index(request):

    # site logo
    site_logo = SiteLogo.objects.filter().order_by('-pk').first()

    # HeaderBanner
    headerBanner = HeaderBanner.objects.filter().order_by('-pk').first()

    # HeaderRightIcon
    headerRightIcon = HeaderRightIcon.objects.filter().order_by('-pk').first()


    # BannerSlider
    bannerSlider = BannerSlider.objects.filter().order_by('-pk')[:5]

    # WelcomeBanner
    welcomeBanner = WelcomeBanner.objects.filter().order_by('-pk').first()

    # Welcome_bnner_Slider1
    welcome_banner_slider1 = Welcome_bnner_Slider1.objects.filter().order_by('-pk')[:5]

    # Welcome_bnner_Slider2
    welcome_bnner_Slider2 = Welcome_bnner_Slider2.objects.filter().order_by('-pk')[:5]

    # HowToPlayBanner
    howToPlayerBanner = HowToPlayBanner.objects.filter().order_by('-pk').first()

    # MinMaxWithdrawBanner
    minMaxWithdrawBanner = MinMaxWithdrawBanner.objects.filter().order_by('-pk').first()

    # GalleryBelowWithdrawBanner
    galleryBelowWithdrawBnr = GalleryBelowWithdrawBanner.objects.filter().order_by('-pk')[:7]

    # GalleryGames
    galleryGames = GalleryGames.objects.filter().order_by('-pk')[:12]

    # PaymentMethodsBanner
    paymentMethodBanner = PaymentMethodsBanner.objects.filter().order_by('-pk').first()

    context = {
        "site_logo": site_logo,
        "headerBanner": headerBanner,
        "headerRightIcon": headerRightIcon,
        "bannerSlider": bannerSlider,
        "welcomeBanner": welcomeBanner,
        "welcome_banner_slider1":welcome_banner_slider1,
        "welcome_bnner_Slider2": welcome_bnner_Slider2,
        "howToPlayerBanner":howToPlayerBanner,
        "minMaxWithdrawBanner": minMaxWithdrawBanner,
        "galleryBelowWithdrawBnr": galleryBelowWithdrawBnr,
        "galleryGames": galleryGames,
        "paymentMethodBanner": paymentMethodBanner
    }


    return render(request, "front-end/index.html", context)
