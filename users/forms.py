from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # 폼의 형태를  지정할 수 있음 > clean_ 으로 시작
    # 매번 폼 제출 시 clean_ 함수를 모두 실행해서 체크
    # return result of clean data

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                # 직접적으로 에러 발생 위치를 지정 > 지정X -> 모든에러가 제일 윗단에서 발생
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
