from django.db.models import OrderWrt
from django.db.models.expressions import OrderBy
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def cancel_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = OrderBy.objects.get(id=order_id)
            order.status = 'canceled'  # Assuming you have a 'status' field in your Order model
            order.save()
            # Implement refund logic here if applicable

            return HttpResponse(json.dumps({'message': 'Order canceled successfully.'}), content_type='application/json')
        except OrderWrt.DoesNotExist:
            return HttpResponse(json.dumps({'message': 'Order not found.'}), content_type='application/json')
    return HttpResponse(json.dumps({'message': 'Invalid request method.'}), content_type='application/json')