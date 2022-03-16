from django.shortcuts import render, redirect
from .forms import CollegeForm
from .models import CollegeModel


def show(request):
    colleges = CollegeModel.objects.all()
    context = {'colleges':colleges}
    return render (request, 'college/show.html', context)

def add(request):
    form=CollegeForm()
    if request.method == 'POST':
        form=CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
        else:
            form = CollegeForm()
    context={'form': form}
    return render (request, 'college/add.html', context)

def edit(request,pk):
    colleges = CollegeModel.objects.get(id=pk)
    form = CollegeForm(instance=colleges)
    if request.method == 'POST':
        form=CollegeForm(request.POST , instance=colleges)
        if form.is_valid():
            form.save()
            return redirect('show')
        # else:
        #     form = CollegeForm()
    context={'form':form}
    return render (request, 'college/edit.html',context)

def delete(request,pk):
    colleges = CollegeModel.objects.get(id=pk)
    if request.method == 'POST':
        colleges.delete()
        return redirect('show')
    context={'college':colleges}
    return render (request, 'college/delete.html',context)