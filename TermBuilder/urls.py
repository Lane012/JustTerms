from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^study', views.study_page, name='study'),
    url(r'^test', views.test_page, name='test'),
    url(r'ajax/create_word_list/', views.create_user_word_list, name="new list"),
    url(r'ajax/test_score_update/', views.test_score_update, name="new score"), 
]

