from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import auth, contacts, users

app = FastAPI(title="Contacts REST API")

# Налаштування CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення роутерів з правильними префіксами
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(contacts.router, prefix="/api/contacts", tags=["contacts"])
app.include_router(users.router, prefix="/api/users", tags=["users"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Contacts API"}