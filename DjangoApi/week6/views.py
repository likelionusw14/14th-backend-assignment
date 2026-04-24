from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

# 초기 데이터
lions = [
    {"id": 1, "name": "아기사자1", "track": "Django"},
    {"id": 2, "name": "아기사자2", "track": "SpringBoot"},
]
next_id = 3

def lion_list(request):
    keyword = request.GET.get('keyword', '')
    
    filtered_lions = lions
    if keyword:
        filtered_lions = [lion for lion in filtered_lions if keyword in lion['name']]
        
    return render(request, 'lions/list.html', {
        'lions': filtered_lions,
        'keyword': keyword,
    })

def lion_create(request):
    if request.method == 'POST':
        global next_id
        name = request.POST.get('name')
        track = request.POST.get('track')
        
        new_lion = {
            "id": next_id,
            "name": name,
            "track": track
        }
        lions.append(new_lion)
        next_id += 1
        return redirect('lion_detail', id=new_lion['id'])
    
    return render(request, 'lions/new.html')

def lion_detail(request, id):
    lion = next((lion for lion in lions if lion['id'] == id), None)
    if not lion:
        return redirect('lion_list')
    return render(request, 'lions/detail.html', {'lion': lion})

def lion_edit(request, id):
    lion = next((lion for lion in lions if lion['id'] == id), None)
    if not lion:
        return redirect('lion_list')
        
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        
        lion['name'] = name
        lion['track'] = track
        return redirect('lion_detail', id=id)
        
    return render(request, 'lions/edit.html', {'lion': lion})

def lion_delete(request, id):
    if request.method == 'POST':
        global lions
        lions = [lion for lion in lions if lion['id'] != id]
    return redirect('lion_list')
