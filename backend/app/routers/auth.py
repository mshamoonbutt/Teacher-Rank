from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import crud, schemas, auth, firebase_auth
from ..database import get_db

router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/google-token")
async def google_login(token: str, db: Session = Depends(get_db)):
    try:
        decoded_token = firebase_auth.verify_firebase_token(token)
        email = decoded_token.get("email")
        if not email:
            raise HTTPException(status_code=400, detail="Email not found in token")
        user = crud.get_user_by_email(db, email=email)
        if not user:
            # Optionally create a new user if not exists
            user = crud.create_user(db, schemas.UserCreate(email=email, password=""))
        access_token = auth.create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 