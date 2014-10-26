from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control requiredField', 'id': 'contact-name',
                                                           'name': 'contactName', 'placeholder': 'Tu Nombre',
                                                           'data-error-empty': 'Por favor, escribe tu nombre'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'contact-mail', 'name': 'email', 'placeholder': 'Tu Email',
                                                           'class': 'form-control requiredFiled',
                                                           'data-error-empty': 'Por favor, escribe tu email',
                                                           'data-error-invalid': 'Email Invalido'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'id': 'contact-message', 'name':'comments',
                                                       'placeholder': 'Escribe texto aqui', 'class': 'form-control requiredField',
                                                       'rows': '8', 'data-error-empty': 'Venga, escribenos algo primero :)'}))

