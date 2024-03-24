from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
import json

def index(request):
    if request.method == 'POST':
        # POST 요청이 오면 user_login 함수를 호출하여 로그인을 시도
        # 로그인 성공하면 성공 페이지로 이동
        # 로그인이 실패하면 index 페이지에서 에러문구 출력
        return user_login(request)
    else:
        # POST 요청이 아니면 index.html 보여주기
        return render(request, 'index.html')



# 회원가입 미구현
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True, 'message': 'User created successfully'})
#         else:
#             return JsonResponse({'success': False, 'errors': form.errors}, status=400)
#     else:
#         form = UserCreationForm()
#     return render(request, 'bobapps/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #redirect 함수를 통해 원하는 html 파일로 이동(.html안써도 됨, id 와 pw도 같이 보냄)
            return redirect('이동할 페이지', username=username, password=password)
        else:
            return render(request, 'index.html', {'message': 'Invalid credentials'}, status=401)

def menuList(request):
    # 정적 파일 데이터 경로(없으면 None을 반환)
    data_path = finders.find('src/data.json')
    
    # 정적파일 데이터 불러오기
    with open(data_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    
    return JsonResponse(json_data, status=200)