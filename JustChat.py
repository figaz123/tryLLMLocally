import gradio as gr
import ollama
import re

def ollama_chat_only(question, history):
    response = ollama.chat(
        model="deepseek-r1",

        messages=[{"role": "user", "content": question}],
    )

    response_content = response["message"]["content"]

    # Optional: clean up thinking tags
    final_answer = re.sub(r"<think>.*?</think>", "", response_content, flags=re.DOTALL).strip()
    return final_answer

chatbot = gr.ChatInterface(
    fn=ollama_chat_only,
    title="Chat with DeepSeek",
    description="Ask anything and get an answer from DeepSeek-R1.",
    theme="soft",
    examples=["What is deep learning?", "Tell me a joke", "What's the capital of France?"]
)

chatbot.launch()
