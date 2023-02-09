from django.shortcuts import render
from django.views.generic import TemplateView


#➀templatesフォルダにウェブページをのhtmlファイルを追加する
#➁views.pyにhtmlをユーザーに返す「ビュー」を追加
#➂urls.pyでびゅーとURLをつなげる

#views.pyはユーザーの入力に対して、htmlを返す役割
# Create your views here.


class IndexViews(TemplateView):
    template_name = "index.html"


#TemplateViewをもとに、IndexViewsというクラスを作成
#その後に、どのテンプレートを返すかを記述
