from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .utils import chatbot_reply
from .models import ChatHistory

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")
        response = chatbot_reply(message)
        ChatHistory.objects.create(message=message, response=response)
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Invalid request"}, status=400)

def chat_page(request):
    return render(request, "chat.html")
