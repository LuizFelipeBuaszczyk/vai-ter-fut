from fastapi.routing import APIRouter
from routes.tree_router import router as tree_router

router = APIRouter()
router.include_router(tree_router)
