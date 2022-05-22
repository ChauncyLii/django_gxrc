from urllib import request
from django.shortcuts import render
from .models import Infomation
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def index(request):
    return render(request,'info/index.html')

# 保留全局搜索条件
global value
global v_city
global v_level

def system(request):
    global value
    global v_city
    global v_level
    dict_data = {}
    if request.GET.get('q'):
        value = request.GET.get('q')
    else:
        value = ''
    if request.GET.get('level_1'):
        v_level = request.GET.get('level_1')
    else:
        v_level = "计算机/互联网/通信电子"

    dict_data['target_post__contains'] = value
    post_list = Infomation.objects.filter(
        **dict_data
    ).filter(level_1= v_level)
    paginator = Paginator(post_list,6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(1)
    return render(request, 'info/system.html', {'page_obj': page_obj,'value':value,'v_level': v_level})

def detail(request,info_id):
    detail_item = Infomation.objects.get(id=info_id)
    return render(request,'info/detail.html',{'detail_item':detail_item})


    