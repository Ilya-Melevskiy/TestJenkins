from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic.alias_generators import to_camel


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    model_config = ConfigDict(
        extra="forbid", alias_generator=to_camel, populate_by_name=True
    )
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo | None = None


class Company(BaseModel):
    model_config = ConfigDict(
        extra="forbid", alias_generator=to_camel, populate_by_name=True
    )
    model_config = ConfigDict(extra="forbid")
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    model_config = ConfigDict(
        extra="forbid", alias_generator=to_camel, populate_by_name=True
    )
    model_config = ConfigDict(extra="forbid")
    id: int
    name: str
    username: str
    email: EmailStr
    phone: str
    website: str
    address: Address
    company: Company


class UserCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid", alias_generator=to_camel, populate_by_name=True
    )
    model_config = ConfigDict(extra="forbid")
    name: str
    username: str
    email: EmailStr
