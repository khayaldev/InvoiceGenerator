from re import template
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  FormView,
                                  TemplateView,
                                  DetailView,
                                  UpdateView,
                                  RedirectView,
                                  DeleteView)
from .models import Invoice
from positions.models import Position
from profiles.models import Profile
from .forms import InvoiceForm
from positions.forms import PositionForm
from django.urls import reverse
from django.contrib import messages
from .mixins import InvoiceClosedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required

# Create your views here.


class InvoiceListView(LoginRequiredMixin,ListView):
  model=Invoice
  template_name='invoices/main.html' 
  paginate_by=3
  # context_object_name  #object_list
  
  def get_queryset(self):
    profile=get_object_or_404(Profile,user=self.request.user)
    # profile=Profile.objects.get(user=self.request.user)
    return super().get_queryset().filter(profile=profile).order_by('-created')
    
    
class InvoiceFormView(LoginRequiredMixin,FormView):
  form_class=InvoiceForm
  template_name='invoices/create.html'
  # success_url=reverse_lazy('invoices:main')
  i_instance=None
  
  def get_success_url(self):
    print(self.i_instance)
    return reverse('invoices:details', kwargs={'pk':self.i_instance.pk})
  
  def form_valid(self,form):
    profile=get_object_or_404(Profile,user=self.request.user)
    instance=form.save(commit=False)
    instance.profile=profile
    form.save() 
    self.i_instance=instance
    return super().form_valid(form)
  
class InvoiceTemplateView(LoginRequiredMixin,DetailView):
  model=Invoice
  template_name='invoices/invoice_template.html'
  
  
class PositionFormView(FormView):
  form_class=PositionForm
  template_name='invoices/details.html'
  
  def get_success_url(self):
      return self.request.path

  def form_valid(self,form):
    invoice_pk=self.kwargs['pk']
    invoice_obj=Invoice.objects.get(pk=invoice_pk)
    instance=form.save(commit=False)
    instance.invoice=invoice_obj
    form.save()
    messages.info(self.request,f'Position added succesfully to the {invoice_obj.number}')
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    invoice_obj=Invoice.objects.get(pk=self.kwargs['pk'])
    qs=invoice_obj.positions
    context["invoice_obj"] =invoice_obj
    context['qs']=qs
    return context

    
  
    
class InvoiceUpdateView(LoginRequiredMixin,InvoiceClosedMixin,UpdateView):
  model=Invoice
  template_name="invoices/update.html"
  success_url=reverse_lazy('invoices:main')
  form_class=InvoiceForm
  
  def form_valid(self,form):
    instance=form.save()
    messages.success(self.request,f'Invoice - {instance.number} succesfully updated')

    return super().form_valid(form)
  
  
class InvoiceRedirectView(RedirectView):
  pattern_name="invoices:details"
  
  def get_redirect_url(self, *args, **kwargs):
      invoice_pk=self.kwargs['pk']
      invoice_obj=Invoice.objects.get(pk=invoice_pk)
      invoice_obj.closed=True
      invoice_obj.save()
      return super().get_redirect_url(*args, **kwargs)
    
    
class PositionDeleteView(LoginRequiredMixin,InvoiceClosedMixin,DeleteView):
  model=Position
  template_name="invoices/position_delete_confirm.html"
  
  def get_object(self):
    pk=self.kwargs['position_pk']
    
    object=Position.objects.get(pk=pk)
    return object
  def get_success_url(self):
      messages.info(self.request,"Position deleted succesfully")
      return reverse('invoices:details',kwargs={'pk':self.object.invoice.id})
    
@login_required  
def render_pdf_view(request,**kwargs):
    pk=kwargs['pk']
    obj=Invoice.objects.get(pk=pk)
    
    font_result=finders.find('fonts/Poppins-Medium.ttf')
    searched_locations=finders.searched_locations
    
    
    template_path = 'invoices/pdf1.html'
    context = {'object':obj,'static':{
      'font':font_result
    }}
    print(obj.profile.company_logo)
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
  
  