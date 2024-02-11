from typing import TypedDict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorControllerData(TypedDict):
    type: str
    count: int
    path: str
class TagCreatorControllerResponse(TypedDict):
    data: TagCreatorControllerData

class TagCreatorController:
    '''
        responsible for implementing business rules
    '''

    def create(self, product_code: str) -> TagCreatorControllerResponse:
        path_from_tag = self.__create_tag(product_code)
        return self.__format_response(path_from_tag)

    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        return barcode_handler.create_barcode(product_code)

    def __format_response(self, path_from_tag: str) -> TagCreatorControllerResponse:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
