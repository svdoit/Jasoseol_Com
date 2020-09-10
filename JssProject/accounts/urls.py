from django.urls import path
from .views import signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', signup, name = "signup"),
    path('login/', LoginView.as_view(), name = "login"), 
    path('logout/', LogoutView.as_view(), name = "logout"), 
    #LoginView함수 이용. class를 url에서 직접 실행하고 싶으면 .as_view()를 같이 써줘야 함. class는 함수처럼 바로바로 실행이 안 되고, instance를 생성해줘야 하기 때문
    #LoginView이용하려면 registration폴더를 만들고 그 안에 login.html파일이 있어야 함. 둘 다 만들어줘야 됨

]