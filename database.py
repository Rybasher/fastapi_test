from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Enum
from datetime import date
import enum


meta = MetaData()


class EnumChoice(enum.Enum):
    active = "active"
    inactive = "inactive"
    deleted = "deleted"


# СОздание таблицы Users
users = Table(
    "Users", meta,
    Column("id", Integer, primary_key=True),
    Column("user_name", String),
    Column("email", String),
    Column("password", String),
    Column("status", Enum(EnumChoice, name="status"), default="active"),
    Column("created_at", Date, default=date.today),
    Column("updated_at", Date, default=None)
)

# Подлючаемся к БД
engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/test_task")
meta.create_all(engine)
conn = engine.connect()
