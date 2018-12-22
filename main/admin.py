from django.contrib import admin
from main import models
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['name', 'email']
admin.site.register(models.ContactUs, ContactUsAdmin)
