from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.NumberInput(attrs={
        'class': 'form-control text-center me-3',
        'id': 'inputQuantity',
        'type': 'num',
        'value': '1',
        'size': '2',
        'style': 'width: 55px',
    }))
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
