from dataclasses import field
from django import forms
from .models import Photo

# form 생성 시 form.form(일반 폼 ) or forms.ModelForm ( 모델 폼 ) 상속 받으면서 생성 할 수 있음

class PhotoForm(forms.ModelForm):

    # 장고 폼은 내부 클래스를 반드시 meta 가져와야함
    class Meta:
        # 폼과 연결할 모델
        model = Photo
        # 모델 에서 사용할 필드 지정
        fields = ['title','author','image','description','price'] # fields = __all__