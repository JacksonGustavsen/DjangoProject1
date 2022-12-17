#!/usr/bin/env python
__author__ = "Jackson Gustavsen"
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, World! Jackson Gustavsen")
