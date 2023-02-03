import datetime as _dt 
import pydantic as _pydantic

class _BaseContact(_pydantic.BaseModel):
    name = str
    lastname = str
    email = str
    email: str
    phone_number: str

class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime
    class Config:
        _orm_mode = True
class CreateContact(_BaseContact):
    pass        