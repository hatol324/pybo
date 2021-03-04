from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Answer, Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    """
    pybo 목록 출력 
    render 함수는 context에 있는 Question 모델 데이터 question_list를 
    pybo/question_list.html 파일에 적용하여 HTML 코드로 변환한다. 
    그리고 장고에서는 이런 파일(pybo/question_list.html)을 템플릿이라 부른다. 
    템플릿은 장고의 태그를 추가로 사용할 수 있는 HTML 파일이라 생각하면 된다. 
    템플릿에 대해서는 바로 다음 실습 과정을 통해 자연스럽게 알아보겠다.
    """
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    return render(request, 'pybo/question_list.html', context)

# def question_create(request):
    # return HttpResponse("안녕하세요 request 입니다.")

def detail(request, question_id):
    """
    pybo 내용출력
    get_object_or_404 함수는 모델의 기본키를 이용하여 모델 객체 한 건을 반환
    pk에 해당하는 건이 없으면 오류 대신 404페이지를 반환 
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)



    # return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

    