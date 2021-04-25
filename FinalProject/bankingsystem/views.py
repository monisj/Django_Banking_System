from django.shortcuts import render,redirect
from .models import Register
from .models import Comment
from.models import Deposit
from .models import WithDraw
from .models import Bill
from .models import State
from .models import Total
from .forms import Registerform
from .forms import Commentform
from .forms import Depositform
from .forms import WithDrawform
from .forms import Billform
from .forms import StatusForm
from .forms import Totalform
from .tag import sel
class choose:
    name=str()
    email=str()
    account=str()
    amount=int()
def index(request):
    now=sel()
    form=Registerform(initial={'account':sel.a})
    return(render(request, 'registration.html',{'form':form}))

def add_new(request):
    form=Registerform(request.POST)
    form.save()
    namel=[]
    eml=[]
    acl=[]
    aml=[]
    acc=Register.objects.values()
    for i in acc:
        namel.append(i['Name'])
        eml.append(i['Email'])
        acl.append(i['account'])
        aml.append(i['amount'])
    form1=Register.objects.get(account=acl[-1])
    form2=Total(Name=namel[-1],Email=eml[-1],account=form1,amount=aml[-1])
    form2.save()

    return redirect('/show')

def login(request):
    form=Registerform
    return(render(request, 'Login.html',{'form':form}))

def check(request):
    acc=Register.objects.values()
    st=State.objects.values()
    form=Commentform
    em=request.GET['uname']
    pass1=request.GET['psw']
    eml=[]
    psl=[]
    namel=[]
    accl=[]
    accl1=[]
    act=[]
    for i in st:
        accl1.append(i['account'])
        act.append(i['Status'])

    for s in acc:
        eml.append(s['Email'])
        psl.append(s['password'])
        namel.append(s['Name'])
        accl.append(s['account'])

    if 'btn2' in request.GET.keys():
        print(request.GET.keys())
        info=choose()
        info.name=namel[eml.index(em)]
        info.email=em
        info.account=accl[eml.index(em)]
        if em in eml and pass1 in psl and em=='siddiquimohsin660@gmail.com' and pass1=='Mohsin90':
            if info.account in accl1:
                State.objects.filter(account=info.account).delete()
                fo1=State(Name=info.name,Email=info.email,account=info.account,Status='Active')
                fo1.save()
                return (render(request,'adminregister.html'))
        else:
            fo1=State(Name=info.name,Email=info.email,account=info.account,Status='Active')
            fo1.save()
            return (render(request,'dontshowadmin.html'))
    else:
        if em in eml and pass1 in psl and eml.index(em)==psl.index(pass1):
            a=namel[eml.index(em)]
            info=choose()
            info.name=namel[eml.index(em)]
            info.email=em
            info.account=accl[eml.index(em)]

            if info.account in accl1:
                State.objects.filter(account=info.account).delete()
                fo1=State(Name=info.name,Email=info.email,account=info.account,Status='Active')
                fo1.save()
                return(render(request, 'home.html',{'form':form,'breif':info}))
            else:
                fo1=State(Name=info.name,Email=info.email,account=info.account,Status='Active')
                fo1.save()
                return(render(request, 'home.html',{'form':form,'breif':info}))
        else:
            return(render(request, 'dontshow.html'))


def comment(request):
    fo1=State.objects.values().last()
    fore=Register.objects.values()
    psl=[]
    for i in fore:
        psl.append(i['password'])
    if request.GET['psw'] in psl and fo1['Status']!='Deactive':
        stud=Register.objects.get(account=fo1['account'])
        form=Comment(Name=fo1['Name'],Email=fo1['Email'],account=stud,comment=request.GET['comment'])
        form.save()
        return (render(request,'dosent1.html'))
    else:
        return (render(request,'notsendcomment.html'))


def deposit(request):
    form=State.objects.values().last()
    return(render(request,'Deposit.html',{'form':form}))


def dodeposit(request):
    fo=State.objects.values().last()
    fore=Register.objects.values()
    psl=[]
    amml=[]
    for i in fore:
        psl.append(i['password'])
        amml.append(i['amount'])
    stud=Register.objects.get(account=fo['account'])
    if request.GET['psw'] in psl and request.GET['amm']!=0 and fo['Status']!='Deactive':
        value=amml[psl.index(request.GET['psw'])]+int(request.GET['amm'])
        to=Total.objects.filter(account=stud).update(amount=value)
        depo=Deposit(account=stud,password=request.GET['psw'],amount=request.GET['amm'])
        depo.save()
        return (render(request,'dodeposite1.html'))
    else:
        return (render(request,'dontdeposite.html'))
def withdraw(request):
    form=State.objects.values().last()
    return (render(request,'Withdraw.html',{'form':form}))

def dowithdraw(request):
    fo=State.objects.values().last()
    fore=Register.objects.values()
    psl=[]
    amml=[]
    for i in fore:
        psl.append(i['password'])
        amml.append(i['amount'])
    stud=Register.objects.get(account=fo['account'])
    if request.GET['psw'] in psl and request.GET['amm']!=0 and fo['Status']!='Deactive':
        if int(request.GET['amm'])<amml[psl.index(request.GET['psw'])]:
            value=amml[psl.index(request.GET['psw'])]-int(request.GET['amm'])
            to1=Register.objects.filter(account=fo['account']).update(amount=value)
            to=Total.objects.filter(account=stud).update(amount=value)
            depo=WithDraw(account=stud,password=request.GET['psw'],amount=request.GET['amm'])
            depo.save()
            return (render(request,'dowithdraw1.html'))
        else:
            return (render(request,'shortwithdraw.html'))
    else:
        return (render(request,'dontdeposite.html'))

def billpay(request):
    form=State.objects.values().last()
    return (render(request,'BillPay.html',{'form':form}))

def dobillpay(request):
    fo=State.objects.values().last()
    fore=Register.objects.values()
    psl=[]
    amml=[]
    for i in fore:
        psl.append(i['password'])
        amml.append(i['amount'])
    stud=Register.objects.get(account=fo['account'])
    if request.GET['psw'] in psl and request.GET['amm']!=0 and fo['Status']!='Deactive':
        if int(request.GET['amm'])<amml[psl.index(request.GET['psw'])]:
            value=amml[psl.index(request.GET['psw'])]-int(request.GET['amm'])
            to1=Register.objects.filter(account=fo['account']).update(amount=value)
            to=Total.objects.filter(account=fo['account']).update(amount=value)
            depo=Bill(account=stud,password=request.GET['psw'],amount=request.GET['amm'],billno=request.GET['bill'])
            depo.save()
            return (render(request,'dobillpay1.html'))
        else:
            return (render(request,'shortwithdraw.html'))
    else:
        return (render(request,'dontdeposite.html'))

def adminshow(request):
    if 'btn1' in request.GET.keys():
        stud=Deposit.objects.order_by('-id')
        return (render(request,'depositeall.html',{'stud':stud}))
    elif 'btn2' in request.GET.keys():
        stud=WithDraw.objects.order_by('-id')
        return (render(request,'withdrawall.html',{'stud':stud}))
    elif 'btn3' in request.GET.keys():
        stud=Bill.objects.order_by('-id')
        return (render(request,'billall.html',{'stud':stud}))
    elif 'btn4' in request.GET.keys():
        stud=Comment.objects.order_by('-id')
        return (render(request,'commentall.html',{'stud':stud}))
    elif 'btn5' in request.GET.keys():
        stud=Total.objects.order_by('-id')
        return (render(request,'totalall.html',{'stud':stud}))
    elif 'btn6' in request.GET.keys():
        stud=State.objects.order_by('-id')
        return (render(request,'stateall.html',{'stud':stud}))
    elif 'btn7' in request.GET.keys():
        return redirect('/logout')

def logout(request):
    form=State.objects.values().last()
    print(form)
    name=form['Name']
    email=form['Email']
    account=form['account']
    State.objects.filter(account=account).delete()
    form2=State(Name=name,Email=email,account=account,Status='Deactive')
    form2.save()
    form=Registerform(initial={'account':sel.a})
    return(render(request, 'registration.html',{'form':form}))




