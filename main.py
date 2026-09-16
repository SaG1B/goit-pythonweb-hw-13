from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import contacts, auth, users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router, prefix='/api/auth', tags=['auth'])
app.include_router(users.router, prefix='/api/users', tags=['users'])
app.include_router(contacts.router, prefix='/api/contacts', tags=['contacts'])

@app.get('/')
def read_root():
    return {'message': 'Welcome to FastAPI Contacts API'}
