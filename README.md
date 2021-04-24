# Fastapi
Things I learned in FastApi

# Template Rendering
* pipenv install jinja2 & aiofiles

* from fastapi import Request

* from fastapi.response import HtmlResponse

* from fastapi.staticfiles import StaticFiles

* from fastapi.templating import Jinja2Templates

* app = fastapi()   # create an instance of the api

* app.mount("/static", StaticFiles(directory='static'), name='static')   # specify the staticfiles path and url routing


* templates = Jinja2Templates(directory = "templates")  # ASpecify the templates path

```python
@app.get("/")
async def home(request: Request, response_class=HtmlResponse):    # By declaring response class the doc UI will know that the response will be HTML
  return templates.TemplateResponse("base.html", {'request': request})
  ```
  
  
  # To specify link in href for staticfiles
  
  * href="{{  url_for(static path='/styles.css')  }}"
