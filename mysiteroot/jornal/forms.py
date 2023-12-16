from django import forms


class FormularioCadastro(forms.Form):
    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={"placeholder": "Nome"}))
    sobrenome = forms.CharField(label="Sobrenome", widget=forms.TextInput(attrs={"placeholder": "Sobrenome"}))
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={"placeholder": "Email"}))
    senha = forms.CharField(label="Senha",widget=forms.PasswordInput(attrs={"placeholder": "Senha"}))

class FormularioNoticia(forms.Form):
    titulo = forms.CharField(max_length=60)
    texto_noticia = forms.CharField(widget=forms.Textarea)  # Use CharField para texto longo
    data_noticia = forms.DateField()