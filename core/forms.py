from django import forms
from .models import Produto

class ProdutoModelForm(forms.ModelForm):
	class Meta:
		model = Produto

		#campos que serãoa apresentados no formulário
		fields = '__all__'