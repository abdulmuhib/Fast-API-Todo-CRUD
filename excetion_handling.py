from fastapi import HTTPException


class ApiException(HTTPException):
    @staticmethod
    def bad_request(message: str):
        return ApiException(status_code=400, detail=message)

    @staticmethod
    def not_found(message: str):
        return ApiException(status_code=404, detail=message)

    @staticmethod
    def server_error(message: str):
        return ApiException(status_code=500, detail=message)

    @staticmethod
    def value_error(message: str):
        return ApiException(status_code=422, detail=message)
