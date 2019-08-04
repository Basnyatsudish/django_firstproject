from django.urls import path, include
from . import views


urlpatterns = [
    path('addusers', views.addusers),
    path('additems', views.additems),
    path('additems/<str:action>/<int:oid>', views.additems,name='additems'),
    path('listitems',views.listitems),

]
