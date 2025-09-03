# from cabin.models import *
from django.db.models import Sum
from cabin.models import Driver, Payment


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
    q = "your query here"
    return q


def query_4():
    q = "your query here"
    return q


def query_5(t):
    q = "your query here"
    return q


def query_6():
    q = "your query here"
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
