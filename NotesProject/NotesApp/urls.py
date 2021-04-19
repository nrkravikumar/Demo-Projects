from django.urls import path
from NotesApp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="cn"),
	path('reg/',views.register,name="rg"),
	path('dashboard/',views.dashboard,name="dsh"),
	path('login/',v.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	path('pfle/',views.prfle,name="pf"),
	path('updf/',views.updfple,name="upf"),
	path('vwnt/',views.notesview,name="ntv"),
	path('crnt/',views.crnotes,name="crn"),
	path('upnot/<int:pk>/',views.updatent,name="upnt"),
	path('dlt/<int:pj>/',views.deletent,name="delt"),
]