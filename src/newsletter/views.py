from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm, SingUpForm

from .models import SingUp
# Create your views here.
def home(request):
	title = "Sing Up Now"
	#if request.user.is_authenticated():
	#	title = "My title %s" %(request.user)

	#print (request)
	#if request.method == "POST":
	#	print (request.POST)
	
	form = SingUpForm(request.POST or None)
	context = {
		"template_title": title,
		"form": form
	}
	if form.is_valid():
		#form.save()
		instance = form.save(commit=False)
		if not instance.fullname:
			instance.fullname = "Justin"
		instance.save()
		context = {
			"template_title": "Thank you"
		}
		print (instance.email)
		print (instance.timestamp)

	if request.user.is_authenticated() and request.user.is_staff:
			#print(SingUp.objects.all())
			# for item in SingUp.objects.all():
			# 	print(item.	fullname)
			# context = {
			# 	"queryset": [123, 456]
			# }
			queryset = SingUp.objects.all().order_by('-timestamp')
			context = {
				"queryset": queryset
			}


	return render(request, "home.html", context)


def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# # for key, value in form.cleaned_data.itemview():
		# for key, value in iter(form.cleaned_data.items()):
		# 	print (key, value)
		# 	# print (form.cleaned_data.get(key))
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_fullname = form.cleaned_data.get("fullname")
		# print (email, message, fullname)
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'otheremail@xx.xx']
		contact_message = "%s: %s via %s"%(
			form_fullname, 
			form_message, 
			form_email)

		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject,
				contact_message,
				from_email,
				to_email,
				html_message=some_html_message,
				fail_silently=False) #True in DB
	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}

	return render(request, "forms.html", context)