from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import TaskCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, template_name='Task/dashboard.html')


def task_List(request):
    current_user = request.user
    queryset = Notes.objects.filter(user=current_user)
    context = \
        {
            'tasks': queryset,
            'user': current_user
        }
    return render(request, template_name='Task/list.html', context=context)


def Create_task(request):
    form = TaskCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
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
