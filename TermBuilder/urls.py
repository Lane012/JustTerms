from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'ajax/create_word_list/', views.create_user_word_list, name="new list"),
]

