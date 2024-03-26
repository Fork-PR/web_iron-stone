from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add custom fields if needed
    pass

class Menu(models.Model):
    date = models.DateField()
    menu_course_type = models.CharField(max_length=3)
    main_dish = models.CharField(max_length=10)
    # 서브메뉴가 여러 개일 수 있으므로 ManyToManyField를 사용
    sub_menus = models.ManyToManyField('SubMenu')

class SubMenu(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name