from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    is_unprocessable_entity_error = isinstance(error, HttpUnprocessableEntityError)

    status_code = error.status_code if is_unprocessable_entity_error else 500
    title = error.name if is_unprocessable_entity_error else "Internal Server Error"
    detail = error.message if is_unprocessable_entity_error else str(error)

    body = {
        "errors": [{
            "title": title,
            "detail": detail
        }]
    }

    return HttpResponse(status_code, body)
