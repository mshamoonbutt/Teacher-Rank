from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, auth
from ..database import get_db

router = APIRouter()

@router.get("/reviews/", response_model=list[schemas.Review])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reviews = crud.get_reviews(db, skip=skip, limit=limit)
    return reviews

@router.get("/reviews/{review_id}", response_model=schemas.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    db_review = crud.get_review(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@router.post("/reviews/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    # Optionally, ensure the review.user_id matches the authenticated user
    if review.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Cannot create review for another user.")
    return crud.create_review(db=db, review=review) 