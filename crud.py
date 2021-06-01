from fastapi import APIRouter
from database import conn, users
from schemas import User
from datetime import date
from database import EnumChoice

user = APIRouter()


# Получить всех пользователей из таблицы юзерс
@user.get('/show_users/')
async def show_users():
    return conn.execute(users.select()).fetchall()


# Получить информацию о пользователе по id
@user.get('/{user_id}')
async def show_user_bu_id(user_id: int):
    return conn.execute(users.select().where(users.c.id == user_id)).fetchall()


# Создание пользователя
@user.post('/create_user/')
async def create_user(u: User):
    try:
        conn.execute(users.insert().values(
            user_name=u.user_name,
            email=u.email,
            password=u.password,
            status=u.status,
            created_at=u.created_at,
            updated_at=None
        ))
    except:
        return {"success": False}
    return conn.execute(users.select()).fetchall()


# Редактирование существующего пользователя
@user.put('/update_user/{user_id}/')
async def update_user(user_id: int, u: User):
    conn.execute(users.update().values(
        user_name=u.user_name,
        email=u.email,
        password=u.password,
        status=u.status,
        updated_at=date.today()
    ).where(users.c.id == user_id))
    return conn.execute(users.select()).fetchall()


# Удаление конкретного пользователя по id
@user.delete('/delete_user/{user_id}')
async def delete_user(user_id: int):
    conn.execute(users.delete().where(users.c.id == user_id))
    return conn.execute(users.select()).fetchall()
