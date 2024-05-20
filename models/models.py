from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

User = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("role_id", Integer, ForeignKey("role.id"), nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
)

Event = Table(
    "event",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("status", String, nullable=False),
    Column("employer_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("start_date", TIMESTAMP, default=datetime.utcnow),
    Column("end_date", TIMESTAMP, onupdate=datetime.utcnow),
)

Group = Table(
    "group",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("status", String, nullable=False),
)

EventGroup = Table(
    "event_group",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("event_id", Integer, ForeignKey("event.id"), nullable=False),
    Column("group_id", Integer, ForeignKey("group.id"), nullable=False),
)

EmployeGroup = Table(
    "employe_group",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("employer_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("group_id", Integer, ForeignKey("group.id"), nullable=False),
)

Test = Table(
    "test",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("link", String, nullable=False),
)

TestGroup = Table(
    "test_group",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("test_id", Integer, ForeignKey("test.id"), nullable=False),
    Column("group_id", Integer, ForeignKey("group.id"), nullable=False),
)

Instraction = Table(
    "instraction",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("link", String, nullable=False),
)

InstractionGroup = Table(
    "instraction_group",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("instraction_id", Integer, ForeignKey("instraction.id"), nullable=False),
    Column("group_id", Integer, ForeignKey("group.id"), nullable=False),
)