from django import forms
from .models import Resume, Vacancy

class ResumeForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Resume
        fields = '__all__'
        exclude =  ('user',)

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        exclude = ['created_by', 'created_at']
