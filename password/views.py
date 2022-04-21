from django.shortcuts import render
from password.forms import PasswordForm
from password.models import Password
from django import forms
import requests
import hashlib
import sys
# Create your views here.

def home_page(request):
    if(request.method == 'POST'):
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = Password.objects.latest('id')
            count = pwned_api_check(form_data.password)
            Password.objects.all().delete()
            return render(request, 'success.html', {'count' : count})

    form = PasswordForm()
    context = {'form' : form}
    return render(request, 'home.html', context)

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_five)
    return get_password_leaks_count(response, tail)

def request_api_data(query_check):
    url = 'https://api.pwnedpasswords.com/range/' + query_check
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching : {res.status_code}, please check your api!')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count 
    return 0