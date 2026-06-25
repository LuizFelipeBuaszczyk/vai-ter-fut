from fastapi.routing import APIRouter
from services.ai_service import AIService
from dto.tree_dto import RequestTree

router = APIRouter(prefix='/tree')

@router.post("/")
async def predict_game(data: RequestTree):
    return await AIService.is_possible_play_soccer(data)
