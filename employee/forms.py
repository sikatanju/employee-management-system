from django import forms

from .models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Address',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': "Start with '0',then 10 digits",
            }),
            'salary': forms.NumberInput(attrs={
                'placeholder': 'Salary',
            }),
            'designation': forms.TextInput(attrs={
                'placeholder': 'Designation',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Short Description',
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.startswith('0'):
            raise forms.ValidationError("Phone number must start with '0'.")
    
        phone_num = phone[1:]

        if not phone_num.isdigit():
            raise forms.ValidationError("Phone number must contain only digits after '0'.")
        
        if len(phone_num) != 10:
            raise forms.ValidationError("Phone number must have exactly 10 digits after '0'.")

        return phone
    
class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone', 'description']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.startswith('0'):
            raise forms.ValidationError("Phone number must start with '0'.")
    
        phone_num = phone[1:]

        if not phone_num.isdigit():
            raise forms.ValidationError("Phone number must contain only digits after '0'.")
        
        if len(phone_num) != 10:
            raise forms.ValidationError("Phone number must have exactly 10 digits after '0'.")

        return phone