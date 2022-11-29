from django.shortcuts import render
from django.shortcuts import redirect
from app12.models import studentMode,loginMode,adminMode
from django.contrib import messages

# Create your views here.
def studentInfo(request):
    return render(request,"home.html")


def studentLogin(request):
    return render(request,"login.html")


def studentRegister(request):
    return render(request,"registration.html")


def studentData(request):
    n = request.POST.get("t1")
    a = request.POST.get("t2")
    c = request.POST.get("t3")
    g = request.POST.get("t4")
    u = request.POST.get("t5")
    p = request.POST.get("t6")
    type='student'
    st = studentMode(name=n,age=a,contactno=c,gender=g,username=u)
    st.save()

    loginMode(username=u,password=p,type=type).save()
    messages.success(request,"Registerd Sucessfully")
    return redirect("register")


def sLogin(request):
    u = request.POST.get("t1")
    p = request.POST.get("t2")
    try:
        loginMode.objects.get(username=u, password=p)
        return render(request, "student_home.html",{"name":u})
    except loginMode.DoesNotExist:
        return render(request,"login.html",{"note":"Login Failed"})


def studentHome(request):
    uname=request.GET.get("un")
    return render(request,"student_home.html",{"name":uname})


def studentProfile(request):
    uname = request.GET.get("un")
    stu=studentMode.objects.get(username=uname)
    return render(request, "student_profile.html", {"name": uname,"data":stu})


def studentUpdate(request):
    uname = request.GET.get("un")
    stu = studentMode.objects.get(username=uname)
    return render(request, "student_update.html", {"name": uname, "data": stu})


def updateStudent(request):
    n = request.POST.get("u1")
    age = request.POST.get("u2")
    cno = request.POST.get("u3")
    g = request.POST.get("u4")
    un = request.POST.get("u5")
    try:
        studentMode.objects.filter(username=un).update(name=n, age=age, gender=g, contactno=cno)
        return render(request,"student_home.html",{"name":un})
    except studentMode.DoesNotExist:
        return render(request,"student_home.html",{"name":un})


def forgot(request):
    return render(request,"forgot.html")


def checkPassword(request):
    u = request.POST.get("p1")
    cno = request.POST.get("p2")
    try:
        studentMode.objects.get(username=u,contactno=cno)
        lm=loginMode.objects.get(username=u)
        return render(request,"forgot.html",{"data":lm})
    except studentMode.DoesNotExist:
        return render(request,"forgot.html",{"eror":"Enterd Wrong details"})


def adminLogin(request):
    return render(request,"admin_login.html")


def adLogin(request):
    u = request.POST.get("a1")
    p = request.POST.get("a2")
    try:
        adminMode.objects.get(username=u,password=p)
        return render(request, "admin_home.html")
    except adminMode.DoesNotExist:
        return render(request, "admin_login.html")


def adminHome(request):
    adminMode.objects.get()
    return render(request,"admin_home.html")


def viewProfile(request):

        st = studentMode.objects.all()

        return render(request,"viewprofile.html",{"data":st})


def adviewProfile(request):
    st = studentMode.objects.only().delete()
    l1 = loginMode.objects.only().delete()
    return render(request,"viewprofile.html",{"data":st,"data":l1})