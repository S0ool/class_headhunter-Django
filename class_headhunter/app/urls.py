from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name='start_page'),

    path('vacancies/', views.VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:vacancy_id>/', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/create/', views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:vacancy_id>/', views.VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/delete/<int:vacancy_id>/', views.VacancyDeleteView.as_view(), name='vacancy_delete'),

    path('resumes/', views.ResumeListView.as_view(), name='resume_list'),
    path('resumes/<int:resume_id>/', views.ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/create/', views.ResumeCreateView.as_view(), name='resume_create'),
    path('resume/update/<int:resume_id>/', views.ResumeUpdateView.as_view(), name='resume_update'),
    path('resume/delete/<int:resume_id>/', views.ResumeDeleteView.as_view(), name='resume_delete'),
]
