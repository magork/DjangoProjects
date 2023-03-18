from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.index, name="index"),
    #127.0.0.1/polls/
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name="detail"),
    #127.0.0.1/polls/1
    url(r'^(?P<question_id>[0-9]+)/results$', views.detail, name="results"),
    #127.0.0.1/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/votes$', views.detail, name="vote"),
    # 127.0.0.1/polls/1/votes


]