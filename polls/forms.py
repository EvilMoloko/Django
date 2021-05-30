from django import forms


class CreateForm(forms.Form):
    question_name = forms.CharField(label="Название нового вопроса", max_length=100)