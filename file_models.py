import datetime
from uuid import uuid4

from database import Base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, DateTime, Boolean, Text
import sqlalchemy.orm as orm



class File(Base):
    _tablename_ = "files"
    id = Column(String(255), primary_key=True, index=True, default=uuid4().hex)
    filename = Column(String(255), index=True)
    description = Column(Text)
    is_deleted=Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)
