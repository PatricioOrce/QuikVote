

from ..manager.models import Option
from django import forms
from forms import inlineformset_factory



class CreatePollForm(forms.ModelForm):
    class Meta:
        model: Option 
    pollDescription = forms.CharField(label="Description:", required=True)

    
