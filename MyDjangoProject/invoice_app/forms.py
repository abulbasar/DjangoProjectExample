from django.forms import ModelForm, ValidationError
from invoice_app.models import *


class CustomerForm(ModelForm):
    class Meta:
        model = CustomerModel
        fields = "__all__"
        #fields = ["name", "tax_id", "status"]

    def clean_tax_id(self, *args, **kwargs):
        tax_id = self.cleaned_data.get("tax_id")
        if not tax_id.startswith("000"):
            raise ValidationError("Invalid tax id. It must start with 000")
        return tax_id

    def clean(self):
        status = self.cleaned_data.get("status")
        if status == "Inactive":
            raise ValidationError("You cannot update an inactive account")