from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_finder import UserFinder
from src.presentation.controllers.user_finder_controller import UserFinderController

def user_finder_composer():
    respository = UsersRepository()
    use_case = UserFinder(respository)
    controller = UserFinderController(use_case)

    return controller.handle
