from fastapi import APIRouter, status, Depends
from celery.result import AsyncResult
from ..celeryTasks.tasks import background_task

from .. import oauth2
from .. import schema
router = APIRouter(
    prefix="/task",
    tags=['Tasks']
)


@router.post('/new', response_model=schema.TaskResult)
async def run_task(current_user: str = Depends(oauth2.get_current_user)):
    task_id = background_task.delay(1, 2)
    return {'task_id': str(task_id), 'status': 'Processing', 'result': None}


@router.get('/result/{task_id}', response_model=schema.TaskResult)
async def fetch_result(task_id: str, current_user: str = Depends(oauth2.get_current_user)):
    task = AsyncResult(task_id)
    if not task.ready():
        return {'task_id': task_id, 'status': 'Processing', 'result': None}
    result = task.get()
    return {'task_id': task_id, 'status': 'Completed', 'result': str(result)}
