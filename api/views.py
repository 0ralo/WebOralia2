from django.shortcuts import render
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/ping")
def pong(request):
	return "pong"


@api.get("")
def f(request):
	return ...
