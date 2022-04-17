from django.contrib.auth.forms import UserCreationForm  # 新增
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View, TemplateView


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)


class HomePage(TemplateView):
	template_name = 'home.html'
