from django.forms import ModelForm
from .models import ContactForm

class FormSerializer(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'