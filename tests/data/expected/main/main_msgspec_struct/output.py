# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from msgspec import Meta, Struct, field
from typing_extensions import Annotated


class Pet(Struct):
    id: int
    name: str
    tag: Optional[str] = None


Pets = List[Pet]


class User(Struct):
    id: int
    name: str
    tag: Optional[str] = None


Users = List[User]


Id = str


Rules = List[str]


class Error(Struct):
    code: int
    message: str


class Api(Struct):
    apiKey: Optional[
        Annotated[str, Meta(description='To be used as a dataset parameter value')]
    ] = None
    apiVersionNumber: Optional[
        Annotated[str, Meta(description='To be used as a version parameter value')]
    ] = None
    apiUrl: Optional[
        Annotated[str, Meta(description="The URL describing the dataset's fields")]
    ] = None
    apiDocumentationUrl: Optional[
        Annotated[str, Meta(description='A URL to the API console for each API')]
    ] = None


Apis = List[Api]


class Event(Struct):
    name: Optional[str] = None


class Result(Struct):
    event: Optional[Event] = None
