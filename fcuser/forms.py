from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required': '아이디를 입력해 주세요'}, max_length=128, label="NAME")
    password = forms.CharField(error_messages={'required': '비밀번호를 입력해 주세요'}, widget=forms.PasswordInput, label="PASSWORD")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username = username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '아이디가 없네요. 회원가입하세요')
                return


            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호오류')
            else:
                self.user_id = fcuser.id
