from dotenv import load_dotenv
import os
import json
import requests
from pypdf import PdfReader
import gradio as gr
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv(override=True)

# 🔔 Push notification via Pushover
def push(text):
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": text,
        }
    )

# 📩 Tool: record user details
def record_user_details(email, name="Name not provided", notes="not provided"):
    push(f"Recording {name} with email {email} and notes {notes}")
    return {"recorded": "ok"}

# ❓ Tool: record unknown question
def record_unknown_question(question):
    push(f"Unknown Question: {question}")
    return {"recorded": "ok"}

# 🧰 Tool schemas
record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "description": "User's email"},
            "name": {"type": "string", "description": "User's name"},
            "notes": {"type": "string", "description": "Contextual notes"},
        },
        "required": ["email"],
    }
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Use this tool to record any question the AI could not answer.",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "The unknown question"},
        },
        "required": ["question"],
    }
}

tools = [record_user_details_json, record_unknown_question_json]

class Me:
    def __init__(self):
        self.name = "Ritesh Thakur"
        self.llm = Ollama(model="openchat")

        reader = PdfReader("me/linkedin.pdf")
        self.linkedin = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.linkedin += text

        with open("me/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()

    def system_prompt(self):
        return f"""
You are acting as {self.name}. You are answering questions on {self.name}'s website related to his skills, experience, and career.
Your job is to represent {self.name} professionally to potential employers or collaborators.
You have access to a summary and a LinkedIn profile.

If a user asks something you cannot answer, record it using the `record_unknown_question` tool.

If the user seems interested in contacting, ask for their email and record it using `record_user_details`.

Summary:
{self.summary}

LinkedIn:
{self.linkedin}

Only speak as {self.name}. Do not break character.
"""

    def parse_tool_call(self, response_text):
        try:
            data = json.loads(response_text)
            if isinstance(data, dict) and "tool_name" in data and "parameters" in data:
                return data
        except:
            return None
        return None

    def handle_tool_call(self, tool_data):
        tool_name = tool_data["tool_name"]
        args = tool_data["parameters"]
        func = globals().get(tool_name)
        if func:
            result = func(**args)
            return f"(Tool executed: {tool_name}) → {result}"
        return "(Unknown tool)"

    def chat(self, message, history):
        full_prompt = self.system_prompt() + f"\n\nUser: {message}\n\nRespond as {self.name}:"
        response = self.llm(full_prompt)

        # Try to parse tool call if it's in JSON
        tool_data = self.parse_tool_call(response)
        if tool_data:
            return self.handle_tool_call(tool_data)

        return response

if __name__ == "__main__":
    me = Me()
    gr.ChatInterface(fn=me.chat, title="AI Resume Avatar (Ritesh)", description="Ask me about my skills, career, or experience.").launch()
