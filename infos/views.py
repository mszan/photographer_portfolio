from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import About

class AboutView(TemplateView):
    model = About
    # template_name = 'infos/about.html'

    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'infos/about.html', context)

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(self.request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['dmszanowski@icloud.pl'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message sent.')
            return redirect('infos-about')
