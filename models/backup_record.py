from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from utils.database import Base

class BackupRecord(Base):
    __tablename__ = "backup_records"

    id = Column(Integer, primary_key=True, index=True)
    backup_file = Column(String(200), comment="备份文件名")
    backup_path = Column(String(500), comment="备份文件路径")
    file_size = Column(Integer, comment="文件大小（字节）")
    is_manual = Column(Boolean, default=True, comment="是否手动备份")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")