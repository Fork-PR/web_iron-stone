from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
import json

def index(request):
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
            #로그인 하는 함수
            login(request, user)
            #아이디와 비밀번호를 딕셔너리로 정리
            context = {
                'username' : username,
                'password' : password,
                'success': True,
                'message': 'Login successful',
            }
            #render에 context를 인자로 줘서 딕셔너리로 전달
            return JsonResponse(context)
        else:
            # 사용자가 존재하지 않을 때
            if not authenticate(username=username):
                context = {
                'success': False,
                'message': '해당 ID가 없습니다.',
                 }
                return JsonResponse(context, status=401)
            # 비밀번호가 틀렸을 때
            elif not authenticate(username=username, password=password):
                context = {
                'success': False,
                'message': '비밀번호가 틀렸습니다.',
                 }
                return JsonResponse(context, status=401)


def menuList(request):
    # 정적 파일 데이터 경로(없으면 None을 반환)
    data_path = finders.find('src/data.json')
    
    # 정적파일 데이터 불러오기
    with open(data_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    
    return JsonResponse(json_data, status=200)