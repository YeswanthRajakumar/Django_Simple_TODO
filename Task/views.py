from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import TaskCreationForm


# Create your views here.
def task_List(request):
    queryset = Notes.objects.all()
    context = \
        {
            'tasks': queryset
        }
    return render(request, template_name='Task/list.html', context=context)


def Create_task(request):
    form = TaskCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('task-list')
    else:
        return render(request, template_name='Task/create.html', context={'form': form})


def Update_task(request, id):
    print("Moving into Update_task")
    instance = get_object_or_404(Notes, id=id)
    print(instance)
    form = TaskCreationForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        print("Requesting post method")
        if form.is_valid():
            print("form validated")
            form.save()
            print("form saved")
            return redirect('task-list')
    else:
        return render(request, template_name='Task/update.html', context={'form': form})


def Delete_task(request, id):
    print(id)
    task_to_delete = get_object_or_404(Notes, id=id)
    task_to_delete.delete()
    print('Deleted')
    return redirect('task-list')
