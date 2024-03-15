from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

  # Define the location of your templates directory
templates = Jinja2Templates(directory="templates")

  # A list to store the items (just for demonstration, you would use a database in a real application)
items = []


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
      # Render the template named "index.html" located in the "templates" directory
      return templates.TemplateResponse("index.html", {"request": request})


class Item(BaseModel):
      name: str
      description: str | None = None
      price: float


@app.post("/items/", response_model=Item)  
async def create_item(item: Item):
      # Add the new item to the list
      items.append(item)
      # Return the created item
      return item


@app.get("/items/", response_model=list[Item])  # Define a GET endpoint to retrieve all items
async def read_items():
      return items
