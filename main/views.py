from django.views.generic import View
from django.views.generic import ListView 
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.shortcuts import render
from main import models
from django.contrib.messages import  add_message

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"


class ContactUs(TemplateView):
    template_name = "contact-us.html"


class Contactus(TemplateView):
    template_name = "meet-and-co.html"


class Whereweheaded(TemplateView):
    template_name = "where-we-headed.html"


class Boardadvisoryservices(TemplateView):
    template_name = "board-advisory-services.html"


class Awphilosophy(TemplateView):
    template_name = "aw-philosophy.html"


class Seven(TemplateView):
    template_name = "seven.html"


class Eight(TemplateView):
    template_name = "eight.html"


class Nine(TemplateView):
    template_name = "nine.html"


class Ten(TemplateView):
    template_name = "ten.html"


class Eleven(TemplateView):
    template_name = "eleven.html"


class Twelve(TemplateView):
    template_name = "twelve.html"


class Thirteen(TemplateView):
    template_name = "thirteen.html"


class Fourteen(TemplateView):
    template_name = "fourteen.html"


class Fifteen(TemplateView):
    template_name = "fifteen.html"


class Press(TemplateView):
    template_name = "press.html"


class WorkWithUs(CreateView):
    model = models.ContactUs
    template_name = "work-with-us.html"
    fields = ['name', 'email', 'message']
    success_url = "/invest-with-us"
    
    def form_valid(self, form):
        fi = form.save(commit=False)
        fi.save()
       	add_message(self.request, 25, "We will get in touch with you.")
        return super(WorkWithUs, self).form_valid(form)

    def form_invalid(self, form):
    	return super(WorkWithUs, self).form_invalid(form)

# class InvestWithUs(TemplateView):
#     template_name = "invest-with-us.html"


class InvestWithUs(CreateView):
    model = models.ContactUs
    template_name = "invest-with-us.html"
    fields = ['name', 'email', 'message']
    success_url = "/invest-with-us"
    
    def form_valid(self, form):
        fi = form.save(commit=False)
        fi.save()
        add_message(self.request, 25, "We will get in touch with you.")
        return super(InvestWithUs, self).form_valid(form)

    def form_invalid(self, form):
    	print form.errors
    	return super(InvestWithUs, self).form_invalid(form) 




