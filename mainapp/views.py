from django.shortcuts import render


def main(request):
    return render(request, "mainapp/index.html")


def shop(request):
    return render(request, "mainapp/shop.html")


def about(request):
    return render(request, "mainapp/about.html")


def contact(request):
    return render(request, "mainapp/contact.html")
