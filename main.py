

import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import HumanMessage

# from workflow.agentic_workflow_with_mcp_webreseaerch import AgenticRAG # MCP websearch variant

def main():
    """Simple CLI entry point for the project (prints a greeting)"""
    print ("Welcome to the Product Assistant!")

if __name__ == "__main__":
    main()

#Initialize the FastAPI app and templates

app = FastAPI()

#Setup Jinja2 templates and static files rendering from the templates and static directories
templates = Jinja2Templates(directory="templates")

#Mounting the /static directory to serve CSS, JS, and other static assets for the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Allow all origins for CORS (Cross-Origin Resource Sharing) to enable frontend-backend communication during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# ---------- FastAPI Endpoints ---------- #

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serves the chat UI HTML Page at the root URL."""
    return templates.TemplateResponse("chat.html", {"request": request})