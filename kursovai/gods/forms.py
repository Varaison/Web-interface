from django.forms import ModelForm

from .models import Gs


class GgForm(ModelForm):
    class Meta:
        model = Gs
        fields = ('title', 'content', 'price', 'rubric')
