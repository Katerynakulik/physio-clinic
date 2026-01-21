from django.shortcuts import render
from accounts.models import Physiotherapist


def home(request):
    """
    Render the clinic home page with a short intro and
    a list of physiotherapists pulled from the database.
    """
    physiotherapists = Physiotherapist.objects.all()[:3]

    return render(
        request,
        "clinic/home.html",
        {"physiotherapists": physiotherapists},
    )