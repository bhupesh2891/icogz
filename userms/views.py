from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "userms/dashbord.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     data = {
    #             "message": _("Welcome to Dashboard"),
    #             'page_code': SIDEBAR_MENU_PAGE_CODE_APPLICATION
    #         }
    #     context.update(data)
    #     return context
