from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

#from django.contrib.auth.views import LoginView
#login.html을 registration폴더 밑이 아니라 templates폴더 바로 밑에 저장하고 싶은 경우 사용

def signup(request):
    regi_form = UserCreationForm()
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')

    return render(request, 'signup.html', {'regi_form':regi_form})


#<오버라이딩>
# class MyLoginView(LoginView):         -> MyLoginView가 LoginView를 상속
#     template_name = 'login.html'      -> registration/login.html이던 것을 그냥 login.html로 바꿔주면 login.html을 templates폴더 바로 밑에 둘 수 있게 됨

#urls.py에서 from .views import MyLoginView를 써주고, path에서도 LoginView를 쓰는 것이 아닌 MyLoginView를 써야 됨