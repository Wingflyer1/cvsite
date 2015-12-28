from django.shortcuts import render
from datetime import date

def about(request):
	today = date.today()
	my_birthday = date(1977,4,12)
	curr_employer = 'Kystverket'

	my_age = today.year - my_birthday.year - ((today.month, today.day ) < (my_birthday.month, my_birthday.day))
	personal = {
		"Fodselsdato": my_birthday,
		"Alder": my_age,
		"Arbeidsgiver": curr_employer,
		"Sivilstand": 'Gift, 3 barn',
		"Bosted": 'Aakrehamn, Karmoy',
	}

	context = {
		"personal":personal,
	}

	return render(request, "about.html", context)