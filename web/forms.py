from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(label="关键字", max_length=50, widget=forms.TextInput(
        attrs={'id': 'search-input', 'class': 'search-input', 'tabIndex': '1', 'autocomplete': "off"}))
