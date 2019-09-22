from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views
from delta.resources import statusResource,ledResource
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
status_resource = statusResource()
led_resource=ledResource()
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^delta/', include(status_resource.urls)),
    url(r'^delta/', include(led_resource.urls)),
    path('function/',views.function, name="function"),
    path('delta/tele/led/',views.show , name="show"),
    path('node/led/',views.node , name="node"),
    path('',views.homepage),
    path('on/',views.on, name="on"),
    path('off/',views.off, name="off")
]
urlpatterns += staticfiles_urlpatterns()

#mydata = json.loads(request.body.decode("utf-8"))
