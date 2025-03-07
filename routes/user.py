from fastapi import APIRouter

from configs.db import SessionDep
from models.model import UserCreate, UserTable

# from schemas.user import UserCreate  # Suponiendo que tienes un esquema para validar datos

router = APIRouter()

@router.post("/")
async def create_user(user_data: UserCreate, session: SessionDep) -> UserTable:
    user = UserTable(**user_data.dict())  # ⚡ Convertir UserCreate a UserTable
    session.add(user)
    session.commit()
    session.refresh(user)  # Ahora sí es una instancia válida de UserTable
    return user

# @app.get("/heroes/")
# def read_heroes(
#     session: SessionDep,
#     offset: int = 0,
#     limit: Annotated[int, Query(le=100)] = 100,
# ) -> list[Hero]:
#     heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
#     return heroes


# @app.get("/heroes/{hero_id}")
# def read_hero(hero_id: int, session: SessionDep) -> Hero:
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     return hero


# @app.delete("/heroes/{hero_id}")
# def delete_hero(hero_id: int, session: SessionDep):
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     session.delete(hero)
#     session.commit()
#     return {"ok": True}