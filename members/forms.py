from django import forms

from members.models import Members

# creating a django form

# class MembersForm(forms.Form):
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput)
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput)

class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = "__all__"
        