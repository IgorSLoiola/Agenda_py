from typing import Any
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import Http404, HttpResponse
from contact.models import Contact
from django.contrib import messages, auth
from contact.forms import contactForm, RegisterForm, loginUser
# from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
# from contact import models


# Create your views here.
def index(request):
    # contacts = models.Contact.objects.all().order_by('id')
    contacts = Contact.objects.filter(show=True).order_by('id')

    paginator = Paginator(contacts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # print(contacts.query)

    context = {
        'page_obj' : page_obj,
        'title_page': 'Contacts',
    }
    return render(
        request,
        'contact/pages/index.html',
        context,
                )
def contact(request, id):
    #oneContact = Contact.objects.filter(pk=id).first()
    #oneContact = get_object_or_404(Contact.objects.filter(pk=id))
    oneContact = get_object_or_404(Contact, pk=id, show=True)

    # if oneContact is None:
    #     raise Http404()

    # print(contacts.query)

    name_contact = f'{oneContact.name}'

    context = {
        'contact' : oneContact,
        'title_page': name_contact,
    }
    return render(
        request,
        'contact/pages/contact.html',
        context,
                )

def search(request):
    search_value = request.GET.get('q', '').strip()
    contacts = Contact.objects.filter(show=True).filter(Q(name__icontains=search_value) | Q(email__icontains=search_value) ).order_by('id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if search_value == '':
        return redirect('index')
    

    context = {
        'page_obj' : page_obj,
        'title_page': 'search ',
    }
    return render(
        request,
        'contact/pages/index.html',
        context,
                )

##########################################CRUD#########################################################CRUD#####################

def create(request):
    form_action = reverse('create')
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contato = form.save()
            return redirect('update', id=contato.pk)

        return render(
            request,
            'contact/pages/create.html',
            context
        )

    context = {
        'form': contactForm(),
        'form_action': form_action,
    }

    return render(
            request,
            'contact/pages/create.html',
            context
        )

def update(request, id):
    contact = get_object_or_404(Contact, pk=id, show=True)
    form_action = reverse('update', args=(id,))
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contato = form.save()
            return redirect('update', id=contato.pk)

        return render(
            request,
            'contact/pages/create.html',
            context
        )

    context = {
        'form': contactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
            request,
            'contact/pages/create.html',
            context
        )

def delete(request, id):
    contact = get_object_or_404(Contact, pk=id, show=True)

    confirmation = request.POST.get('confirmation', 'no')
    confirmation_del = request.POST.get('confirmation_del')
    messages.info(request, "Deseja realmente deleta o contato?")
    if confirmation_del == 'del':
        contact.delete()
        return redirect('index')
    
    if confirmation_del == 'cancel':
        return redirect ('contact', id=contact.pk)

    
    return render(request, 'contact/pages/contact.html',{
        'contact': contact,
        'confirmation': confirmation,
    })

##########################################ENDCRUD#########################################################ENDCRUD#####################

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Usuário registrado com sucesso!')
            return redirect('register')
    return render(request, 'contact/pages/register.html', {
        'form': form,
    })

def login(request):
    form = loginUser()
    if request.method == 'POST':
        form = loginUser(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request,'Logado com sucesso!')
        else:
            messages.error(request, 'Login inválido.')

    return render(request, 'contact/pages/login.html', {
        'form': form
    })

def logoff(request):
    auth.logout(request)
    return redirect('login')


    # form = AuthenticationForm(request)
    # if request.method == 'POST':
    #     form = AuthenticationForm(request, data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         messages.success(request,'Usuário registrado com sucesso!')

    # return render(request, 'contact/pages/login.html', {
    #     'form': form
    # })