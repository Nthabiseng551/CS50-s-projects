from django.shortcuts import render

from . import util
import markdown2 

# Convert markdown content to HTML
def md_converter(title):
    markdowner = Markdown()
    content = util.get_entry(title)
    if content == None:
        return None
    return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

     if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html", {
            "message:" "The requested page not found"
        })

     return render(request,"encyclopedia/entry.html", {
         "title": title,
         "content": converter(title)
    })

