from django.urls import path, include
from .views import Captcha, Resume, get_skill, get_skill2

urlpatterns = [
	path('captcha/', Captcha.as_view(), name="captcha"),
	path('resume/', Resume.as_view(), name="resume"),
	path("get_by_id/<int:pk>", get_skill),
	path("get_by_name/<str:name>", get_skill2),
	path('', include("api.urls")),
]
