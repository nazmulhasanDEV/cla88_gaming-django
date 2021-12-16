from django.db import models


# Add News Model
# class News(models.Model):
#     class NewsGeneralObjects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset().filter(news_types='general_news')
#
#     objects = models.Manager() # built-in manager
#     leadmainobjects = LeadMainObjects() # custom manager
#     leadminor1objects = LeadMinor1Objects() # custom manager
#     leadminor2objects = LeadMinor2Objects() # custom manager
#     newsgeneralobjects = NewsGeneralObjects() # custom manager
#     publishedObjects = PublishedNews() # custom manager
#

# site logo
class SiteLogo(models.Model):
    logo = models.ImageField(upload_to="logos")
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.logo)


# header banner
class HeaderBanner(models.Model):
    img = models.ImageField(upload_to="header_banner")
    link = models.CharField(default='', max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

# header right icon
class HeaderRightIcon(models.Model):
    img = models.ImageField(upload_to="header_right_icon")
    link = models.CharField(default='', max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

# banner
class BannerSlider(models.Model):
    img1 = models.ImageField(upload_to="banner_slider")
    link = models.CharField(default='', max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.pk)


# welcome banner
class WelcomeBanner(models.Model):
    img = models.ImageField(upload_to="welcome_banner")
    link = models.CharField(default='', max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

# slider below welcome banner
class Welcome_bnner_Slider1(models.Model):
    img = models.ImageField(upload_to="welcome_bnr_slider1")
    link = models.CharField(default='', max_length=300, blank=True, null=True)
    def __str__(self):
        return str(self.pk)

# slider below welcome banner2
class Welcome_bnner_Slider2(models.Model):
    img = models.ImageField(upload_to="welcome_bnr_slider1")
    link = models.CharField(default='', max_length=300, blank=True, null=True)
    def __str__(self):
        return str(self.pk)


# how to play banner
class HowToPlayBanner(models.Model):
    img = models.ImageField(upload_to="howToPlay")
    link = models.CharField(default='', max_length=300, blank=True, null=True)
    def __str__(self):
        return str(self.pk)

# min max deposit withdraw banner
class MinMaxWithdrawBanner(models.Model):
    img = models.ImageField(upload_to="howToPlay")
    link = models.CharField(default='', max_length=300, blank=True, null=True)
    def __str__(self):
        return str(self.pk)


# Gallery under min max withrdaw banner
class GalleryBelowWithdrawBanner(models.Model):
    img = models.ImageField(upload_to="howToPlay")
    link = models.CharField(default='', max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.pk)


# our game gallery
class GalleryGames(models.Model):
    img = models.ImageField(upload_to="howToPlay")
    link = models.CharField(default='', max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

# payment methods
class PaymentMethodsBanner(models.Model):
    img = models.ImageField(upload_to="payment_method_banner")
    link = models.CharField(default='', max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.pk)



# about us
class AboutUs(models.Model):
    about_us = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + "|" + str(self.added_at)



# social media links
class SocailMediaLinks(models.Model):
    fb = models.CharField(max_length=255, blank=True, null=True)
    tw = models.CharField(max_length=255, blank=True, null=True)
    insgrm = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.pk)




