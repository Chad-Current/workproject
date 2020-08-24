from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import *

# Change to TemplateView with Radio Boxing and Logic Flow
class TicketReportingView(LoginRequiredMixin, ListView):
    model = Tickets
    template_name = 'ticket/ticketreporting.html'


class ReturnTicketsView(LoginRequiredMixin, ListView):
    model = Tickets
    template_name = 'ticket/ret_tickets.html'

    context_object_name = 'ticket'  # Default: object_list
    queryset = Tickets.objects.all().order_by('badge_identifier')

class UpdateTicketsView(LoginRequiredMixin, ListView):
    model = Tickets
    template_name = 'ticket/upd_ticket.html'

class DeleteTicketsView(LoginRequiredMixin, ListView):
    model = Tickets
    template_name = 'ticket/del_ticket.html'

class CreateTicketsView(LoginRequiredMixin, ListView):
    model = Tickets
    template_name = 'ticket/cre_ticket.html'
