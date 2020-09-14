from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required #login된 유저에게만 보여줄 곳에 붙여주면 됨
# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})

def my_index(request):
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_jss':my_jss})

#objects들을 가져올 수 있는 방법들
# 모델.objects.all()
# 모델.objects.get()
# 모델.objects.filter()

@login_required(login_url='/login/') #login된 유저에게만 보여줄 곳에 붙여주면 됨
def create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False) #글 작성자가 자동으로 입력되게 하는 코드
            #save() 안에 commit=False를 넣어주게 되면 잠시 저장이 되기 전에 오브젝트가 생성이나 업데이트되기 전에 저장을 지연시키고 그 사이에 어떤 것들을 해줄 수가 있음
            temp_form.author = request.user #글 작성자가 자동으로 입력되게 하는 코드
            temp_form.save() #글 작성자가 자동으로 입력되게 하는 코드
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})

def detail(request, jss_id):
    # try:
    #     my_jss = Jasoseol.objects.get(pk=jss_id)
    # except:
    #     raise Http404
    # 위와 같이 쓸 수 도 있지만 바로 밑 줄 처럼 쓸 수 도 있음

    my_jss = get_object_or_404(Jasoseol, pk=jss_id)

    return render(request, 'detail.html', {'my_jss':my_jss})
    
def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author: #user가 해당 글을 작성한 작성자인지 확인
        my_jss.delete() #맞다면 글 삭제 처리 가능
        return redirect('index')
    # 삭제 버튼이 없더라도 url로 delete를 입력해서 다른 사용자가 작성한 글을 삭제시키는 일이 없도록 하기 위함   
    raise PermissionDenied #해당 글의 작성자가 아니므로 거부

def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    return render(request, 'create.html', {'jss_form':jss_form})