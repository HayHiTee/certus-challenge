from django.forms import ModelForm
from .models import PasswordVault

# Create the form class.
class PasswordVaultForm(ModelForm):
	class Meta:
		model = PasswordVault
		fields = [
        	'include_symbols', 'include_numbers', 'include_lower', 'include_upper', 'exclude_similar', 'exclude_char','integer_value'
        ]


class PasswordVaultPostForm(ModelForm):
        class Meta:
                labels = {
                'can_store': ('Do you want to save the password to the vault?'),
                'website': ('This password is stored for?'),
                'password': ('Unique generated password is'),
                'general_info': ('Add more details password saved'),
                }