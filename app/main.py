from fastapi import FastAPI


app = FastAPI(
    title="OrderFlow Analytics Platform",
    version="0.1.0",
    description=(
        "Real-time market microstructure "
        "analytics platform."
    )
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "ofap-api"
    }


@app.get("/")
async def root():
    return {
        "name": "OrderFlow Analytics Platform",
        "version": "0.1.0",
        "status": "running"
    }

