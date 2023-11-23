from django.shortcuts import render

from . import util
from markdown2 import Markdown

# Convert markdown content to HTML
def converter(title):
    markdowner = markdown.Markdown()
    
    if util.get_entry(title) == None:
        return None
    return markdowner.convert(util.get_entry(title))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
     if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")

     return render(request,"encyclopedia/entry.html", {
        "entries": util.get_entry(title)
    })

