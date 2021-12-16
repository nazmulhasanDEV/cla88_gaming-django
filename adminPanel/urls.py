from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^ap/index/$', views.ap_index, name="apIndex"),
    re_path(r'^ap/home/$', views.ap_home, name="apHome"),

    re_path(r'^ap/remove/user/(?P<pk>\d+)/$', views.ap_removeUser, name="apRemoveUser"),



    # add site logo ############################################
    re_path(r'^ap/add/site/logo/$', views.ap_addSiteLogo, name="apAddSiteLogo"),

    # delete site logo
    re_path(r'^ap/del/site/logo/(?P<logo_id>\d+)/$', views.ap_delSiteLogo, name="apDelSiteLogo"),

    # edit site logo
    re_path(r'^ap/edit/site/logo/(?P<logo_id>\d+)/$', views.ap_editSiteLogo, name="apEditSiteLogo"),

    # add header_banner
    re_path(r'^ap/add/header/banner/$', views.ap_addheaderBanner, name="apAddHeaderBanner"),
    re_path(r'^ap/del/header/banner/(?P<pk>\d+)/$', views.ap_deleteHeaderBanner, name="apDelHeaderBanner"),

    # header right icon
    re_path(r'^ap/add/header/right/icon/$', views.ap_addHeader_rightIcon, name="apAddHeaderIconright"),
    re_path(r'^ap/del/header/right/icon/(?P<pk>\d+)/$', views.ap_deleteHeaderRightIcon, name="apDelHeaderBannerRightIcon"),

    # slider below banner
    re_path(r'^ap/add/header/banner/slider/$', views.ap_add_banner_slider, name="apAddBannerSlider"),
    re_path(r'^ap/del/header/banner/slider/(?P<pk>\d+)/$', views.ap_deleteHeaderBannerSlider, name="apDelHeaderBannerSlider"),

    # welcome banner
    re_path(r'^ap/add/welcome/banner/$', views.ap_add_welcome_banner, name="apAddWelcomeBanner"),
    re_path(r'^ap/del/welcome/banner/(?P<pk>\d+)/$', views.ap_deleteWelcomeBanner, name="apDelWelcomeBnnr"),

    # welcome banner slider one
    re_path(r'^ap/add/welcome/banner/slider/one/$', views.ap_add_welcome_banner_sliderOne, name="apAddWelcomeBannerSliderOne"),
    re_path(r'^ap/del/welcome/banner/slider/one/(?P<pk>\d+)/$', views.ap_deleteWelcomeBnrSliderOne, name="apDeleteWelcomeBnrSliderOne"),

    # welcome banner slider two
    re_path(r'^ap/add/welcome/banner/slider/two/$', views.ap_add_welcome_banner_sliderTwo, name="apAddWelcomeBannerSliderTwo"),
    re_path(r'^ap/del/welcome/banner/slider/two/(?P<pk>\d+)/$', views.ap_deleteWelcomeBnrSliderTwo, name="apDeleteWelcomeBnrSliderTwo"),

    # how to play banner
    re_path(r'^ap/add/how/to/play/banner/$', views.ap_add_howTo_play_banner, name="apAddHowToPlayBanner"),
    re_path(r'^ap/del/how/to/play/banner/(?P<pk>\d+)/$', views.ap_deleteHow_toPlay_banner, name="apDeleteHowToPlayBanner"),

    # min max withdraw amount
    re_path(r'^ap/add/min/max/withdraw/amnt/$', views.ap_add_min_max_withdraw_bannr, name="apAddMinMaxWithdrawBnnr"),
    re_path(r'^ap/del/min/max/withdraw/amnt/(?P<pk>\d+)/$', views.ap_deleteMinMaxWithDrawBanner, name="apDeleteMinMaxWithdrawBnnr"),


    # Gallery below withdraw banner
    re_path(r'^ap/add/gallery/bel/withraw/banner/$', views.ap_add_gallery_below_withdraw_bnr, name="apAddGalleryBelowWithdrawBanner"),
    re_path(r'^ap/del/gallery/bel/withraw/banner/(?P<pk>\d+)/$', views.ap_delete_Gallery_below_withdraw_bnr, name="apDeleteGalleryBelWithdrawBnr"),

    # Gallery games
    re_path(r'^ap/add/gallery/games/$', views.ap_add_gallery_games, name="apAddGalleryGames"),
    re_path(r'^ap/del/gallery/games/(?P<pk>\d+)/$', views.ap_delete_Gallery_games, name="apDeleteGalleryGames"),

    # payment method banner
    re_path(r'^ap/add/payment/method/$', views.ap_add_payment_method, name="apAddPaymentMethod"),
    re_path(r'^ap/del/payment/method/(?P<pk>\d+)/$', views.ap_delete_payment_method, name="apDeletePaymentMethod"),


    #  about us
    re_path(r'^ap/news/about/us/$', views.ap_aboutUs, name="apAboutUs"),
    re_path(r'^ap/del/news/about/us/(?P<pk>\d+)/$', views.ap_delAboutUs, name='apDelAboutUs'),
    re_path(r'^ap/del/news/about/us/edit/(?P<pk>\d+)/$', views.ap_editAboutUs, name='apEditAboutUs'),

    # msg list
    re_path(r'^ap/visitor/msg/list/$', views.ap_VisitorMsgList, name="apVisitorMessageList"),

    re_path(r'^ap/del/visitor/msg/(?P<pk>\d+)/$', views.ap_DelVisitorMsg, name="apDelVisitorMsg"),

    #************integrate social media link
    re_path(r'^ap/add/social/media/link/$', views.ap_addSocialMediaLink, name="apAddSocialMediaLink"),
    re_path(r'^ap/del/social/media/link/(?P<pk>\d+)/$', views.ap_delSocialMediaLink, name="apDelSocialMediaLink"),
    re_path(r'^ap/edit/social/media/link/(?P<pk>\d+)/$', views.ap_editSocialMediaLink, name="apEditSocialMediaLink"),


]
