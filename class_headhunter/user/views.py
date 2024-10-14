from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm


def register(request):
    if request.user.is_authenticated:
        return redirect('start_page')
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            return redirect('start_page')

    form = UserForm
    ctx = {'forms': form}
    return render(request, 'user/index.html', ctx)


def signIn(request):
    if request.user.is_authenticated:
        return redirect('start_page')

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                print(f"Welcome {username}!")
                login(request, user)
                return redirect('start_page')
            else:
                print("username or password error")
    form = ProfileForm()
    ctx = {'form': form}
    return render(request, 'user/signIn.html', ctx)


@login_required
def profile(request):

    if request.user.resume:
        resume = request.user.resume
    else:
        resume = ""
    if request.user.is_staff:
        vacancies = request.user.vacancy.all()
        print(1)
    else:
        vacancies = ''
        print(2)

    print(vacancies)
    ctx = {
        'user': request.user,
        'resume': resume,
        'vacancies': vacancies
    }
    return render(request, 'user/profile.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('start_page')