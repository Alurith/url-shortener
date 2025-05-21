from typing import Annotated, Union

from fastapi import Depends, FastAPI

from url_shortener.repository.base import AliasRepository
from url_shortener.repository.memory import InMemory

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "ok", "database": "ok", "cache": "ok"}


@app.post("/short-urls")
def create_short(
    repo: Annotated[AliasRepository, Depends(InMemory)],
    long_url: str,
    alias: Union[str, None] = None,
):
    # TODO: alias adesso è opzionale, se non c'è dovete creare una stringa random di almeno 5 caratteri ed usarla come alias.
    # alias = ??
    repo.add(alias=alias, long_url=long_url)

    return {
        "long_url": f"{long_url}",
        "short_url": f"localhost:8000/{alias}",
        "alias": alias,
    }


@app.get("/short-urls/{alias}")
def get_short(
    repo: Annotated[AliasRepository, Depends(InMemory)],
    alias: str,
):
    long_url = repo.get_by_alias(alias=alias)

    return {
        "long_url": f"{long_url}",
        "short_url": f"localhost:8000/{alias}",
        "alias": alias,
    }
