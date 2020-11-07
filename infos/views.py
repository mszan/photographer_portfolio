from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import Bio


class BioView(TemplateView):
    model = Bio
    template_name = 'infos/bio.html'

    def get_context_data(self, **kwargs):
        context = super(BioView, self).get_context_data(**kwargs)
        context['bio'] = Bio.objects.first()
        context['contact_form'] = ContactForm()
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(self.request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['jouissance3000@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message sent.')
            return redirect('infos-bio')
