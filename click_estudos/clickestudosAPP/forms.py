from django import forms
from .models import Material, Avaliacao

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['titulo', 'descricao', 'arquivo']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do material',
                'required': True,
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descrição opcional',
            }),
            'arquivo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
        }

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['professor', 'texto', 'nota']
        widgets = {
            'professor': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
        }
