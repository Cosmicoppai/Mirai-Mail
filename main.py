"""
未来Mail
"""

# いつかヒロになりたい
# ドライフラワー
from fastapi import Request, Form
from pydantic import EmailStr
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import starlette.status as status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
from functools import lru_cache
from dotenv import load_dotenv  # to load the environment variables
from support import send_mail
from airtable import AirTable
import os

app = FastAPI()  # declared the name of the app

app.mount("/static", StaticFiles(directory='static'), name='static')  # staticfiles location
templates = Jinja2Templates(directory='templates')  # name of the 3rd party template


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


@app.post('/', status_code=200)
async def get_mail(request: Request, Email: EmailStr = Form(...), Msg: str = Form(...), Scheduled_date: str = Form(...)):

    airtable_client = AirTable(base_id=_base_id,
                               api_key=_api_key,
                               table_name=_table_name)

    today_date = str(datetime.today()).split(" ")[0]
    if Scheduled_date == today_date:
        subject = f"From {today_date} -_- "

        send_mail(Email, Msg, subject)  # Trigger the mail function
        return templates.TemplateResponse("base.html", {'request': request, "status_code": status.HTTP_200_OK})

    airtable_client.create_records({'Email':Email, 'Msg':Msg, 'Scheduled_on':Scheduled_date})
    return templates.TemplateResponse("base.html", {'request': request, "status_code": status.HTTP_200_OK})