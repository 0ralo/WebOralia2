from django.urls import path, include
from .views import Captcha, Resume

urlpatterns = [
	path('captcha/', Captcha.as_view(), name="captcha"),
	path('resume/', Resume.as_view(), name="resume"),
	path('', include("api.urls")),
]
