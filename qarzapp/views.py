from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import QarzModel
from .forms import QarzForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

@login_required(login_url='login')
def QarzCreate(request):
    form=QarzForm

    if request.method == 'POST':
        form=QarzForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('qarzlar')
    context={'form':form}
    return render(request,'qarzapp/qarz-create.html',context)
    

def QarzUpdate(request,pk):
    qarz=QarzModel.objects.get(id=pk)
    form=QarzForm(instance=qarz)

    if request.method == 'POST':
        form=QarzForm(request.POST,instance=qarz)
        if form.is_valid():
            form.save()
            return redirect('qarzlar')
    context={'form':form}
    return render(request,'qarzapp/qarz-create.html',context)

def QarzDelete(request,pk):
    qarz=QarzModel.objects.get(id=pk)
    if request.method == 'POST':
        qarz.delete()
        return redirect('qarzlar')
    context={'qarz':qarz}
    return render(request,'qarzapp/del.html',context)


def QarzSearch(request):
    text=''
    if request.GET.get('text'):
        text = request.GET.get('text')

    qarzlar=QarzModel.objects.filter(
        Q(name__icontains=text)|
        Q(amount__icontains=text)|
        Q(date__icontains=text)|
        Q(currency__icontains=text)
    )
    return qarzlar,text

@login_required(login_url='login')
def QarzPage(request):

        qarzdorlar, text=QarzSearch(request)
        context={'qarzdor':qarzdorlar,'text':text}
        return render(request,'qarzapp/qarzlar.html',context)

def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('qarzlar')

    if request.method=='POST':
        username=request.POST['username'].lower()
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
        except:
            return redirect('login')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('qarzlar')
        else:
            return redirect('login')

    return render(request,'qarzapp/login.html')


