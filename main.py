from fastapi import FastAPI  #導入fastapi
import uvicorn
from routers.webhooks import line_app
from enum import Enum
#uvicorn main:app --reload
#uvicorn main:app --debug 
# 添加--debug，它将在文件更新时自动重新加载，这在开发过程中非常方便。
app = FastAPI()         #創建一個fastapi應用

# app.include_router(webhooks.router) #注册 APIRouter
app.include_router(line_app) #注册 APIRouter

@app.get("/item/{item_id}")   #創建一個route路徑用get方法
async def root(item_id:int):      #function 傳入參數 :int 型態
    return {"message": "Hello World",
            "item_id": item_id}


class ModelName(str,Enum):
  alexnet = "alexnet"
  resnet  = "resnet"
  lenet   = "lenet"


@app.get("/model_name/{model_name}")   #創建一個route路徑用get方法
async def get_model(model_name:ModelName):      #function 傳入參數 :int 型態
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#路径转换器
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)