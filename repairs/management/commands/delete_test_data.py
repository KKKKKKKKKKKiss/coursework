from repairs.models import Locomotive, PlacesToWork, TypeRepair
from users.models import User

# Удаление всех моделей Locomotive, PlacesToWork, TypeRepair и Work
Locomotive.objects.all().delete()
PlacesToWork.objects.all().delete()
TypeRepair.objects.all().delete()

# Удаление всех пользователей
User.objects.all().delete()