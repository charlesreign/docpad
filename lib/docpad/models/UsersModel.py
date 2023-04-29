import uuid
from sqlalchemy import TIMESTAMP, Column, String, text
from sqlalchemy.dialects.postgresql import UUID
from lib.docpad.utils.database import Base


class User(Base):
    __tablename__ = "docpad_users"
    id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4
    )
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    password = Column(String)
    time_created = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    time_updated = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
