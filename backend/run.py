"""
Development server runner.

This is a convenience script to run the FastAPI application.

Usage:
    python run.py

The server will start on http://0.0.0.0:8000 with auto-reload enabled.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload for development
        log_level="info"
    )