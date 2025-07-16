from sqlalchemy.future import select
from sqlalchemy.orm import selectinload  # <-- ADD THIS
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    new_user = models.User(**user.dict())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    # Re-fetch using selectinload to avoid Lazy Load errors
    result = await db.execute(
        select(models.User).options(selectinload(models.User.messages)).where(models.User.id == new_user.id)
    )
    return result.scalars().first()

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(models.User).options(selectinload(models.User.messages)).where(models.User.id == user_id)
    )
    return result.scalars().first()

async def get_users(db: AsyncSession):
    result = await db.execute(
        select(models.User).options(selectinload(models.User.messages))
    )
    return result.scalars().all()


async def update_user(db: AsyncSession, user_id: int, data: schemas.UserCreate):
    user = await get_user(db, user_id)
    if user:
        for key, value in data.dict().items():
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
    return user

async def delete_user(db: AsyncSession, user_id: int):
    user = await get_user(db, user_id)
    if user:
        await db.delete(user)
        await db.commit()
    return user

async def create_message(db: AsyncSession, message: schemas.MessageCreate):
    new_msg = models.Message(**message.dict())
    db.add(new_msg)
    await db.commit()
    await db.refresh(new_msg)
    return new_msg

async def get_messages(db: AsyncSession):
    result = await db.execute(select(models.Message))
    return result.scalars().all()

async def get_message(db: AsyncSession, msg_id: int):
    result = await db.execute(select(models.Message).where(models.Message.id == msg_id))
    return result.scalars().first()

async def update_message(db: AsyncSession, msg_id: int, data: schemas.MessageCreate):
    msg = await get_message(db, msg_id)
    if msg:
        for key, value in data.dict().items():
            setattr(msg, key, value)
        await db.commit()
        await db.refresh(msg)
    return msg

async def delete_message(db: AsyncSession, msg_id: int):
    msg = await get_message(db, msg_id)
    if msg:
        await db.delete(msg)
        await db.commit()
    return msg
