from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from utils.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String(50), unique=True, index=True, comment="商品编码")
    barcode = Column(String(100), unique=True, index=True, comment="条形码")
    name = Column(String(200), index=True, comment="商品名称")
    specification = Column(String(200), comment="规格型号")
    unit = Column(String(20), comment="单位")
    category = Column(String(50), index=True, comment="分类")
    supplier = Column(String(100), comment="供应商")
    purchase_price = Column(Float, comment="采购价")
    selling_price = Column(Float, comment="销售价")
    stock = Column(Integer, default=0, comment="库存数量")
    min_stock = Column(Integer, default=0, comment="最低库存")
    max_stock = Column(Integer, default=0, comment="最高库存")
    location = Column(String(100), comment="仓库位置")
    remark = Column(String(500), comment="备注")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), comment="更新时间")