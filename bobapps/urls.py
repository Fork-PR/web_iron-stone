from django.urls import path
from bobapps import views

app_name = 'bobapps'
urlpatterns = [
    #회원가입 미구현
    # path('signup/', views.signup, name='signup'),
    #index에서 같이 사용할 예정
    path('user_login/', views.user_login, name='user_login'),
    path('menuList/', views.menuList, name='menuList'),
    path('', views.index, name='index'),
    path('login_page/', views.login_page, name='login_page')
    # other urls...
]