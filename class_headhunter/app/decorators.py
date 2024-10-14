from django.shortcuts import redirect


def IsOwnerResumeOrVacancy(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.is_authenticated:
            if kwargs.get('vacancy_id'):
                id_field = 'vacancy_id'
            else:
                id_field = 'resume_id'

            if request.user.id != kwargs.get(id_field):
                return redirect('start_page')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def IsStaff(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('start_page')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def IsOwnerResumeOrStaff(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff and request.user.id != kwargs['pk']:
            return redirect('start_page')
        return view_func(request, *args, **kwargs)
    return _wrapped_view