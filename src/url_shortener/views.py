from typing import Union

from fastapi import FastAPI

app = FastAPI()

urls_mapping = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "ok", "database": "ok", "cache": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/short-urls")
def create_short(long_url: str, alias: str):
    urls_mapping["alias"] = long_url

    return {
        "long_url": f"{long_url}",
        "short_url": f"localhost:8000/{alias}",
        "alias": alias,
    }


@app.get("/short-urls/{alias}")
def get_short(alias: str):
    long_url = urls_mapping.get("alias", None)

    return {
        "long_url": f"{long_url}",
        "short_url": f"localhost:8000/{alias}",
        "alias": alias,
    }
