from django.http import HttpRequest
from django.shortcuts import redirect, render

from passwordmanager.models import PasswordsManagerModel
from passwordmanager.util import EncryptHelper

# Create your views here.
def home(req:HttpRequest):
    print(type(req))
    context={"data":map(lambda o:{
        "id":o.id,
        "password":EncryptHelper.decrypt(o.password),
        "username":EncryptHelper.decrypt(o.username),
        "name":o.name,
        "url":o.url
        }, PasswordsManagerModel.objects.all())}
    return render(req,"passwordmanager/home.html",context=context)

def delete(req:HttpRequest,id):
    PasswordsManagerModel.objects.get(id=id).delete()
    return redirect('/passwordmanager/')

def edit(req:HttpRequest,id):
    if req.POST:
        passwordManager=PasswordsManagerModel.objects.get(id=id)
        passwordManager.name=req.POST.get("name")
        passwordManager.url=req.POST.get("url")
        passwordManager.username=req.POST.get("username")
        passwordManager.password=req.POST.get("password")
        passwordManager.save()
        return redirect('/passwordmanager/')
    passwordManager=PasswordsManagerModel.objects.get(id=id)
    context={
        "editData":{
            "id":passwordManager.id,
            "password":EncryptHelper.decrypt(passwordManager.password),
            "username":EncryptHelper.decrypt(passwordManager.username),
            "name":passwordManager.name,
            "url":passwordManager.url
            },

        "data":map(lambda o:{
        "id":o.id,
        "password":EncryptHelper.decrypt(PasswordsManagerModel.objects.all().first().password),
        "username":EncryptHelper.decrypt(PasswordsManagerModel.objects.all().first().username),
        "name":o.name,
        "url":o.url
        }, PasswordsManagerModel.objects.all())
    }
    return render(req,"passwordmanager/home.html",context) 

def add(req:HttpRequest):
    passwordManager=PasswordsManagerModel(
        name=req.POST.get("name"),
        username=req.POST.get("username"),
        url=req.POST.get("url"),
        password=req.POST.get("password")
    )
    passwordManager.save()
    return redirect('/passwordmanager/')

