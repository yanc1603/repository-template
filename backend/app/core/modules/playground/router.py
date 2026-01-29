from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from pydantic import BaseModel
from .models import Task


router = APIRouter(prefix="/playground", tags=["Playground"])

# Pydantic Schemas (Data validation)
class TaskCreate(BaseModel):
    title: str

class TaskResponse(BaseModel):
    id: int
    is_completed: bool

# Send Data (CREATE)
@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    new_task = Task(title=task.title)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

# Read Data (LIST)
@router.get("/", response_model=list)
async def read_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    return result.scalars().all()

# Change State (UPDATE)
@router.patch("/", response_model=TaskResponse)
async def toggle_state(task_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if not task: raise HTTPException(404)

    task.is_completed = not task.is_completed # Toggle True/False
    await db.commit()
    await db.refresh(task)
    return task