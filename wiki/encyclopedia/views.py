from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
     if None:
        return render(request, "encyclopedia/error.html")

     return render(request,"encyclopedia/entry.html", {
        "entries": util.get_entry(title)
    })

