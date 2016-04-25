from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List
from printer.printer import print_to_log
def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    print_to_log(request)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    print_to_log('b:'+str(redirect('/lists/%d/' % list_.id)
))
    return redirect('/lists/%d/' % list_.id)

def view_list(request,list_id):
    print_to_log('c:'+str(request)+':')
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request,'list.html',{'items':items})
