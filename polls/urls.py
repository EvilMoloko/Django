from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('create_form', views.create_form, name='create_form'),
    path('success_saved', views.success_saved, name='success_saved'),
    path('<int:pk>/question_update/', views.QuestionUpdateView.as_view(), name='question_update'),
    path('<int:pk>/question_delete', views.QuestionDeleteView.as_view(), name='question_delete'),
    path('create_choice', views.ChoiceCreateView, name='create_choice'),
    path('<int:pk>/update_choice/', views.ChoiceUpdateView.as_view(), name='update_choice'),
    path('<int:pk>/delete_choice', views.ChoiceDeleteView.as_view(), name='delete_choice'),
    path('question_new', views.QuestionCreateView.as_view(), name='question_new'),

]