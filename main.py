import uvicorn
from app import app

if __name__ == "__main__":
    # 启动FastAPI应用
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)