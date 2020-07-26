from django.urls import path

from . import views

app_name = 'polls'
# urlpatterns = [
#     path('', views_extended.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views_extended.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views_extended.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views_extended.vote, name='vote'),
# ]

# pk as in primary key
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]