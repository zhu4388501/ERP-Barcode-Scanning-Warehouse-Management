from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from sqlalchemy.sql import func
import enum
from utils.database import Base

class OfflineOperationType(str, enum.Enum):
    SCAN = "scan"  # 扫描操作
    CREATE_PRODUCT = "create_product"  # 创建商品
    UPDATE_PRODUCT = "update_product"  # 更新商品

class OfflineOperation(Base):
    __tablename__ = "offline_operations"

    id = Column(Integer, primary_key=True, index=True)
    operation_type = Column(Enum(OfflineOperationType), comment="操作类型")
    data = Column(String(2000), comment="操作数据，JSON格式")
    is_synced = Column(Boolean, default=False, comment="是否已同步到服务器")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")
    synced_at = Column(DateTime(timezone=True), nullable=True, comment="同步时间")