from django.shortcuts import render,redirect,get_object_or_404
from careapp.models import *

#Create your views here.

def home (request):
    return render (request,'index.html')

def starter (request):
    return render (request,'starter-page.html')


def appointment (request):
    if request.method == 'POST':

        all = MyAppointments(
            name = request.POST['name'],
            email = request.POST['email'],
            phonenumber = request.POST['phone'],
            datetime = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],

        )
        all.save()
        return render (request,'appointment.html')
    else:
        return render (request,'appointment.html')



def about (request):
    return render (request,'about.html')

def show (request):
    allappointments=MyAppointments.objects.all()
    return render(request,'show.html',{'allappointments':allappointments})

def delete(request,id):
    myappoint =MyAppointments.objects.get(id = id)
    myappoint.delete()
    return redirect ('/show')

def edit(request,id):
    editappointment = get_object_or_404(MyAppointments,id=id)
    if request.method =='POST':
        editappointment.name =request.POST.get('name')
        editappointment.email =request.POST.get('email')
        editappointment.phonenumber=request.POST.get('phonenumber')
        editappointment.datetime =request.POST.get('datetime')
        editappointment.department=request.POST.get('department')
        editappointment.doctor =request.POST.get('doctor')
        editappointment.message=request.POST.get('message')

        editappointment.save()
        return redirect('/show')
    return render(request,'edit.html',{'editappointment':editappointment})


