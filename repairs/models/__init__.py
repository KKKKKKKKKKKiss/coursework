from repairs.models.repairs import Repair, Status
from repairs.models.places import PlacesToWork
from repairs.models.type_repair import TypeRepair
from repairs.models.parts import Parts
from repairs.models.works import Works
from repairs.models.IDobjects import Comp

__all__ = (
    'Status',
    'Works',
    'Parts',
    'TypeRepair',
    'PlacesToWork',
    'Repair',
    'Comp'
)
