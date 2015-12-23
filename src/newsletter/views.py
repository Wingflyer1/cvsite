from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	title = 'Motta en PDF-CV'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Takk, \n du vil om litt motta en PDF versjon av min CV til din e-post."
		}

	if request.user.is_authenticated() and request.user.is_staff:
		#print(SignUp.objects.all())
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)
		# 	i += 1

		queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
		#print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
		context = {
			"queryset": queryset
		}

	return render(request, "home.html", context)



def contact(request):
	title = 'Send meg en melding:'
	title_align_center = True
	button_text = 'Send\ meldingen'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("epost")
		form_message = form.cleaned_data.get("melding")
		form_full_name = form.cleaned_data.get("ditt_navn")
		# print email, message, full_name
		subject = 'Sten Terje Falnes - CV kontakt skjema'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'sten.terje.falnes@kystverket.no']
		contact_message = "%s har sendt deg en beskjed:\r\n %s \n\r \n\rvia %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		#some_html_message = """
		#<h1>hello</h1>
		#"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				#html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
		"button_text": button_text,
	}
	return render(request, "forms.html", context)




