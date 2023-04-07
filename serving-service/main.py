import uvicorn

from src.server import server

if __name__ == "__main__":
    serving_app = server()
    uvicorn.run(
        serving_app,
        host="0.0.0.0",
        port=8008,
        log_level="info",
    )
