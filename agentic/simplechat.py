import gradio as gr
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma4:e2b", temperature=0.0)

agent = create_agent(model=llm)

def chat_and_control(message, history):
    try:
        messages = []
        messages.extend(history)
        messages.append({"role": "user", "content": message})
        response = agent.invoke({"messages": messages})
        return response["messages"][-1].content
    except Exception as e:
        return f"Execution loop logging: {str(e)}"

demo = gr.ChatInterface(
    fn=chat_and_control,
    title="🤖 Local LLM Agent",
    description="Powered by Gemma 4 Edge 2B via Ollama. Interacting directly with the filesystem and VLC engine."
)

demo.launch(server_name="127.0.0.1", server_port=7860, share=False)