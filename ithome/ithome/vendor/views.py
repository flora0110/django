
from django.views.generic import ListView, DetailView  # 新增
from django.shortcuts import get_object_or_404  # 新增
from django.http import Http404
from .forms import VendorForm, RawVendorForm  # 要記得 import 相對應的 Model Form 唷!
from django.shortcuts import render
from .models import Vendor
# Create your views here.

'''
def showtemplate(request):
    vendor_list = Vendor.objects.all()  # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list}  # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendors\detail2.html', context)
'''


def showtemplate(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    # print(vendor_list)
    return render(request, 'vendors/detail.html', context)

# 針對 vendor_create.html


def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    print(form)
    print(form.cleaned_data)
    if form.is_valid():
        Vendor.objects.create(**form.cleaned_data)  # 新增
        form = RawVendorForm()

    context = {
        'form': form
    }
    return render(request, "vendors/vendor_create.html", context)


def singleVendor(request, id):
    vendor_list = get_object_or_404(Vendor, id=id)
    # try:
    #     vendor_list = Vendor.objects.get(id=id)
    # except Vendor.DoesNotExist:
    #     raise Http404
    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendors/vendor_detail.html', context)


# Create your views here.
# 繼承 ListView

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_list.html'

# 繼承 DetailView


class VendorDetail(DetailView):
    model = Vendor
    # queryset = Vendor.objects.all()
    template_name = 'vendors/vendor_detail2.html'
