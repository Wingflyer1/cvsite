from django.shortcuts import render
from .models import Experience
# Create your views here.


def experience(request):
	title = 'Min yrkeserfaring'
	message = 'Denne siden vises bare om du er logget inn.'
	context = {
		'message': message,
		'title': title
	}
	if request.user.is_authenticated():
	# 	#print(SignUp.objects.all())
	# 	# i = 1
	# 	# for instance in SignUp.objects.all():
	# 	# 	print(i)
	# 	# 	print(instance.full_name)
	# 	# 	i += 1
		message = 'Her er min utdanning.'

		queryset = Experience.objects.all().order_by('-year_from') #.filter(full_name__iexact="Justin")
		#print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
		context = {
			"queryset": queryset,
			'title': title
		}

	return render(request, "experience.html", context)