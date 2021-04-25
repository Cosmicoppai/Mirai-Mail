"""
未来Mail
"""

# いつかヒロになりたい
# ドライフラワー
from fastapi import Request, Form
from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import starlette.status as status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
from collections import OrderedDict
from functools import lru_cache
from dotenv import load_dotenv
from support import send_mail
from airtable import AirTable
import os

app = FastAPI()  # declared the name of the app

app.mount("/static", StaticFiles(directory='static'), name='static')  # staticfiles location
templates = Jinja2Templates(directory='templates')  # name of the 3rd party template


class Mirai(BaseModel):
    Email: EmailStr
    date: Optional[str] = str(datetime.today()).split(" ")[0]
    subject: Optional[str] = f"From {str(date)} -_- "
    Msg: str
    Scheduled_date: str

    def __init__(self, **data):

        super().__init__(**data)

        # if Email already exist don't increase the id

        """if database.get(self.Email, False):
            return
        else:
            # get the latest id from the database...
            self.id = database[list(database)[-1]][0]['id'] + 1"""

    """@validator('Email')
    def email_checker(cls, v):
        if not v:
            raise ValueError("Umhmm Please Enter the Email")
        return v

    @validator('Msg')
    def msg_checker(cls, v):
        if not v:
            raise ValueError('Ahhh Common type some message')"""


@lru_cache()  # To cache the data
def cached_keys():
    load_dotenv()


cached_keys()

_base_id = os.environ.get('AIRTABLE_BASE_ID')
_api_key = os.environ.get('AIRTABLE_API_KEY')
_table_name = os.environ.get('AIRTABLE_TABLE_NAME')


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("base.html", {'request':request})  # Just rendering the basic html Page


@app.post('/')
async def get_mail(request: Request, Email: str = Form(...), Msg: str = Form(...), Scheduled_date: str = Form(...)):

    airtable_client = AirTable(base_id=_base_id,
                               api_key=_api_key,
                               table_name=_table_name)

    if Scheduled_date == str(datetime.today()).split(" ")[0]:
        mirai = Mirai(Email=Email, Msg=Msg, Scheduled_date=Scheduled_date)
        mirai = mirai.dict()

        # database[mirai['Email']] = [mirai, ]  # else save the whole data in OrderedDict in list format
        send_mail(mirai['Email'], mirai['Msg'], mirai['subject'])  # Trigger the mail function
        return templates.TemplateResponse("base.html", {'request': request, "status_code": status.HTTP_200_OK})

    # print(Email, Msg, Scheduled_date)
    airtable_client.create_records({'Email':Email, 'Msg':Msg, 'Scheduled_on':Scheduled_date})
    return templates.TemplateResponse("base.html", {'request': request, "status_code": status.HTTP_200_OK})