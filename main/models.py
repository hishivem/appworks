from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ContactUs(models.Model):
	name = models.CharField(max_length=80, null=True, blank=False)
	email = models.EmailField(null=True, blank=False)
	message = models.TextField(null=True, blank=False)


	def __unicode__(self):
		return """%s:%s""" % (self.name, self.email)
