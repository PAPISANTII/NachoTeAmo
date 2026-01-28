from django import forms

class ChatForm(forms.Form):
    prompt = forms.CharField(
        label="Tu mensaje para Gemini",
        widget=forms.TextInput(attrs={
            "class": "w-full p-3 border rounded-lg",
            "placeholder": "Escribe algo como '¿Qué es Django?'"
        })
    )
