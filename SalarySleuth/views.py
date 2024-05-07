from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'test.html')


def login(request):
    #return HttpResponse("This is the login page.")
    return render(request, 'login.html')


def logout(request):
    return HttpResponse("This is the logout page.")


def register(request):
    #return HttpResponse("This is the register page.")
    return render(request, 'register.html')

def companies(request):
    return HttpResponse("This is the list of companies.")


def company_detail(request, cid):
    return HttpResponse(f"This is the detail view for company {cid}.")


def listings(request):
    #return HttpResponse("This is the listings page.")
    return render(request, 'listings.html')


def listing_detail(request, lid):
    #return HttpResponse(f"This is the detail view for listing {lid}.")
    return render(request, 'listing_detail.html',{lid:"dataset"})


def choose_info(request, uid, lid):
    #return HttpResponse(f"This is the profile page for user {uid}.")
    return render(request, 'choose_info.html',{lid:uid})


def profile(request, uid):
    #return HttpResponse(f"This is the profile page for user {uid}.")
    return render(request, 'profile.html',{uid:"dataset"})


def profile_listings(request, uid):
    return HttpResponse(f"These are the listings for user {uid}.")


def applications(request, uid):
    return HttpResponse(f"These are the applications for user {uid}.")


def profile_listing_detail(request, uid, lid):
    return HttpResponse(f"This is the detail view for listing {lid} of user {uid}.")


def listing_applicants(request, uid, lid):
    return HttpResponse(f"These are the applicants for listing {lid} of user {uid}.")


def applicant_detail(request, uid, lid, aid):
    return HttpResponse(f"This is the detail view for applicant {aid} for listing {lid} of user {uid}.")
