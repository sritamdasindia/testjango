from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="blogs_index"),
    url(r'^posts$',views.posts,name="blog_posts"),
    url(r'^success$',views.show,name="blog_success")

]
