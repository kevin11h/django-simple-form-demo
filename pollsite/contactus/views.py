# Create your views here.
from django.shortcuts import render_to_response
from django.core.mail import mail_admins
from django import forms
from django.template import RequestContext

class ContactForm(forms.Form):
	name = forms.CharField(max_length=200)
	email= forms.EmailField()
	title= forms.CharField(max_length=200)
	text = forms.CharField(widget=forms.Textarea)

def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		
		if form.is_valid():
			mail_admins(
				"Contact Form: %s" % form.cleaned_data['title'],#form.title,
				"%s <%s> Said: %s" % (form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['text']))
			return render_to_response("contactus/success.html")
	else:
		form = ContactForm()

	return render_to_response("contactus/form.html", {'form': form}, context_instance = RequestContext(request))
