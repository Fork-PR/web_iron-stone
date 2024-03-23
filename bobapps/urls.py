from django.urls import path
from bobapps import views

app_name = 'bobapps'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('menuList', views.menuList, name='menuList')
    # other urls...
]