from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index_2.html"

    def get_context_data(self):
        #super()はもともとある、TemplateViewからコードを取るという意味らしい
        ctxt = super().get_context_data()
        ctxt["username"] = "マンタロー"
        return ctxt

#htmlのファイル名は他と一致しないようにしよう
class AboutView(TemplateView):
    template_name = "about_2.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_anarchy_match"] = 13000
        ctxt["skills"] = [
            "Xマッチ2200",
            "ビッグラン上位5%",
            "ヒーローモード完遂！",
        ]
        return ctxt

