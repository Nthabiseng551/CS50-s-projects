from django.shortcuts import render

from . import util
import markdown2
from markdown2 import Markdown

# convert markdown content to html
def md_html(title):
    markdowner = Markdown()
    if util.get_entry(title) == None:
        return None
    return markdowner.convert(util.get_entry(title))

# define index page
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# define entry page (display content of specific entry)
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

# function to search for encyclopedia entry
def search(request):
    if request.method == "POST":
        search = request.POST["q"]
        content = md_html(search)
        if content is not None:
            return render(request, "encyclopedia/entry.html",{
                "title": search,
                "content": content
            })
        else:
            entries = util.list_entries()
            recommendation = []
            for entry in entries:
                if search.upper() in entry.upper():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })

# function to create new page/ encyclopedia entry
def new(request, ):
