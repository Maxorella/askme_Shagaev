"""
URL configuration for TechnoWebShagaev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.urls import reverse

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('admin/', admin.site.urls),
    path('hot', views.hotquestions, name='hotquestion'),
    path('tag/<tag_name>',views.tagpage, name='tagpage'),#TODO
    path('question/<int:question_id>', views.onequest, name='onequestion'),#TODO
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('ask',views.askquestion, name='askquestion'),
    path('settings',views.settings, name='settings')
]
