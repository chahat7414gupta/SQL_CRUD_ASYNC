from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, crud, database

router = APIRouter()

async def get_db():
    async with database.async_session() as session:
        yield session

@router.post("/users/", response_model=schemas.UserRead)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_user(db, user)

@router.get("/users/", response_model=list[schemas.UserRead])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db)

@router.get("/users/{user_id}", response_model=schemas.UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=schemas.UserRead)
async def update_user(user_id: int, user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud.update_user(db, user_id, user)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_user(db, user_id)

@router.post("/messages/", response_model=schemas.MessageRead)
async def create_message(msg: schemas.MessageCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_message(db, msg)

@router.get("/messages/", response_model=list[schemas.MessageRead])
async def list_messages(db: AsyncSession = Depends(get_db)):
    return await crud.get_messages(db)

@router.get("/messages/{msg_id}", response_model=schemas.MessageRead)
async def get_message(msg_id: int, db: AsyncSession = Depends(get_db)):
    msg = await crud.get_message(db, msg_id)
    if not msg:
        raise HTTPException(status_code=404, detail="Message not found")
    return msg

@router.put("/messages/{msg_id}", response_model=schemas.MessageRead)
async def update_message(msg_id: int, data: schemas.MessageCreate, db: AsyncSession = Depends(get_db)):
    return await crud.update_message(db, msg_id, data)

@router.delete("/messages/{msg_id}")
async def delete_message(msg_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_message(db, msg_id)
