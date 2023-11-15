from django.shortcuts import render
from django.http import HttpResponse
import string
import random

def password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))  # Default to 12 if not provided
        choices = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(choices) for _ in range(length))
        return render(request, 'password.html', {'password': password})
    return render(request, 'password.html')