import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

import google.generativeai as genai
from backend.settings import GEMINI_API_KEY

print("🔍 Probando conexión con Gemini...")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-exp')

response = model.generate_content("Hola")
print(" V Gemini responde:")
print(response.text)
