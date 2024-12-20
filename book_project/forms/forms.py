from django import forms


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget={})
    author = forms.CharField(label='Author', max_length=100)
    price = forms.IntegerField(max_value=1000, min_value=100)
