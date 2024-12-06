import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env dosyasını yükler ve içerisindeki değişkenleri sisteme ekler.
load_dotenv()

# .env dosyasından API Key'i okur
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Generative AI kütüphanesini GOOGLE_API_KEY ile yapılandırır
genai.configure(api_key=GOOGLE_API_KEY)

# Kullanacağımız Generative AI modelini tanımlıyoruz
model = genai.GenerativeModel('gemini-1.5-flash')


def give_response(chat_history, soru):
    # Sorumuza geçmiş konuşmalarımızı da ekliyoruz
    prompt = f"{chat_history}\nuser: {soru}\nassistant:"

    # Hazırlanan prompt'u modele gönderir ve modelin oluşturduğu içeriği döndürür
    response = model.generate_content(prompt)

    return response.text  # Modelden gelen yanıtın sadece metin kısmını döndürür