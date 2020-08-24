from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views
from django.contrib.auth import views as auth_views
from .views import *
from users import views as user_views
from genesis import views as genesis_views

app_name = 'ticket'


urlpatterns = [
    path('ticketreporting/', login_required(TicketReportingView.as_view()), name='ticket-reporting'),
    path('ticketreporting/?ret_tickets', ReturnTicketsView.as_view(), name='return-tickets'),
    path('ticketreporting/?upd_ticket', UpdateTicketsView.as_view(), name='update-ticket'),
    path('ticketreporting/?del_ticket', DeleteTicketsView.as_view(), name='delete-ticket'),
    path('ticketreporting/?cre_ticket', CreateTicketsView.as_view(), name='create-ticket'),
]
