from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "multipleimagesapp"
urlpatterns = [
    path("",views.home, name="home"),
    path("uploadhandler/",views.uploadhandler, name="uploadhandler"),
    path("gallery/<int:pk>/",views.gallery, name="gallery"),
    path("delete/",views.delete, name="delete"),
    path("update/",views.update, name="update"),
 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
