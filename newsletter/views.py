from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.core.mail import get_connection, send_mail
from django.core import mail
from django.utils import timezone
from django.core.mail.message import EmailMessage

from newsletter.forms import MailForm, Newsletter
from newsletter.models import Mails, Message


# Create your views here.

def homepage(request):
	return render(request, 'index.html')

def newsletter(request):
	form = MailForm;
	content = {'form' : form }
	if request.method == 'POST':
		if form.is_valid:
			mail = request.POST['mail']
			if not Mails.objects.filter(mail=mail).exists() and '@' in list(mail):
				Mails.objects.create(mail=mail)
				if 'error' in content:
					content.pop('error')
				return HttpResponseRedirect('/thanks/')
			if Mails.objects.filter(mail=mail).exists(): #errors when subscriber adds his/her e-mail and it fails
				content.update({'error' : 'Taki adres e-mail już został dodany.'}) # for it already exists
			elif '@' in list(mail):
				content.update({'error' : 'Niepoprawna forma adresu e-mail.'}) # for its form is wrong
		else:
			content.pop('error') # DRY rule has been broken here. I'm going to fix it soon.

	return render(request, 'newsletter.html', content)

def login_view(request):
	username = request.POST('username', '')
	password = request.POST("password", '')
	user = authenticate(username=username, password=password)
	if form.is_valid:
		if user is not None and user.is_active:
			login(request, user)
			return HttpResponseRedirect('/panel/news-manager/')
		else:
			return HttpResponseRedirect('/logging-failure/')


def logout_view(request):
	logout(request, '/logged-out/')
	return render(request, 'registration/logout.html')

def thanks(request):
	return render(request, 'thanks.html')

def failure(request):
	return render(request, 'failure.html')

@login_required()
def manage_mails(request):
	mails = Mails.objects.all()
	if request.method == 'POST':
		Mails.objects.filter(id=request.POST['del']).delete()
	content = {'mail_list' : mails}
	return render(request, 'panel/manage_mails.html', content)

@login_required()
def manage_news(request):
	content = {'form' : Newsletter, 'msg_list' : Message.objects.all().filter().order_by('-date')}
	if request.method == 'POST':
		if content['form'].is_valid:
			Message.objects.create(subject=request.POST['title'],
								  news_msg=request.POST['message'])
			
			with get_connection( # HERE is how you connect to your SMTP server. You have to specify password, username, host, port and tls (as long as it's turned on).
								host='localhost', 
								port='1027', 
								#username=my_username, 
								#password=my_password, 
								#user_tls=my_use_tls
								) as connection:
				EmailMessage(request.POST['title'], request.POST['message'], 'from1', ['to1'],
								connection=connection).send()
	return render(request, 'panel/manage_news.html', content)