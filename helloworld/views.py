from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from myDatabase.models import commentBox #匯入SQLite
from myDatabase.models import msg
from django.http import HttpResponseRedict

def index(request):
	menutexts=["首頁(偽)","推薦影片(偽)","最多觀看(偽)","發燒影片(偽)","尊榮會員(偽)"]

	#insert value in my SQLite sheet
	t1 = commentBox.objects.create(talker="不訂閱不斗內看免費",comment="這個不能只有我看到")
	t2 = commentBox.objects.create(talker="公館金城武",comment="5樓這個可以")
	msgs = commentBox.objects.all()

	return render(request,"week2.html",locals())

def message(request):
	talker = request.GET.get("name",False)
	comment=request.GET.get("msg",False)
	db = msg.objects.create("user"=talker,"message"=comment)
	msgs1  = db.objects.all()
	return render(request,'',locals())
