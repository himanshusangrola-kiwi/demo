from django import forms
from .models import CollegeModel

 
# creating a form
class CollegeForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = CollegeModel
 
        # specify fields to be used
        fields = '__all__'