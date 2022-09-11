from ninja import NinjaAPI
from .models import Person, Employee

api = NinjaAPI()


@api.get("/ping")
def pong(request):
	return "pong"


@api.get("people/")
def people(request):
	return Person.objects.all()


@api.get("employee/")
def employee(request):
	return Employee.objects.all()
