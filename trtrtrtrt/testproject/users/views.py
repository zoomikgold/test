from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .UserForm import UserRegisterForm

#
# def registr(request):
#     a = 509
#     print("sadasddsa")
#     print(request.method)
#     if request.method == 'POST':
#         print(request.POST)
#         form = UserRegisterForm(request.POST)
#         print(form.is_valid())
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
#             return redirect(request, 'users/profile.html')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/registr.html', {'form': form})



def registr(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registr.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
