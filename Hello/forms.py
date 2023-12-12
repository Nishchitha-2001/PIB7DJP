from django import forms
# class studentform(forms.Form):
#     student_ID = forms.IntegerField()
#     student_name = forms.CharField(max_length=50)
#     course = forms.CharField(max_length=30)
#     jdate = forms.DateField()

from Hello.models import students
from django.forms import ModelForm
from Hello.models import students
class studentform(ModelForm):
    class Meta:
        model=students
        fields= ['student_ID','student_name','course','jdate']


