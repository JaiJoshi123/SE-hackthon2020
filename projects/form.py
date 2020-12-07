from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Title of your project"})
                            )
    keywords = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Keywords!",
                "rows": 10,
                "cols": 60
            }
        )
    )
    code = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write Your Code Here",
                "rows": 100,
                "cols": 60
            }
        )
    )
    author = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "placeholder": "Enter your UID here",
            }
        )
    )

    class Meta:
        model = Project
        fields = [
            'title',
            'keywords',
            'code',
            'author',
            'file',
        ]
