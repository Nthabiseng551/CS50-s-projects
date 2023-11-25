from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import util
import markdown2
from markdown2 import Markdown
import random


# convert markdown content to html
def md_html(title):
    markdowner = Markdown()
    if util.get_entry(title) != None:
        return markdowner.convert(util.get_entry(title))
    return None


# define index page
def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


# define entry page (display content of specific entry)
def entry(request, title):
    if util.get_entry(title) == None:
        return render(
            request,
            "encyclopedia/error.html",
            {"message:" "The requested page not found"},
        )

    return render(
        request, "encyclopedia/entry.html", {"title": title, "content": md_html(title)}
    )


# function to search for encyclopedia entry
@csrf_exempt
def search(request):
    if request.method == "POST":
        input = request.POST["q"]

        if util.get_entry(input) != None:
            return render(
                request,
                "encyclopedia/entry.html",
                {"title": input, "content": md_html(input)},
            )
        else:
            entries = util.list_entries()
            search_results = []
            for entry in entries:
                if input.upper() in entry.upper():
                    search_results.append(entry)
            return render(
                request, "encyclopedia/search.html", {"search_results": search_results}
            )


# function to create new page/ encyclopedia entry
@csrf_exempt
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["md"]

        if title in util.list_entries():
            return render(
                request,
                "encyclopedia/error.html",
                {"message": "Encyclopedia entry already exists"},
            )
        else:
            util.save_entry(title, content)
            return render(
                request,
                "encyclopedia/entry.html",
                {"title": title, "content": md_html(title)},
            )

    else:
        return render(request, "encyclopedia/new.html")


# function to edit contents of an entry
@csrf_exempt
def edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        return render(
            request,
            "encyclopedia/edit.html",
            {"title": title, "content": util.get_entry(title)},
        )


# save edited entry
@csrf_exempt
def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["md"]
        util.save_entry(title, content)

        return render(
            request,
            "encyclopedia/entry.html",
            {"title": title, "content": md_html(title)},
        )


# function to take user to random encyclopedia page
def r_entry(request):
    entries = util.list_entries()
    randompage = random.choice(entries)

    return render(
        request,
        "encyclopedia/entry.html",
        {"title": randompage, "content": md_html(randompage)},
    )
