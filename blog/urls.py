from django.conf.urls import url
import views

urlpatterns = [
    url("^$", views.index,name="index"),
    url("^login$",views.login,name="login"),
    url("^register$",views.register,name="register"),
]
