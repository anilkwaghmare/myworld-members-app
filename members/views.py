from audioop import reverse
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from .models import Members
from .forms import MembersForm
from .filters import MemberFilter
# Create your views here.

def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    messages.success(request, "Record added successfully.")
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    messages.warning(request, "Record deleted successfully.")
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    messages.info(request, "Record updated successfully.")
    return HttpResponseRedirect(reverse('index'))
    
def MembersView(request):
    context = {}
    form = MembersForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updated successfully by Model Form.')
        return HttpResponseRedirect(reverse('index'))
    context['form'] = form
    return render(request, 'addform.html', context)
