from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
	menutexts=["首頁(偽)","推薦影片(偽)","最多觀看(偽)","發燒影片(偽)","尊榮會員(偽)"]

	return render(request,"week2.html",locals())