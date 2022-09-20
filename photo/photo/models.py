from pydoc import describe
from django.db import models

#데이터 베이스 작업
# 테이블 == 클래스로 작업

# photo
# 컬럼 : pk, 제목, 저작자, 이미지, 사진 설명 , 가격
# 데이터 타입 : 숫자, 문자열,문자열,문자열 ( 이미지 주소), 문자열, 숫자

class Photo(models.Model):
    # 필드명 = 필드타입 ( 조건 .....)
    # pk ( 창고에서 기본적으로 생성 )
    title = models.CharField(max_length=50)
    autuor = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title + " " + self.autuor