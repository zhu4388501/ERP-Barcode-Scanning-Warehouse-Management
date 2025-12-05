from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from routes import router as api_router

# 创建FastAPI应用
app = FastAPI(
    title="ERP条码扫描仓库管理系统",
    description="基于FastAPI的ERP条码扫描仓库管理系统API",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置为具体的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 包含API路由
app.include_router(api_router, prefix="/api")

# 根路径
@app.get("/")
def read_root():
    return {"message": "欢迎使用ERP条码扫描仓库管理系统API"}