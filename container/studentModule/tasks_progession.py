from celery.result import AsyncResult
import json
from django.http import JsonResponse


def vd(myvar):
    json_lisible = json.dumps(myvar, indent=4)
    print(json_lisible)

def get_progress_level(request, payment_lot=None):
    for i, group in enumerate(request.session['payment_tasks']):
        if group['payment_lot'] == payment_lot :
            for id in group['payment_ids']:
                if isDone(id):
                    request.session['payment_tasks'][i]['payment_ids'].remove(id)
                    request.session.modified = True
            done_tasks_count = len(request.session['payment_tasks'][i]['payment_ids'])
            total_tasks_count = request.session['payment_tasks'][i]['task_count']
            return get_percent(done_tasks_count, total_tasks_count)
            break

def get_percent(level, max):
    if max == 0:
        return 0
    return 100 - (level*100)/max

def add_new_payment_group(request,group):
    if 'payment_tasks' not in request.session:
        request.session['payment_tasks'] = []

    request.session['payment_tasks'].append(group)
    print(request.session['payment_tasks'])
    request.session.modified = True

def get_task_info(request):
    lot = int(request.POST.get('lot_id', None))
    print(lot)
    level = get_progress_level(request, payment_lot=lot)
    return JsonResponse({lot: level})

def isDone(task_id):
    task = AsyncResult(task_id)
    if task.ready(): 
        return True
    return False
