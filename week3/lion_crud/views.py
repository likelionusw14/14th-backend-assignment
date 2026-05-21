from django.shortcuts import render,redirect

lions = []

next_id = 1

def index(request):
    return render(request, 'baby_lion/index.html', {'lions':lions})

def lion_new(request):
    global next_id
    if request.method == 'POST':
        name = request.POST.get('name')
        track = request.POST.get('track')
        if not name or not track:
            return render(request, 'baby_lion/new.html', {
                'error_message': '이름과 트랙을 입력해주세요!'
            })
        lion = {
            'id': next_id,
            'name': name,
            'track': track,
        }
        lions.append(lion)
        next_id +=1
        return redirect('index')
    return render(request, 'baby_lion/new.html')
    
def lion_detail(request, id):
    lion = next((item for item in lions if item['id']==int(id)), None)
    return render(request, 'baby_lion/detail.html', {'lion': lion})

def lion_list(request):
    global lions
    keyword = request.GET.get('keyword')
    filtered = [item for item in lions if item['name'] == keyword]
    return render(request, 'baby_lion/index.html', {'lions' : filtered})


def lion_edit(request,id):
    global lions
    lion = next((item for item in lions if item['id'] == int(id)) , None)
    if request.method == 'POST':
        lion['name'] = request.POST.get('name')
        lion['track'] = request.POST.get('track')
        return redirect('index')
    return render(request, 'baby_lion/edit.html', {'lion': lion})

def lion_delete(request,id):
    global lions
    if request.method == 'POST':
        lions[:] = [item for item in lions if item['id'] != int(id)]
        return redirect('index')
    return render(request, 'baby_lion/detail.html')
        