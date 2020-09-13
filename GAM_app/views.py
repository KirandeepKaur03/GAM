from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from GAM_app.models import Subscribe, Queries, SiteUser, admins
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'index.html')


def About_us(request):
    return render(request, 'About_us.html')


def Classes_Taught(request):
    return render(request, 'Classes_Taught.html')


def admin_login1(request):
    return render(request, 'admin_login.html')


def After_Login(request):
    if request.session.get('_auth_user_id') is not None:
        return render(request, 'After_Login.html')
    else:
        return redirect('/login/')


@csrf_exempt
def Add_Subscriber(request):
    if request.method == 'POST':
        email = request.POST['email']
        S = Subscribe(email=email)
        S.save()
        return redirect('/')


@csrf_exempt
def Add_Queries(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        Q = Queries(Message=message, Email=email)
        Q.save()
        return redirect('/')


@csrf_exempt
def add_user_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        address = request.POST['address']
        mobile = request.POST['mobile']
        if SiteUser.objects.filter(username=name).exists():
            messages.error(request, 'This username has already been taken by other user. Please try some other '
                                    'username.')
            return render(request, 'add_user_data.html')
        else:
            data = SiteUser(username=name, email=email,
                            password=password, address=address,
                            mobile=mobile)
            data.save()
            messages.success(request, 'Student saved successfully. You can now login with your login credentials.')
    return render(request, 'add_user_data.html')


@csrf_exempt
def my_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if SiteUser.objects.filter(email__icontains=email).exists():
            data = SiteUser.objects.get(email__icontains=email)
            if check_password(password, data.password):
                user = authenticate(request, username=data.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/After_Login/')
                else:
                    return HttpResponse('user none aa rha hai')
            else:
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('Invalid Email')
    elif request.session.get('_auth_user_id') is not None:
        return redirect('/After_Login/')
    else:
        return redirect('/')


def my_logout(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        if admins.objects.filter(Username__icontains=Username).exists():
            data = admins.objects.get(Username__icontains=Username)
            if check_password(password,data.password):
                user = data.Username
                print(user)
                if user is not None:
                    return redirect('/admin_login1/')
            else:
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('Invalid Username')
    else:
        return redirect('/')


def admin_logout(request):
    return redirect('/')


def enrolled(request):
    records = SiteUser.objects.all()
    return render(request, 'enrolled.html', {'data': records})


@csrf_exempt
def update(request, id):
    if request.method == 'POST':
        updated = SiteUser(id=id, username=request.POST['username'], email=request.POST['email'],
                           address=request.POST['address'], mobile=request.POST['mobile'])
        updated.save()
        return redirect('/admin_login1/enrolled/')

    elif SiteUser.objects.filter(id=id).exists():
        data = SiteUser.objects.get(id=id)
        return render(request, 'update.html', {'data': data})
    return redirect('/admin_login1/enrolled/')


@csrf_exempt
def delete(request, id):
    if SiteUser.objects.filter(id=id).exists():
        data = SiteUser.objects.get(id=id)
        data.delete()
        return redirect('/admin_login1/enrolled/')


def queries(request):
    records = Queries.objects.all()
    return render(request, 'queries.html', {'data': records})


@csrf_exempt
def query_delete(request, id):
    if Queries.objects.filter(id=id).exists():
        data = Queries.objects.get(id=id)
        data.delete()
        return redirect('/admin_login1/queries/')

@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if SiteUser.objects.filter(email=email).exists():
            data = SiteUser.objects.filter(email=email).update(password=password)
            messages.success(request,"Password changed successfully")
    return render(request, 'forgot_password.html')

@csrf_exempt
def add_admin(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = make_password(request.POST['password'])
        if admins.objects.filter(Username=Username).exists():
            messages.error(request, 'You are already an admin.')
            return render(request, 'add_admin.html')
        else:
            data = admins(Username=Username,
                            password=password)
            data.save()
            messages.success(request, 'Admin created successfully')
            return render(request, 'add_admin.html')
    return render(request, 'add_admin.html')

def forgot_adminpass(request):
    return render(request,'add_admin.html')


@csrf_exempt
def forgot_adminpass(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = make_password(request.POST['password'])
        if admins.objects.filter(Username=Username).exists():
            data = admins.objects.filter(Username=Username).update(password=password)
            messages.success(request,"Password changed successfully")
    return render(request, 'forgot_adminpass.html')


