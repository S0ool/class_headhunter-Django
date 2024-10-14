from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .decorators import IsOwnerResumeOrVacancy, IsStaff, IsOwnerResumeOrStaff
from .forms import ResumeForm, VacancyForm
from .models import Vacancy, Resume, Request


class StartPageView(TemplateView):
    template_name = 'app/start_page.html'


@method_decorator(login_required, name='dispatch')
class VacancyListView(ListView):
    model = Vacancy
    template_name = 'app/vacancy_list.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        user_requests = Request.objects.filter(resume__user=self.request.user).values_list('vacancy_id', flat=True)
        vacancies = Vacancy.objects.exclude(id__in=user_requests)

        search_query = self.request.GET.get('search', '')
        if search_query:
            vacancies = vacancies.filter(Q(title__icontains=search_query) |
                                         Q(description__icontains=search_query) |
                                         Q(skills__name__icontains=search_query)).distinct()
        return vacancies

@method_decorator(login_required, name='dispatch')
class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'app/vacancy_detail.html'
    pk_url_kwarg = 'vacancy_id'

@method_decorator(login_required, name='dispatch')
class VacancyCreateView(CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'app/vacancy_form.html'

    def form_valid(self, form):
        vacancy = form.save(commit=False)
        vacancy.created_by = self.request.user
        vacancy.save()
        form.save_m2m()
        return redirect('vacancy_detail', vacancy_id=vacancy.id)

@method_decorator(IsOwnerResumeOrVacancy, name='dispatch')
class VacancyUpdateView(UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'app/vacancy_form.html'
    pk_url_kwarg = 'vacancy_id'

    def form_valid(self, form):
        form.save()
        return redirect('vacancy_list')

@method_decorator(IsOwnerResumeOrVacancy, name='dispatch')
class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'app/vacancy_confirm_delete.html'
    pk_url_kwarg = 'vacancy_id'

    def get_success_url(self):
        return reverse_lazy('vacancy_list')

@method_decorator(IsStaff, name='dispatch')
class ResumeListView(ListView):
    model = Resume
    template_name = 'app/resume_list.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        resumes = Resume.objects.all()
        search_query = self.request.GET.get('search', '')
        if search_query:
            resumes = resumes.filter(Q(name__icontains=search_query) |
                                     Q(last_name__icontains=search_query) |
                                     Q(skills__name__icontains=search_query)).distinct()
        return resumes

@method_decorator(IsOwnerResumeOrStaff, name='dispatch')
class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'app/resume_detail.html'
    pk_url_kwarg = 'resume_id'

@method_decorator(IsStaff, name='dispatch')
class ResumeCreateView(CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'app/resume_form.html'

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.user = self.request.user
        resume.save()
        form.save_m2m()
        return redirect('profile_page')

@method_decorator(IsOwnerResumeOrVacancy, name='dispatch')
class ResumeUpdateView(UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'app/resume_form.html'
    pk_url_kwarg = 'resume_id'

    def form_valid(self, form):
        form.save()
        return redirect('profile_page')

@method_decorator(IsOwnerResumeOrVacancy, name='dispatch')
class ResumeDeleteView(DeleteView):
    model = Resume
    template_name = 'app/resume_confirm_delete.html'
    pk_url_kwarg = 'resume_id'

    def get_success_url(self):
        return reverse_lazy('profile_page')
