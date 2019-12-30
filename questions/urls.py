from django.urls import path
from . import views


urlpatterns = [
    path('exam/<int:question_id>', views.exam, name="exam"),
    path('exam/result', views.result, name="result"),

]