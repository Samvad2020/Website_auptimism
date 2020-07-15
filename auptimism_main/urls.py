

from django.urls import path
from IEP.views import iep
from .views import login, logout, add_profile, create_activity, assign, homeplan, seechild, \
    show_activity, nochild, noactivity, view_activity, view_child, done, report, reportmed, reportd, home, \
    contact, show

urlpatterns = [
    path('', home),
    path('login/',login),
    path('logout',logout, name='logout'),
    path('show/', show, name='show'),
    path('addchild/',add_profile,name='add_profile'),
    path('createactivity/',create_activity, name="create_activity"),
    path('assignactivity/<str:title>',assign, name="assign"),
    path('homeplan/', homeplan, name="homeplan"),
    path('seechild/<str:name>/', seechild, name="seechild"),
    path('showactivity/', show_activity, name="show_activity"),
    path('nochild/',nochild,name="nochild"),
    path('noactivity/',noactivity,name="noactivity"),
    path('activity/<str:title>/',view_activity,name="view_activity"),
    path('iep/',iep,name="iep"),
    path('view_child/',view_child,name="view_child"),
    path('done/',done,name="done"),
    path('report/<str:name>/',report,name="report"),
    path('reportd/<str:name>/',reportd,name="reportd"),
    path('reportmed/<str:name>/',reportmed,name="reportmed"),
    path('contact/',contact,name="contact"),
]