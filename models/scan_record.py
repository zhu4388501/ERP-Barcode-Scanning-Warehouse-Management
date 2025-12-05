from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from utils.database import Base

class OperationType(str, enum.Enum):
    IN = "in"  # 入库
    OUT = "out"  # 出库

class ScanRecord(Base):
    __tablename__ = "scan_records"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True, comment="商品ID")
    barcode = Column(String(100), index=True, comment="条形码")
    product_name = Column(String(200), comment="商品名称")
    quantity = Column(Integer, comment="数量")
    operation_type = Column(Enum(OperationType), comment="操作类型：in-入库，out-出库")
    operator = Column(String(50), comment="操作人")
    remark = Column(String(500), comment="备注")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")

    # 关联商品
    product = relationship("Product")