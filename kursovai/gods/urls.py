from django.urls import path
from .views import *    # import всех методов, которые были созданы во вкладке views.py

urlpatterns = [             # Запуск работы методов из папки views.py
    path('', index, name='index'),        # Метод index, открывающий страницу gods/
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', GgCreateView.as_view(), name='add'),
]
