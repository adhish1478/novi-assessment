from django import forms
from .models import Airport


# Form to add airport into tree
class AirportForm(forms.ModelForm):

    class Meta:
        model = Airport
        fields = ["airport_code", "duration", "parent", "position"]

    # Custom validation
    def clean(self):
        cleaned = super().clean()
        parent = cleaned.get("parent")
        position = cleaned.get("position")

        # If parent exists, position MUST be L or R
        if parent and position not in ("L", "R"):
            raise forms.ValidationError(
                "Position must be Left or Right if parent is selected"
            )

        # Root node should not have position
        if not parent:
            cleaned['position'] = None

        return cleaned


# Form for Question 1
class NthNodeForm(forms.Form):
    start_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all()
    )
    direction = forms.ChoiceField(
        choices=Airport.POSITION_CHOICES
    )
    n = forms.IntegerField(min_value=1)


# Form for Question 3
class BetweenAirportForm(forms.Form):
    airport_a = forms.ModelChoiceField(
        queryset=Airport.objects.all()
    )
    airport_b = forms.ModelChoiceField(
        queryset=Airport.objects.all()
    )
