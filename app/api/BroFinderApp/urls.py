from django.urls import re_path
from BroFinderApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^users$',views.usersApi),
    re_path(r'^users/([0-9]+)$',views.usersApi),

    re_path(r'^events$',views.eventsApi),
    re_path(r'^events/([0-9]+)$',views.eventsApi),

    re_path(r'^login$',views.loginuser),
    re_path(r'^login/([0-9]+)$',views.loginuser),

    re_path(r'^logout$',views.logoutuser),
    re_path(r'^logout/([0-9]+)$',views.logoutuser),

    re_path(r'^register$',views.registeruser),
    re_path(r'^register/([0-9]+)$',views.registeruser),

    re_path(r'^user$',views.getUsers),
    re_path(r'^user/([a-zA-Z]+)$',views.getUsers),

    re_path(r'^pokus$',views.pokusApi),
    re_path(r'^pokus/([a-zA-Z]+)$',views.pokusApi),

    re_path(r'^eventik$',views.eventikApi),
    re_path(r'^eventik/([a-zA-Z]+)$',views.eventikApi),

    re_path(r'^eventikk$',views.eventikNameApi),
    re_path(r'^eventikk/([a-zA-Z]+)$',views.eventikNameApi),

    re_path(r'^comment$',views.commentApi),
    re_path(r'^comment/([0-9]+)$',views.commentApi),

    
    re_path(r'^komment$',views.kommentApi),
    re_path(r'^komment/([0-9]+)$',views.kommentApi),


    re_path(r'^order/([0-9]+)$',views.orderedEventsApi),

    re_path(r'^events/savefile/.',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)