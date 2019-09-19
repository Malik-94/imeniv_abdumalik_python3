from django import forms
from django.forms import widgets
from webapp.models import status_choices


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Title')
    created_at = forms.DateField(label='created_at',)
    text = forms.CharField(max_length=3000, required=False, label='Text',
                           widget=widgets.Textarea)
    category = forms.ChoiceField(choices=status_choices, required=False, label='Category')
