from django.shortcuts import render, redirect
from django.core.cache import cache
from django.core.mail import send_mail
from django.contrib import messages
import random

def send_otp_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email and email.endswith('@vitbhopal.ac.in'):
            otp = str(random.randint(100000, 999999))
            cache.set(email, otp, timeout=300)  # store for 5 minutes

            # Send OTP to college email
            send_mail(
                subject='Your VIT Bhopal Login OTP',
                message=f'Your OTP is: {otp}',
                from_email='youremail@gmail.com',  # your verified email
                recipient_list=[email],
                fail_silently=False,
            )

            request.session['email'] = email  # save email in session for next step
            return redirect('verify_otp')
        else:
            messages.error(request, "Only @vitbhopal.ac.in emails are allowed!")

    return render(request, 'accounts/send_otp.html')

def verify_otp_view(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        email = request.session.get('email')

        if email and entered_otp == cache.get(email):
            # OTP is correct
            cache.delete(email)  # Optional: clear it after use
            return render(request, 'accounts/home.html', {'email': email})

        messages.error(request, "Invalid OTP. Try again!")

    return render(request, 'accounts/verify_otp.html')



def home_view(request):
    return render(request, 'accounts/home.html')
def menu(request):
    return render(request, 'accounts/menu.html')
def contact(request):
    return render(request, 'accounts/contact.html')
def cart(request):
    return render(request, 'accounts/cart_index.html') 
