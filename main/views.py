from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def feed(request):
    content = "Текст поста. Lorem ipsum dolor sit amet, consectetur adipiscing elit Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet\
        Lorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit ametLorem ipsum dolor sit amet"
    context = {"content": content}
    return render(request, "main/feed.html", context=context)