from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

        
"""
Django Form이라고 한다.
Django Form은 사실 2개의 폼으로 구분할 수 있는데,
forms.Form을 상속받으면 폼, forms.ModelForm을 상속받으면 모델 폼이라 부른다.
form.ModelForm을 상속받아 모델 폼을 만들었다.
모델 폼은 모델과 연결된 폼이며, 모델폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있다.
내부 클래스로 선언한 Meta 클래스가 있어야하며,
Meta클래스에는 모델 폼이 사용할 모델과 모델의 필드를 적어야한다.
QuestionForm 클래스는 Question 모델과 연결이 되어있으며 
필드로 subject, content를 사용한다고 정의했다. 
"""


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }