from google import genai

# NOTE: The current API key has been denied access or has exhausted its quota.
# Please generate a new API key from https://aistudio.google.com/
client = genai.Client(api_key="AIzaSyBi1uJs5ZGbzQrV4gjMGgxQlZOUb25hfS4")

def get_response(message):
    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash-latest',
            contents=message,
        )
        return response.text if response.text else "No response"
    except Exception as e:
        error_msg = str(e)
        print("FULL ERROR:", error_msg)
        
        if "403" in error_msg or "PERMISSION_DENIED" in error_msg:
            return "❌ **Access Denied (403)**\n\nYour Google Project has blocked this API key. \n\n**To fix this:**\n1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).\n2. Create a **New Project** (don't use the old one).\n3. Generate a fresh API key and paste it into `chatbot.py`."
        
        if "400" in error_msg or "INVALID_ARGUMENT" in error_msg:
            return "⚠️ **Invalid API Key (400)**\n\nThe API key you entered (`AIzaSyBi...`) is not recognized by Google. Please double-check that you copied the **entire** key correctly from AI Studio."
            
        if "429" in error_msg:
            return "⏳ **Quota Exhausted (429)**\n\nYou have sent too many messages. Please wait a minute or use a different API key."

        return f"🤖 **AI Service Error**\n\n{error_msg[:150]}"