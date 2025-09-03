# from cabin.models import *
from django.db.models import Sum, Count
from cabin.models import Driver, Payment, RideRequest, Rider


def query_0():
    q = Driver.objects.all()
    return q


def query_1():
    q = Payment.objects.aggregate(income=Sum("amount"))
    return q


def query_2(x):
    q = Payment.objects.filter(ride__request_rider__id=x).aggregate(
        paynet_sum=Sum("amount")
    )
    return q


def query_3():
    q = Driver.objects.filter(car__car_type="A").distinct().count()
    return q


def query_4():
    q = RideRequest.objects.filter(ride__isnull=True)
    return q


def query_5(t):
    q = Rider.objects.annotate(
        total=Sum("riderequest__ride__payment__amount").filter(total__gte=t)
    )
    return q


def query_6():
    q = (
        Driver.objects.annotate(n=Count("car"))
        .order_by("-n", "account__last_name")
        .first()
    )
    return q


def query_7():
    q = "your query here"
    return q


def query_8(x):
    q = "your query here"
    return q


def query_9():
    q = "your query here"
    return q


def query_10():
    q = "your query here"
    return q


def query_11(n, c):
    q = "your query here"
    return q


def query_12(n, c):
    q = "your query here"
    return q


def query_13(n, m):
    q = "your query here"
    return q


def query_14(x, y, r):
    q = "your query here"
    return q


def query_15(n, c):
    q = "your query here"
    return q


def query_16(x, t):
    q = "your query here"
    return q


def query_17():
    q = "your query here"
    return q


def query_18():
    q = "your query here"
    return q


def query_19(n, t):
    q = "your query here"
    return q


def query_20():
    q = "your query here"
    return q
