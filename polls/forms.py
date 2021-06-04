from django.forms import ModelForm, TextInput, Textarea, DateTimeField
from .models import Question, Choice
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CreateForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'publication_date']

        widgets = {
            "question_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос'
            }),
        }

class CreateChoice(ModelForm):
     class Meta:
        model = Choice
        fields = ['choice_text', 'question']

        widgets = {
            "choice_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант'
            }),
        }