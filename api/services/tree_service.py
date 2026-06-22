from dto.tree_dto import RequestTree, ResponseTree
from services import clf

class TreeService:
    
    @staticmethod
    async def is_possible_play_soccer(data: RequestTree):
        result = clf.predict([[data.temperature, data.is_raining, data.humidity]])[0]
        return ResponseTree(
                    can_play=result
                )
