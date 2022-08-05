from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.signing import Signer, BadSignature
from random import shuffle, random, randint
from string import ascii_letters
from PIL import Image, ImageDraw, ImageFont
from WebOralia2.celery import deleteimage


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


class Login(View):
	def get(self, request: WSGIRequest, *args, **kwargs):
		try:
			count = request.COOKIES.get("captcha")
			if count == 0:
				return redirect("captcha")
		except BadSignature:
			return redirect("captcha")
		except KeyError:
			return redirect("captcha")
		return render(request, "Auth/login.html")

	def post(self, request, *args, **kwargs):
		# TODO if login then login if error then retry and count -=1
		...
