from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import bcrypt
from jose import jwt

from database import get_db
from schemas import UserCreate


SECRET_KEY = "my-super-secret-key-123"
ALGORITHM = "HS256"

router = APIRouter(prefix="/users", tags=["Users"])

security = HTTPBearer()


@router.post("/register")
def register_user(user: UserCreate):

    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    )

    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users(username, password)
        VALUES (?, ?)
        """,
        (
            user.username,
            hashed_password.decode("utf-8")
        )
    )

    connection.commit()
    connection.close()

    return {
        "message": "User registered successfully",
        "username": user.username
    }


@router.post("/login")
def login_user(user: UserCreate):

    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (user.username,)
    )

    db_user = cursor.fetchone()
    connection.close()

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    password_correct = bcrypt.checkpw(
        user.password.encode("utf-8"),
        db_user["password"].encode("utf-8")
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token_data = {
        "user_id": db_user["id"],
        "username": db_user["username"]
    }

    token = jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "message": "Login successful",
        "access_token": token
    }


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


@router.get("/protected")
def protected_route(
    user=Depends(verify_token)
):

    return {
        "message": "You have access!",
        "user": user
    }