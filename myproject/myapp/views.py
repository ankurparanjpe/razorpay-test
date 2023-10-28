# views.py
import razorpay
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import json
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'create_payment.html', context)

def create_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = int(data['amount'])  # Amount in paisa
            description = data['description']
            email = data['email']

            client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
            data = {
                'amount': amount,
                'currency': 'INR',
                'receipt': 'order_rcptid_11',
                'payment_capture': 1  # Auto-capture the payment
            }
            order = client.order.create(data=data)

            return JsonResponse({
                'key': settings.RAZORPAY_API_KEY,
                'amount': amount,
                'description': description,
                'email': email,
                'id': order.get('id')
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def test_path(request):
    return HttpResponse('<h1>Successful</h1>')