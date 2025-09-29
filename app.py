import os
import requests
import gradio as gr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
MODEL_NAME = "x-ai/grok-4-fast:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# ------------------ API CALL ------------------
def chat_with_model(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# ------------------ CHAT FUNCTIONS ------------------
def user_message(user_input, history):
    if not history:
        history = []

    # Add user message
    history.append({"role": "user", "content": user_input})

    # Typing indicator
    yield history + [{"role": "assistant", "content": "💬 typing..."}], ""

    # Get model reply
    reply = chat_with_model(history)
    history.append({"role": "assistant", "content": reply})

    yield history, ""

def clear_chat():
    return [],

# ------------------ UI ------------------
with gr.Blocks(css="""
    body { font-family: 'Segoe UI', sans-serif; background: #f9f9f9; }
    #title { text-align: center; font-size: 28px; font-weight: bold; margin-bottom: 8px; }
    #subtitle { text-align: center; font-size: 14px; margin-bottom: 20px; color: gray; }
    .gr-chatbot { border-radius: 12px; box-shadow: 0px 4px 10px rgba(0,0,0,0.08); }
    .gr-textbox textarea { border-radius: 8px; font-size: 14px; }
    .gr-button { border-radius: 8px; font-weight: 600; }
""") as demo:
    gr.HTML("<div id='title'>🤖 Chatbot</div>")
    gr.HTML(f"<div id='subtitle'>Made by somyasiddarth | Model: {MODEL_NAME}</div>")

    chatbot = gr.Chatbot(
    height=400,
    type="messages"  # ensures OpenAI-style dicts are used
)


    with gr.Row():
        user_inp = gr.Textbox(
            placeholder="Type your message here...",
            show_label=False,
            scale=8
        )
        send_btn = gr.Button("Send", variant="primary")
        clear_btn = gr.Button("🗑️ Clear", variant="secondary")

    # Events
    user_inp.submit(user_message, [user_inp, chatbot], [chatbot, user_inp])
    send_btn.click(user_message, [user_inp, chatbot], [chatbot, user_inp])
    clear_btn.click(lambda: [], None, chatbot)


# ------------------ RUN ------------------
if __name__ == "__main__":
    demo.queue().launch()

