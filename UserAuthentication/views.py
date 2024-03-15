from django.contrib.auth import authenticate,login,logout
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import Q

def register(request):
    if request.method == "POST":
        u = request.POST.get('u')
        p = request.POST.get('p')
        p1 = request.POST.get('p1')
        e = request.POST.get('e')
        f = request.POST.get('f')
        l = request.POST.get('l')

        # Password validation
        errors = []
        if len(p) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in p):
            errors.append("Password must contain at least one uppercase letter.")
        if not any(char in "!@#$%^&*()-_+={}[]:;\"'<>,.?/~" for char in p):
            errors.append("Password must contain at least one special character.")
        if p != p1:
            errors.append("Passwords do not match.")

        # Email validation
        try:
            validate_email(e)
        except ValidationError:
            errors.append("Invalid email address.")

        if errors:
            error_message = "\n".join(errors)
            messages.error(request, error_message)
            return redirect('UserAuthentication:register')  # Redirect back to registration form with error messages

        try:
            # Check if the email address already exists
            if User.objects.filter(Q(email=e)).exists():
                messages.error(request, "Email address already exists. Please use a different email address.")
                return redirect('UserAuthentication:register')

            # If no errors and email address is unique, create the user
            user = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)

            # Send confirmation email
            subject = 'Registration Successful'
            message = f"Hello {u},\n\nThank you for registering with us. Your account has been successfully created.\n\nYou can now login to your account."
            from_email = 'sreeragp10@gmail.com'  # Update with your Gmail address
            to_email = [e]  # Use the provided email address
            send_mail(subject, message, from_email, to_email)

            # Registration successful message using SweetAlert
            messages.success(request, "Registration successful. You can now login.")
            return redirect('UserAuthentication:login')

        except IntegrityError:
            messages.error(request, "Username or email address already exists.")
            return redirect('UserAuthentication:register')  # Redirect back to registration form with error message

    return render(request, 'userAuth/register.html')




def user_login(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            # Check if there's a success message stored in the session
            if 'password_reset_success' in request.session:
                messages.success(request, request.session['password_reset_success'])
                del request.session['password_reset_success']  # Remove the success message from the session
            return redirect('app1:packages')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'userAuth/login.html')


def user_logout(request):
    logout(request)
    return user_login(request)




def email_confirm(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:  # Check if email is empty
            messages.error(request, 'Please enter an email address.')
            return redirect('UserAuthentication:confirm')
        try:
            # Check if the email exists in the database
            user = User.objects.get(email=email)
            # Generate OTP
            otp = get_random_string(length=6, allowed_chars='1234567890')
            # Store the OTP in the session
            request.session['otp'] = otp
            request.session['email'] = email
            # Send the OTP to the user's email address
            subject = 'OTP for Password Reset'
            message = f'Your OTP for password reset is: {otp}'
            from_email = 'sreeragp10@gmail.com'  # Replace with your email address
            to_email = [email]
            send_mail(subject, message, from_email, to_email)

            # Redirect to the password reset page
            return redirect('UserAuthentication:reset')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email address.')

    return render(request, 'userAuth/email_confirm.html')




def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Verify the OTP

        if otp == request.session.get('otp'):
            # Update the user's password
            try:
                user = User.objects.get(email=request.session.get('email'))
                # Validate the new password
                if new_password == confirm_password and len(new_password) >= 8 and any(char.isupper() for char in new_password) and any(char in "!@#$%^&*()-_+={}[]:;\"'<>,.?/~" for char in new_password):
                    # Set the new password (make sure to hash it)
                    user.password = make_password(new_password)
                    user.save()
                    messages.success(request, 'Password updated successfully.')
                    return redirect('UserAuthentication:login')  # Redirect to the login page
                else:
                    messages.error(request, 'Invalid new password. Password must be at least 8 characters long, contain at least one uppercase letter, and one special character.')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
                return redirect('UserAuthentication:reset')  # Redirect back to the password reset page if user does not exist
        else:
            messages.error(request, 'Invalid OTP. Please enter the correct OTP.')

    return render(request, 'userAuth/password_reset.html')
