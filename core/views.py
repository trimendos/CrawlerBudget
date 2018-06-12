from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class MainPage(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'core/index.html'
