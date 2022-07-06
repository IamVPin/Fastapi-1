from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.user import router as UserRouter
from routes.student import router as StudentRouter

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
   await initiate_database()
   print("3")


@app.get("/", tags=["Root"])
async def read_root():
    print("4")
    return {"message": "Welcome to this fantastic app."}



app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(StudentRouter, tags=["Students"], prefix="/student", dependencies=[Depends(token_listener)])
