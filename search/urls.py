from django.conf.urls import url
from .views import do_search_by_textbox

urlpatterns = [
    url(r'^$', do_search_by_textbox, name="search"),
    ]