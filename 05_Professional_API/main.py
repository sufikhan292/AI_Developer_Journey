from fastapi import FastAPI
from routes.students import router
from routes.users import router as users_router

app = FastAPI()

app.include_router(router)
app.include_router(users_router)