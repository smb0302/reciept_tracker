import os
import pathlib
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from pick import pick

class Item(BaseModel):
    item_name: str = Field(description="The name of the item.")
    unit_price: int = Field(description="price of the item per unit in cents")
    unit: str = Field(description="unit of the item")

class Reciept(BaseModel):
    items: list[Item]

load_dotenv()
API_KEY = os.getenv('KEY')
path = os.getenv('FILE_PATH')
dir_list = os.listdir(path)

title = 'Pick a receipt:  '
file, index = pick(dir_list, title)

client = genai.Client(
    api_key=API_KEY)

filepath = pathlib.Path(f'reciepts/{file}')

prompt = "please extract all items and prices from this receipt"
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='image/jpg',
      ),
    prompt
  ],
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Reciept.model_json_schema(),
    }
)

receipt = Reciept.model_validate_json(response.text)

