from src.views.http_types.http_response import HttpResponse
from src.views.http_types.http_request import HttpRequest

class TagCreatorView:
    '''
        responsibility for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # body = http_request.body
        # product_code = body["product_code"]

        print(http_request.body)

        return HttpResponse(200, {"hello": "world"})
