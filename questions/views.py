from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.datastructures import MultiValueDictKeyError
from .models import Question

def exam(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # questions = Question.objects.order_by("id")

    # paginator = Paginator(questions, 1)
    # page = request.GET.get("page")
    # paged_questions = paginator.get_page(page)

    context={
        # "questions" : paged_questions
        "question": question
    }

    if request.method == "POST" and "choice" in request.POST:
        kullanıcı_cevabı = request.POST['choice']
        print(kullanıcı_cevabı)
        #db kayıt komutu gir
    else:
        print("boş")
        #db kayıt komutu gir (null olarak)

    return render(request, 'exam.html', context)


def question(request):
    # if request.method == "POST" and "choice" in request.POST:
    #     kullanıcı_cevabı = request.POST['choice']
    #     print(kullanıcı_cevabı)
    #     #db kayıt komutu gir
    # else:
    #     print("boş")
    #     #db kayıt komutu gir (null olarak)

    # return render(request, 'exam.html')
    return
