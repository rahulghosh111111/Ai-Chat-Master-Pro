import google.generativeai as genai

# PASTE YOUR KEY DIRECTLY HERE FOR THIS TEST
api_key = "AIzaSyDMfX8zvsWPByebosLXQ5gxyP8lKs93vA8" 

genai.configure(api_key=api_key)

print("Attempting to list models...")
try:
    available_models = list(genai.list_models())
    if not available_models:
        print("❌ connection successful, but NO models found. Check if 'Generative Language API' is enabled in Google Cloud Console.")
    
    for m in available_models:
        # We only care about models that can generate text
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ FOUND: {m.name}")
            
except Exception as e:
    print(f"❌ CRITICAL ERROR: {e}")