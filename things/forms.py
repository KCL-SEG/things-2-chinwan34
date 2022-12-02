"""Forms of the project."""
from django import forms

# Create your forms here.
class ThingForm(forms.Form):
    fields = ["name", "description", "quantity"]
    widget = {
        "description": forms.Textarea(),
        "quantity": forms.NumberInput()
    }