from django import forms
from .models import *



class RoastForm(forms.ModelForm):
    class Meta:
        model = Roast
        fields = "__all__"

class RoastForm(forms.ModelForm):
    class Meta:
        model = Roast
        fields = "__all__"

class SyrupForm(forms.ModelForm):
    class Meta:
        model = Syrup
        fields = "__all__"

class PowderForm(forms.ModelForm):
    class Meta:
        model = Powder
        fields = "__all__"

class CoffeForm(forms.ModelForm):
    class Meta:
        model = Coffe
        fields = "__all__"
