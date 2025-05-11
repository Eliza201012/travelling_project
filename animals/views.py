from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("<h1> Я їду в подорож </h1>")

def new_animal(request):
    return HttpResponse("<ul> <li> Я бачила рибку дорі </li> </ul>")