from django.shortcuts import render

from django.http import HttpResponse
# from hubit.models import Blog


def home(reqeuest):

    return HttpResponse('hello world')