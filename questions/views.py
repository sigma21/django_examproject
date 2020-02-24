from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Account_Question
from accounts.models import Account
import datetime


def save_answer(request,question,existing_answer,user):
        if "choice" in request.POST: #db choice kayıt
            user_answer = request.POST['choice']           
            if (existing_answer):
                existing_answer.update(user_answer=user_answer)
            else:
                answer = Account_Question(question=question, user=user, user_answer=user_answer)
                answer.save()
        else:
            if (existing_answer): #unclick ekle
                existing_answer.update(user_answer="")
            else: #db null kayıt
                answer = Account_Question(question=question, user=user)
                answer.save()

def startexam(request):
    if request.user.is_authenticated:
        user = request.user

    Account.objects.filter(id=user.id).update(test_start_time=datetime.datetime.now())

    return redirect("exam/1")


def exam(request, question_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect("homepage")

    
    exam_start_time = get_object_or_404(Account, pk=user.id).test_start_time
    question = get_object_or_404(Question, pk=question_id)
    existing_answer = Account_Question.objects.filter(question=question, user=user)
    checked_answer=""
    if existing_answer:
        checked_answer = existing_answer[0].user_answer
    
    context={
        "question": question,
        "checked_answer": checked_answer,
        "time": int(exam_start_time.timestamp())
    }

    if request.method == "POST":
        if "next" in request.POST:
            save_answer(request,question,existing_answer,user)
            return redirect(f'/exam/{question.id+1}', context)
    
        if "prev" in request.POST:
            save_answer(request,question,existing_answer,user)
            return redirect(f'/exam/{question.id-1}', context)
        
        if "first" in request.POST:
            save_answer(request,question,existing_answer,user)
            return redirect('/exam/1', context)
        
        if "last" in request.POST:
            save_answer(request,question,existing_answer,user)
            return redirect('/exam/20', context)
       
        if "finish" in request.POST:
            save_answer(request,question,existing_answer,user)
            Account.objects.filter(id=user.id).update(test_completed=True)
            return redirect('result')
    else:
        return render(request, "exam.html", context)


def result(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect("homepage")

    answers = Account_Question.objects.filter(user=user)
    answer_list=[]
    for answer in answers:
        question_id = answer.question_id
        user_answer = answer.user_answer
        answer_list.append((question_id,user_answer))
    print(answer_list)

    x = []
    y = []

    for i in answers:
        x.append(i.question_id)
        y.append(i.user_answer)
    
    xy = dict(zip(x,y))
    print(xy)

    true_count=0
    for i in answers:
        if i.user_answer.lower() == i.question.answer.lower():
            true_count +=1
    print(true_count)

    context = {
        "true_count": true_count,
    }

    return render(request, "result.html", context)