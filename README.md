# ChatBot
An interactive chatbot built with **Gradio** and **OpenRouter’s Grok-4 model**. Chat with the AI in real-time with a clean and responsive UI.

---

## Features

- Modern chat interface with **typing indicator**.
- **Clear chat** button to reset conversation.
- Responsive UI for both desktop and mobile.
- Easy to customize colors, title, and model.

---

## Usage

1. Type a message in the **textbox**.  
2. Press **Enter** or click **Send**.  
3. Chatbot replies instantly.  
4. Use **🗑️ Clear** to reset the conversation.

---

## Customization

- Change **AI model**: update `MODEL_NAME` in `app.py`.  
- Update **UI style**: edit CSS in `gr.Blocks(css=...)`.  
- Set your API key via Hugging Face **Secrets** or `.env` for local testing.

---

## Dependencies

- `gradio`  
- `requests`  
- `python-dotenv`

Install via:

```bash
pip install -r requirements.txt

