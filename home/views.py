from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings # Important: Imports email settings

# Create your views here.
def homepage(request):
    return render(request, 'home/homepage.html')

def services(request):
    return render(request, 'home/services.html')

# UPDATED: Contact View with Email Logic
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # 1. Build the Email Content
        subject = f'New Inquiry from Maluva Vibes Website by {name}'
        
        # Format the email body clearly
        email_body = f"""
        Name: {name}
        Email: {email}
        
        --- Message ---
        {message}
        """

        try:
            # 2. Use Django's send_mail function
            send_mail(
                subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL, # Sender (configured in settings)
                ['malvernmamoche@gmail.com'], # Recipient (your email address)
                fail_silently=False,
            )
            # You can add a success message here if using Django messages framework
            return redirect('home') # Redirect back home after success
            
        except Exception as e:
            # For debugging errors (e.g., incorrect email settings)
            print(f"Error sending email: {e}") 
            # Optionally render the contact page again with an error message
            
    # For GET requests (just viewing the form) or if email sending fails
    return render(request, 'home/contact.html')

def quote(request):
    return render(request, 'home/quote.html')
