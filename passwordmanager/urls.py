
from django.urls import path
from passwordmanager.views import home,delete,edit,add

urlpatterns=[
    path("",home,name="passwordmanager"),
    path("delate/<str:id>",delete,name="delatepassword"),
    path("edit/<str:id>",edit,name="editpassword"),
    path("add/",add,name="addpassword"),
]