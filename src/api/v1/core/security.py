"""
    This file has the functionality to create access token and verify it
    It utilizes JWT and PyJWT
"""

from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from src.api.v1.core.project_settings import settings

project_settings = settings()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + project_settings.ACCESS_TOKEN_EXPIRE_TIME
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, project_settings.SECRET_KEY, algorithm=project_settings.ALGORITHM
    )
    return encoded_jwt


async def validate_token(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, project_settings.SECRET_KEY, algorithms=[project_settings.ALGORITHM]
        )

        if payload.get("sub") is None:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception from InvalidTokenError

    return payload


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
