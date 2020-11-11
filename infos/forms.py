from crispy_forms.layout import Field, Layout
from django import forms
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Your email')
    subject = forms.CharField(required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message',required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
