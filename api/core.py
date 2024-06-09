from fastapi import FastAPI
from api.schames import Settings
from fastapi_jwt_auth import AuthJWT
from api.product_router import product_router
from api.auth import model_auth
from api.order_router import order_router


@AuthJWT.load_config
def get_cofig():
    return Settings()


app = FastAPI()
app.include_router(product_router)
app.include_router(model_auth)
app.include_router(order_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
