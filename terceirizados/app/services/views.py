from django.shortcuts import render
from django.views.generic import TemplateView
from app.services.models import Services

class DashboardView(TemplateView):
    model = Services
    template_name = 'services/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['service_list'] = Services.objects.all()
        return context