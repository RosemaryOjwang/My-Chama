from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserRegister
from accounts.models import Group, Add_Members

#Create form

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserRegister
        fields = "__all__"

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class Group_Form(forms.ModelForm):
    class Meta:
        model =Group
        fields = ('groupName',)

    
class Add_MembersForm(forms.ModelForm):
    class Meta:
        model = Add_Members
        fields = ('groupName','thumbnail', 'memberName', 'member_contact', 'occupation', 'available',)

    




        