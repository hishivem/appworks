"""appworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
admin.site.site_header = "Appworks Admin"
from main import views

urlpatterns = [
    url(r'^bigdrop/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^work-with-us/$', views.WorkWithUs.as_view(), name='work-with-us'),
    url(r'^invest-with-us/$', views.InvestWithUs.as_view(), name='invest-with-us'),
    url(r'^contact-us/$', views.ContactUs.as_view(), name='contact-us'),
    url(r'^aw-philosophy/$', views.Awphilosophy.as_view(), name='aw-philosophy'),
    url(r'^where-we-headed/$', views.Whereweheaded.as_view(), name='where-we-headed'),
    url(r'^seven/$', views.Seven.as_view(), name='seven'),
    url(r'^eight/$', views.Eight.as_view(), name='eight'),
    url(r'^nine/$', views.Nine.as_view(), name='nine'),
    url(r'^ten/$', views.Ten.as_view(), name='ten'),
    url(r'^eleven/$', views.Eleven.as_view(), name='eleven'),
    url(r'^twelve/$', views.Twelve.as_view(), name='twelve'),
    url(r'^thirteen/$', views.Thirteen.as_view(), name='thirteen'),
    url(r'^fourteen/$', views.Fourteen.as_view(), name='fourteen'),
    url(r'^fifteen/$', views.Fifteen.as_view(), name='fifteen'),
    url(r'^press/$', views.Press.as_view(), name='press'),
	 
]
