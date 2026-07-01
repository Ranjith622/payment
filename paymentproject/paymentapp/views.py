import razorpay

from django.conf import settings
from django.shortcuts import render


def home(request):

    amount = 500 * 100

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        "payment": payment,
        "amount": amount,
        "key": settings.RAZORPAY_KEY_ID
    }

    return render(request, "payment.html", context)

def success(request):
    return render(request, "success.html")