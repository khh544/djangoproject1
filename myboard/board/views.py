from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import AnswerForm, CommentForm, QuestionForm
from .models import Answer, Question, Comment

def index(request):
    """
    Question 질문목록 추출
    """

    # 사용자가 요청한 페이지 값 가져오기
    page = request.GET.get("page", 1)

    # 전체 목록 추출
    question_lists = Question.objects.order_by("-created_at")

    # 전체 목록 안에서 사용자가 요청한 페이지에 대한 목록만 전송
    paginator = Paginator(question_lists, 10)
    question_list = paginator.get_page(page)

    return render(request, "board/question_list.html",{"question_list":question_list})


def question_detail(request,question_id):
    """
    Question 상세 내용 추출
    """
    question = get_object_or_404(Question, id=question_id)
    return render(request, "board/question_detail.html",{"question":question})

@login_required(login_url='users:login')
def question_create(request):
    """
    Question 등록
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()

            return redirect("board:index")
    else:
        form = QuestionForm()

    return render(request, "board/question_create.html",{"form":form})

@login_required(login_url='users:login')
def question_modify(request,question_id):
    """
    Question 수정
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            # 성공시 detail 
            return redirect("board:question_detail",question_id=question_id)
    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_modify.html", {"form":form})

@login_required(login_url='users:login')
def question_delete(request, question_id):
    """
    Question 삭제
    """
    question = get_object_or_404(Question, pk=question_id)

    question.delete()
    # 성공시 list 보여주기
    return redirect("board:index")




@login_required(login_url='users:login')
def answer_create(request,question_id):
    """
    Answer 등록
    """
    question = get_object_or_404(Question,id=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            # 성공시 detail
            return redirect("board:question_detail",question_id=question_id)
    else:
        form = AnswerForm()
        
    return render(request, "board/question_detail.html",{"form":form,"question":question})

@login_required(login_url='users:login')
def answer_modify(request,answer_id):

    answer = get_object_or_404(Answer, pk=answer_id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.save()
            return redirect("board:question_detail", question_id = answer.question_id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, "board/answer_modify.html",{"form":form})

@login_required(login_url='users:login')
def answer_delete(request,answer_id):
    
    answer = get_object_or_404(Answer,pk=answer_id)

    answer.delete()
    return redirect("board:index")



def comment_create_question(request,question_id):
    """
    질문 댓글 등록
    """

    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.question = question
            comment.save()
            return redirect("board:question_detail",question_id=question_id)
    else:
        form = CommentForm()
    return render(request, "board/comment_create.html",{"form":form})

def comment_modify_question(request,comment_id):
    """
    질문 댓글 수정 => 템플릿은 comment_create 사용
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect("board:question_detail",question_id=comment.question.id)
        else:
            form = CommentForm(instance=comment)
        return render(request, "board/comment_create.html",{"form":form})