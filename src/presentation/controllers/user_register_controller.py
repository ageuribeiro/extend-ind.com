from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class UserRegisterController(ControllerInterface):
    def __init__(self, use_case: UserRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.body["name"]
        username = http_request.body["username"]
       
      
        response = self.__use_case.register(name, username)

        return HttpResponse(
            status_code = 200,
            body={"data": response}
        )
    
