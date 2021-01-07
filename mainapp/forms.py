from django.forms import ModelForm
from .models import Category
class OrderForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'