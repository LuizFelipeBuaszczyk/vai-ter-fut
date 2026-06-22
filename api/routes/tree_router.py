from fastapi.routing import APIRouter
from services.tree_service import TreeService
from dto.tree_dto import RequestTree

router = APIRouter(prefix='/tree')

@router.post("/")
async def predict_game(data: RequestTree):
    return await TreeService.is_possible_play_soccer(data)
