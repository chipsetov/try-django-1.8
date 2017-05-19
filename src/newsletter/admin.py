from django.contrib import admin

# Register your models here.
from .forms import SingUpForm
from .models import SingUp

class SingUpAdmin(admin.ModelAdmin):
	list_display = ["__str__", "timestamp", "updated"]
	form = SingUpForm
	#class Meta:
	#	model = SingUp

admin.site.register(SingUp, SingUpAdmin)