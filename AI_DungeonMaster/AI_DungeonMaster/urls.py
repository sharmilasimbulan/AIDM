"""
URL configuration for AI_DungeonMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from Infinite_Questmaster import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signuppage, name='signup'),
    path('account1/', views.account1, name='account1'),
    path('account2/', views.account2, name='account2'),
    path('account3/', views.account3, name='account3'),
    path('feedback/', views.feedback, name='feedback'),
    path('character/', views.character, name='character'),
    path('charactercreate/', views.charactercreate, name='charactercreate'),
    path('campaign/', views.campaign, name='campaign'),
    #path('chatbot/', views.chatbot, name='chatbot'),
    path('game/', views.game, name='game'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

