from django import forms


class Zipform(forms.Form):
    image=forms.ImageField()
    font=forms.CharField()
    size=forms.CharField()
    colour=forms.CharField()
    datacsv=forms.FileField()
    position=forms.CharField()