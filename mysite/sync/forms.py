from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name','required':'required'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Age','required':'required'}))
    siblings = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'yes/no','required':'required'}))
    exposures = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Exposures'}))
    mutations = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mutations'}))

    def clean_siblings(self):
        siblings = self.cleaned_data['siblings']
        sibling_lw = siblings.lower()
        if sibling_lw == 'yes' or sibling_lw == 'no':
            return sibling_lw
        else:
            raise forms.ValidationError("Please enter yes or no")

    class Meta:
        model = Participant
        fields = ('name', 'age', 'siblings', 'exposures', 'mutations',)
