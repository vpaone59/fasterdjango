To start,

clone this repository

pip install -r requirements.txt

uvicorn myproject.asgi:app --reload

Go to 127.0.0.1:8000/docs to see the API in action.

Here you can see how values will be inserted and read from the database.

Requires: uvicorn, FastAPI, Django