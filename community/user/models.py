from django.db import models

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionManager

# 회원가입 - 이메일 , 이름 , 전화번호 , 비밀번호 필드만 사용 한다고 할때

class AccountManager(BaseUserManager):
    pass


# User class 생성
class CustomUser(AbstractBaseUser, PermissionManager):
    pass