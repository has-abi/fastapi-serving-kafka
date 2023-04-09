import uvicorn

from src.server import server

if __name__ == "__main__":
    data_app = server()
    uvicorn.run(
        data_app,
        host="0.0.0.0",
        port=8009,
        log_level="info",
    )
