from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .form import SignUpForm, ContactForm
# Create your views here.

def home(request):
    title="Welcome"
    #if request.user.is_authenticated():
    #    title= "Hello myworld %s "%(request.user)
    form = SignUpForm(request.POST or None)
    #print request
    #if request.method == "POST":
    #    print request.POST
    context ={
        "template_title": title,
        "form" : form
    }
    if form.is_valid():
        instance=form.save(commit=False) # commit=False means Don't save data
        #if not instance.full_name:
        #    instance.full_name = "New user"
        #print instance
        #print instance.email
        #print instance.timestamp
        full_name=form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name=full_name
        instance.save()
        context = {
            "template_title": "Thank you"
        }

    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print form.cleaned_data
        form_email=form.cleaned_data.get('email')
        form_message =form.cleaned_data.get('message')
        form_full_name=form.cleaned_data.get('full_name')
        #print email, message, full_name
        subject="contact site"
        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email, "prathapn054@gmail.com"]
        contact_message="%s: %s via %s"%(form_full_name, form_message, form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True)
    context= {
        "form" : form,
    }
    return render(request, "form.html", context)