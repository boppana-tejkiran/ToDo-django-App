from django.shortcuts import render, HttpResponse
from datetime import datetime

current_tasks = [ 'x', 'y', 'z']
# Create your views here.
def index_page(request):
    return render(request,'index.html',context={"cur_date": 
    str(datetime.now())})