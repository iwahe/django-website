from django.contrib import admin
from django.urls import path
#同じ階層(.)のviewsファイルから、IndexViewsをインポート
from .views import IndexViews

#urlとviewの処理をつなげるのか！！
urlpatterns = [
    path('', IndexViews.as_view()),
    path('about/', IndexViews.as_view()),
    path('contact/', IndexViews.as_view()),

]