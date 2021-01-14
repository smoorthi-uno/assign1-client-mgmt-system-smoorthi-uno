from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def send_mail(request):
    # add send e-mail confirmation
    # set up the subject, message, and user’s email address

    subject = 'Reset CMS Password'
    message = 'You have put a password change request. Please use the link to set a new password.'

    user = request.user  # request was passed to the method as a parameter for the view
    user_email = user.email  # pull user’s email out of the user record

    # try to send the e-mail – note you can send to multiple users – this just sends to one user.
    try:
        send_mail(subject, message, 'mswproject.uno@gmail.com', [user_email])
        sent = True
    except:
        print("Error sending e-mail")
