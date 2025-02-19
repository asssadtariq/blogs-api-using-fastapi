from fastapi import HTTPException, status


def get_http_404(err_msg: str = "Data not found"):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail={"message": err_msg}
    )
