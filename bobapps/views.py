from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from .models import Menu, SubMenu
from datetime import datetime

def index(request):
        return render(request, 'index.html')

def login_page(request):
        return render(request, 'login_page.html')



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
            if not CustomUser.objects.filter(username=username).exists():
                context = {
                'success': False,
                'message': '해당 ID가 없습니다.',
                 }

                return JsonResponse(context, status=401)
            # 비밀번호가 틀렸을 때
            else:
                context = {
                'success': False,
                'message': '비밀번호가 틀렸습니다.',
                 }

                return JsonResponse(context, status=401)
    else:
        return render(request, 'index.html')



def menuList(request):
    # 요청에서 날짜를 확인
    requested_date = request.GET.get('date')
    # 가져온 날짜를 datetime 객체로 변환
    # 첫번 째 인자로 'YYYY-MM-DD' 형태의 데이터가 입력
    # 두번 째 인자로 문자열 형식을 지정 '%Y-%m-%d'='YYYY-MM-DD'
    # 시간은 사용하지 않기 위해서 .date()사용
    requested_datetime = datetime.strptime(requested_date, '%Y-%m-%d').date()
    
    # 해낭 날짜에 메뉴가 있는지 DB 탐색을 시도
    try:
        # 요청된 날짜에 해당하는 메뉴를 데이터베이스에서 가져옴
        # 실패 시 excpet로 이동
        menu = Menu.objects.get(date=requested_datetime)
        
        # 메뉴 데이터를 JSON 형식으로 변환하여 반환
        context = {
            'date': menu.date,
            'menu_course_type': menu.menu_course_type,
            'main_dish': menu.main_dish,
            'sub_menus': [submenu.name for submenu in menu.sub_menus.all()],  # 서브 메뉴들을 리스트로 가져옴
            'success': True
        }
        
        # JSON 응답 반환
        return JsonResponse(context, status=200)
    # 해낭 날짜에 메뉴가 없다면 Menu.DoesNotExist 클래스로 예외 처리
    # 메시지와 함께 에러 코드를 반환
    except Menu.DoesNotExist:
        context = {
            'message' : '해당 날짜에 메뉴가 없습니다',
            'success' : False


        }
        # 요청된 날짜에 해당하는 메뉴가 없는 경우, 404 에러와 함께 메시지 반환
        return JsonResponse(context, status=404)




def save_menu(request):
    if request.method == 'POST':
        # POST 요청을 받았을 때 데이터 처리
        date = request.POST.get('date')
        menu_type = request.POST.get('menu_type')
        main_dish = request.POST.get('main_dish')
        # 서브 메뉴는 여러 개일 수 있으므로 리스트로 받음
        sub_menus = request.POST.getlist('sub_menus')

        # Menu 객체 생성
        #created는 서브메뉴가 생성 되었는지 여부를 나타낸다.(bool값)
        menu, create = Menu.objects.get_or_create(date=date, menu_type=menu_type, main_dish=main_dish)

        # 서브 메뉴를 추가
        for sub_menu_name in sub_menus:
            sub_menu = SubMenu.objects.get_or_create(name=sub_menu_name)
            menu.sub_menus.add(sub_menu)
        if create==True:
            return render(request, 'menu_form.html', {'message': '메뉴가 추가되었습니다.'})
        else:
            return render(request, 'menu_form.html', {'message': '메뉴 추가에 실패했습니다.'})
    else:
        return render(request, 'menu_form.html')