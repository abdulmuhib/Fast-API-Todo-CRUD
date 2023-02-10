from typing import Dict, Any


def wrap_response(data: Dict[str, Any], status_code: int = 200) -> Dict[str, Any]:
    response = {"success": True, "data": data}
    if "error" in data:
        response["success"] = False
    return response, status_code