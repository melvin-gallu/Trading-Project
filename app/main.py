from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from .gemini import gemini_ws

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://localhost:8000",
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(gemini_ws.router)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>External WebSocket Data</title>
</head>
<body>
    <h1>Hello</h1>
    <div id="messages"></div>

    <script>
        const ws = new WebSocket("ws://localhost:8000/gemini/market-data");

        ws.onopen = () => {
            console.log("WebSocket connection established.");
        };

        ws.onmessage = (event) => {
            const messagesDiv = document.getElementById("messages");
            messagesDiv.innerHTML += `<p>${event.data}</p>`;
        };

        ws.onerror = (error) => {
            console.error(`WebSocket error: ${error}`);
        };

        ws.onclose = () => {
            console.log("WebSocket connection closed.");
        };
    </script>
</body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html_content)