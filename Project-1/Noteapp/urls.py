from django.urls import path
from Noteapp import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="cn"),
	path('lg/',ad.LoginView.as_view(template_name='stc/login.html'),name="log"),
	path('rg/',views.regi,name="rge"),
	path('ds/',views.dashboard,name="dsh"),
	path('lgo/',ad.LogoutView.as_view(template_name='stc/logout.html'),name="logo"),
	path('pro/',views.profile,name="profile"),
    path('updf/',views.updpf,name="upf"),
    path('psd/',views.chpswd,name="cp"),
    path('fgpwd/',ad.PasswordResetView.as_view(template_name='stc/passwordreset.html'),name="reset_password"),
    path('rspwd/',ad.PasswordResetDoneView.as_view(template_name='stc/passwordresetdone.html'),name="password_reset_done"),
    path('rspwd/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name='stc/passwordresetconfirm.html'),name="password_reset_confirm"),
    path('rspwdcmv/',ad.PasswordResetCompleteView.as_view(template_name='stc/passwordresetcomplte.html'),name="password_reset_complete"),
    ]