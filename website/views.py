from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.signing import Signer
from random import shuffle, randint
from string import ascii_letters
from PIL import Image, ImageDraw, ImageFont
from WebOralia2.celery import deleteimage
from website.models import Skill


class Captcha(View):
	template = "captcha.html"
	signer = Signer()
	letters = list(ascii_letters)

	def get(self, request, *args, **kwargs):
		shuffle(self.letters)
		code = "".join(self.letters[:8])
		hash = self.signer.sign_object(str(code))
		out = Image.new("RGB", (180, 45), (255, 255, 255))
		font = ImageFont.truetype("arial.ttf", size=30)
		img = ImageDraw.Draw(out)
		w, h = img.textsize(code, font=font)
		img.text(((180-w)/2, (45-h)/2), code, fill=(0, 0, 0), font=font)
		name = "code_{}.jpg".format(randint(10, 10000))
		out.save("media/codes/{}".format(name))

		deleteimage.apply_async(countdown=60, args=(name,))
		return render(
			request,
			self.template,
			{
				"hash": hash,
				"code": code,
				"name": name,
			})

	def post(self, request, *args, **kwargs):
		code: str = request.POST.get("code", "")
		codehash: str = request.POST.get("hash", "")
		code = code.strip()
		if code == self.signer.unsign_object(codehash):
			response = redirect("login")
			captcha = self.signer.sign_object(3)
			response.set_cookie("captcha", captcha)
			return response
		else:
			return redirect("captcha")


class Resume(View):
	template = "resume.html"

	def get(self, request, *args, **kwargs):
		skills = Skill.objects.all()
		return render(request, self.template, {"skills": skills})


def get_skill(request, pk):
	try:
		skill = Skill.objects.get(pk=pk)
	except:
		return HttpResponseBadRequest("<h1>Skill was not found</h1>")
	return HttpResponse(f"Skill[{skill.name}]={skill.percent}")


def get_skill2(request, name):
	try:
		skill = Skill.objects.get(name=name)
	except:
		return HttpResponseBadRequest("<h1>Skill was not found</h1>")
	return HttpResponse(f"Skill[{skill.name}]={skill.percent}")

