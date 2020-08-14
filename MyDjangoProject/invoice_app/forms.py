from django.forms import ModelForm
from invoice_app.models import *


class CustomerForm(ModelForm):
    class Meta:
        model = CustomerModel
        fields = "__all__"