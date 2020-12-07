from .models import Question
from .models import Stud_Ans
from django import forms


class New_Question_Form(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Title Of The Question"})
    )
    ques = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Question",
                "rows": 20,
                "cols": 120
            }
        )
    )

    class Meta:
        model = Question
        fields = [
            'title',
            'ques'
        ]


class Answer(forms.ModelForm):
    answer = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Type Your Answer Here",
                "cols": 300
            }
        )
    )

    class Meta:
        model = Stud_Ans
        fields = [
            'answer',
        ]


class Upvote(forms.ModelForm):
    class Meta:
        model = Stud_Ans
        fields = [
            # 'upvote'
        ]
