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
        context['page_title'] = 'bio'
        context['bio'] = Bio.objects.first()
        context['contact_form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(self.request.POST)
        if contact_form.is_valid():
            from_email = contact_form.cleaned_data['from_email']
            to_email = Bio.objects.first().mail_to
            subject = f"From: {from_email}, Subject: {contact_form.cleaned_data['subject']}"
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [to_email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message sent, I will text you back shortly.')
            return redirect('infos-bio')
