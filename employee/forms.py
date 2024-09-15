from django import forms

from .models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'style': 'width: 400px'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Address',
                'style': 'width: 400px'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': "Start with '0', then add remaining 10 digits",
                'style': 'width: 400px'
            }),
            'salary': forms.NumberInput(attrs={
                'placeholder': 'Salary',
                'style': 'width: 400px'
            }),
            'designation': forms.TextInput(attrs={
                'placeholder': 'Designation',
                'style': 'width: 400px'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Short Description',
                'style': 'width: 400px; height: 150px;'
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
        fields = ['name', 'address', 'phone', 'description', 'salary']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'style': 'width: 400px'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Address',
                'style': 'width: 400px'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': "Start with '0', then add remaining 10 digits",
                'style': 'width: 400px'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Short Description',
                'style': 'width: 400px; height: 150px;'
            }),
            'salary': forms.NumberInput(attrs={
                'placeholder': 'Salary',
                'style': 'width: 400px'
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
    
