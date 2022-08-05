from django.urls import path, include
from .views import Captcha, Login

urlpatterns = [
	path('captcha/', Captcha.as_view(), name="captcha"),
	path('login/', Login.as_view(), name="login"),
]
