from django.shortcuts import render

from . import util
import markdown2
from markdown2 import Markdown
import random

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
def new(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['md']
        titleExist = util.get_entry(title) # i want to change this to if title in list entries...
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Encyclopedia entry already exists"
            })
        else:
            util.save_entry(title, content)
            html= md_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html
            })

    else:
        return render(request, "encyclopedia/new.html")

# function to edit contents of an entry
def edit(request):
     if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

# save edited entry
def save(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['md']
        util.save_entry(title, content)
        html = md_html(title)

        return render(request,"encyclopedia/entry.html", {
            "title": title,
            "content": html
        })

# function to take user to random encyclopedia page
def random(request):
    entries = util.list_entries()
    randompage = random.choice(entries)
    content = md_html(randompage)
    return render(request, "encyclopedia/entry.html", {
        "title": randompage,
        "content": content
    })

