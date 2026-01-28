from django.shortcuts import render
from .forms import ChatForm
import google.generativeai as genai

def chatbot_view(request):
    response_text = ""
    error_message = ""

    genai.configure(api_key="AIzaSyAbOmXC1yY-yaQNDU2EGiGAQVuQzMKETnc")

    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data["prompt"]

            try:
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(prompt)
                response_text = response.text
            except Exception as e:
                error_message = f"Error: {e}"
    else:
        form = ChatForm()

    return render(request, "chatbot/chat.html", {
        "form": form,
        "response": response_text,
        "error": error_message
    })
