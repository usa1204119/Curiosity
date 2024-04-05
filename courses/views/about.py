from django.views.generic import TemplateView

class AboutPageView(TemplateView):  # new
    template_name = "courses/about.html"