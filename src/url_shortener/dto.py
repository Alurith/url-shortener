from typing import Literal

from pydantic import BaseModel, HttpUrl

# TODO: sostituire i DTO alle risposte di create_short e get_short


class AliasDTO(BaseModel):
    long_url: HttpUrl
    short_url: HttpUrl
    alias: str


class HealthDTO(BaseModel):
    status: Literal["ok", "error"]
    # TODO: completare con i campi rimasti
