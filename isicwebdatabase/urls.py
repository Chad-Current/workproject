from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views
from django.contrib.auth import views as auth_views
from .views import *
from users import views as user_views
from genesis import views as genesis_views
from ticket import views as ticket_views
app_name = 'isicwebdatabase'


urlpatterns = [
    # path('', views.home, name='home-page'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register-user'),
    path('home/', views.index, name='index-home'),
    path('profile/', user_views.UserProfile.as_view(template_name='users/profile.html'), name='profile-home'),
    path('poc/', login_required(PocHomeView.as_view()), name='poc-home'),
    path('poc/?county', PocSearchViewCounty.as_view(), name='poccounty-results'),
    path('poc/?pointofcontact', PocSearchViewPoc.as_view(), name='pocpoc-results'),
    path('poc/?organization', PocSearchViewOrg.as_view(), name='pocorg-results'),
    path('poc/?level', PocSearchViewLevel.as_view(), name='poclvl-results'),
    path('applicants/?', ApplicantView.as_view(), name='applicant-results'),
    path('siteinformation/', SiteHomeView.as_view(), name='site-home-info'),
    path('siteinformation/?sitename', SiteNameView.as_view(), name='site-name-info'),
    # path('siteinformation/?sitealias', SiteAliasView.as_view(), name='site-alias-info'),
    path('siteinformation/?siteid', SiteIdView.as_view(), name='site-id-info'),
    path('genesisreports/', genesis_views.genesis, name='genesis-reports'),
    path('sitetraining/', login_required(views.SiteTraining.as_view()), name='site-training'),

]
