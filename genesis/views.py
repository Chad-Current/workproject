from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserGenesisReport
import datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style('darkgrid',{ 'axes.spines.bottom': False,
                           'axes.spines.left': False,
                           'axes.spines.right': False,
                           'axes.spines.top': False,
                           "axes.facecolor": ".95"})

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

@login_required
def genesis(request):
    objects = UserGenesisReport.objects.all()
    return render(request, 'genesis/genesisreports.html', {'objects':objects})

# @login_required
# def genesis(request):
#     data = pd.read_excel('c://Users/ccurrent/Desktop/westcom_test.xlsm', skiprows=7, header=None, sheet_name='Data',
#                      parse_dates=True,  usecols=[3,4,5,6],
#                      names=['Subscriber_ID','Subscriber_Alias','PTT Count','PTT Time'])
#     data.dropna(axis=0, inplace=True)
#     # Cover any anominaly
#     data['Subscriber_Alias'].fillna('Missing',inplace=True)
#     data['Subscriber_ID'].fillna(0, inplace=True)
#     data['Subscriber_ID'] = data['Subscriber_ID'].astype(int)
#     data['PTT Count'].fillna(0, inplace=True)
#     data['PTT Count'] = data['PTT Count'].astype(int)
#     data['PTT Time'].fillna(0, inplace=True)
#     data['PTT Time'] = data['PTT Time'].astype(int)
#
#     data_frames = []
#     packs = [(0,100),(101,200),(201,300),(301,400),
#         (401,500),(501,600),(601,700),(701,800),
#         (801,900),(901,1000),(1001,1100),(1101,1200),]
#
#     for i in range(len(packs)):
#         x,y = packs[i]
#         data_frames.append(data[x:y])
#
#     plt.figure(figsize=(20,20))
#     plot = figure(title='Westcom', x_axis_label='Subscriber Id', y_axis_label='PTT Counts', plot_width=400, plot_height=400,
#              x_range=(10000, 20000))
#     plot.vbar(x='Subscriber_ID', top='PTT Count', width=0.9, source=data_frames[0])
#     script, div = components(plot)
#     report_time = datetime.datetime.now() # Change to datetime.datetime.fromtimestamp for correct request time
#
#     return render(request, 'genesis/genesisreports.html', {'script': script, 'div': div , 'report_time': report_time})
#
# @login_required
# def genesispull(request):
#     data = pd.read_excel('c://Users/ccurrent/Desktop/recent.xlsm', skiprows=7, header=None, sheet_name='Data',
#                      parse_dates=True, usecols=[1,2,3], index_col=0,
#                      names=['Date and Time', 'Number of PTTs', 'Airtime (Seconds)'])
#     data_one = data[:35]
#     data_two = data[35:70]
#     data_three = data[70:100]
#     data_four = data[100:130]
#     data_list = [data_one, data_two, data_three, data_four]
#
#     for i in data_list:
#         plt.figure(figsize=(15,5))
#         plt.xticks(rotation=45)
#         plt.xlabel('Time')
#         plt.ylabel('Number of PTTs')
#         plt.plot('Number of PTTs', data=i)
#         plt.show()
#
#     return render(request, 'genesis/genesisreports.html', {'script': script, 'div': div , 'organization':organization})
