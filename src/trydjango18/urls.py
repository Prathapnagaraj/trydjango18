from django.conf.urls import include, url
from django.contrib import admin
import newsletter
urlpatterns = [
    # Examples:
    # url(r'^$', 'trydjango18.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^home", 'newsletter.views.home', name="home"),
    url(r'^admin/', include(admin.site.urls)),

]
