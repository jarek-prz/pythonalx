from django.urls import path
from mysite.views import funkcja_widoku, funkcja_sumy, funkcja_mnozenia
from polls.views import index, questions_list

urlpatterns = [
    path("", index, name="index"),
    path('hello/<name>', funkcja_widoku),
    path('suma/<a>/<b>', funkcja_sumy),
    path('iloczyn/<a>/<b>', funkcja_mnozenia),
    path('questions', questions_list, name = "question-list"),
]


