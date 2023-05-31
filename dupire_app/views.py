from django.shortcuts import render, redirect
from django.contrib import messages
import sys
import os
from pathlib import Path
from django.template import loader

import pandas


def home(request):

    return render (request, 'home.html')