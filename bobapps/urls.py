from django.urls import path
from bobapps import views

app_name = 'bobapps'
urlpatterns = [
    #회원가입 미구현
    # path('signup/', views.signup, name='signup'),
    #index에서 같이 사용할 예정
    # path('login/', views.user_login, name='login'),
    # path('menuList', views.menuList, name='menuList'),
    path('', views.index, name='index'),
    # other urls...
]