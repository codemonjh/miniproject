from django.contrib import admin
from django.urls import path,include
import mimetypes
import config.settings
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("accounts.urls")),
    path('accounts/', include('allauth.urls')),
    path('problem/',include('problem.urls')),
]#일단 두개놔두고 문제생길시 위에거를 제거


#장고디버그툴바세팅
if config.settings.DEBUG:
    mimetypes.add_type("application/javascript", ".js", True)
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns