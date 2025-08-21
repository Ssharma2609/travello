from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','review_text','image']
        widgets = {
            'rating' : forms.NumberInput(attrs={'min': 1, 'max' : 5}),
            'review_text': forms.Textarea(attrs={'rows' : 3, 'placeholder' : 'Write your review...'}),
        }