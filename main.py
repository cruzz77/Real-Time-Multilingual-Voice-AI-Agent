import uvicorn
import os


app_port = int(
    os.environ.get(
        "PORT",
        8000
    )
)


if __name__ == "__main__":

    uvicorn.run(
        "api.server:app",
        host="0.0.0.0",
        port=app_port,
        reload=False
    )