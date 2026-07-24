from fastapi.responses import JSONResponse


def success(data):
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "data": data
        }
    )


def failure(message, status_code=400):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": message
        }
    )