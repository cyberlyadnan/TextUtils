
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     # with open("demo.txt", "r") as file:
#     #     data = file.read()
#     return HttpResponse(f"This is the Home Page")
# def about(request):
#     return HttpResponse("This is the about page")


def index(request):
    return render(request, "index.html")

def analyze(request):
    djtext = request.POST.get("text", "Default")
    remove_punc = request.POST.get("removepunc", "off")
    full_caps = request.POST.get("fullCaps", "off")
    new_line_remover = request.POST.get("newlineremover", "off")
    extra_space_remover = request.POST.get("extraspaceremover", "off")

    punctuation_marks = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''


    analyzed_caps = djtext.upper() if full_caps == "on" else djtext
    analyzed_no_punc = "".join(char for char in analyzed_caps if char not in punctuation_marks) if remove_punc == "on" else analyzed_caps
    analyzed_no_newline = analyzed_no_punc.replace("\n", "").replace("\r", "") if new_line_remover == "on" else analyzed_no_punc
    analyzed_no_extra_space = " ".join(analyzed_no_newline.split()) if extra_space_remover == "on" else analyzed_no_newline

    params = {
        "purpose": "No Option Selected",
        "original_text": djtext,
        "analyzed_text": analyzed_no_extra_space,
    }

    if full_caps == "on":
        params["purpose"] = "Convert To UpperCase"

    if remove_punc == "on":
        params["purpose"] = "Remove Punctuation"

    if new_line_remover == "on":
        params["purpose"] = "New Line Remover"

    if extra_space_remover == "on":
        params["purpose"] = "Extra Space Remover"

    return render(request, "analyze.html", params)










