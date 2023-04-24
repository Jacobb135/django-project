from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat your veggies!",
    "february": "Walk for at least 20 minutes a day",
    "march": "Learn Django for at least 20 minutes a day",
    "april": "Eat your veggies!",
    "may": "Walk for at least 20 minutes a day",
    "june": "Learn Django for at least 20 minutes a day",
    "july": "Eat your veggies!",
    "august": "Walk for at least 20 minutes a day",
    "september": "Learn Django for at least 20 minutes a day",
    "october": "Eat your veggies!",
    "november": "Walk for at least 20 minutes a day",
    "december": None,
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
        })
    except:
        raise Http404()
