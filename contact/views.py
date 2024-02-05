from django.shortcuts import render
from contact import models

# Create your views here.
def index(request):
    # contacts = models.Contact.objects.all().order_by('id')
    contacts = models.Contact.objects.filter(show=True).order_by('id')[0:10]

    # print(contacts.query)

    context = {
        'contacts' : contacts,
    }
    return render(request,
                  'contact/pages/index.html',
                  context,
                  )
def Contactid(request, id):
    # single_contact = models.Contact.objects.get(pk=id_contact),
    single_contact = models.Contact.objects.get(pk=id),

    # print(contacts.query)

    context = {
        'contact' : single_contact,
    }
    return render(request,
                  'contact/pages/contact.html',
                  context,
                  )