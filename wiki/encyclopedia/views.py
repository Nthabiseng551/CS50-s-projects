from django.shortcuts import render

from . import util
import markdown2
from markdown2 import Markdown

# markdown2.markdown(content)
def md_html(title):
    markdowner = Markdown()
    if util.get_entry(title) == None:
        return None
    return markdowner.convert(util.get_entry(title))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = md_html(title)
    if content == None:
        return render(request, "encyclopedia/error.html", {
            "message:" "The requested page not found"
        })

    return render(request,"encyclopedia/entry.html", {
         "title": title,
         "content": content
    })

def search(request):
    if request.method == "POST":
        search = request.POST["q"]
        content = md_html(search)
        if content is not None:
            return render(request, "encyclopedia/entry.html",{
                "title": search,
                "content": content
            })
        
