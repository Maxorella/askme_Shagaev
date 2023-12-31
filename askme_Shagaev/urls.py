"""
URL configuration for askme_Shagaev project.

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
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('admin/', admin.site.urls),
    path('hot/', views.hotquestions, name='hotquestions'),
    path('tag/<tag_name>',views.tagpage, name='tagpage'),
    path('question/<int:question_id>', views.onequest, name='onequestion'),
    path('login', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='logout'),
    path('signup', views.signup, name='signup'),
    path('ask',views.askquestion, name='askquestion'),
    path('settings',views.settings, name='settings')
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)