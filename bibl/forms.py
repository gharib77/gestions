from django import forms
from bibl.models import Personne,Grade

class FormPers(forms.ModelForm):
    
    class Meta:
        model = Personne
        fields = '__all__'
