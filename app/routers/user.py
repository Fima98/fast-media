from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# @router.get('/me', response_model=schemas.UserOut)
# def get_current_user(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
#     if not current_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="User does not exist")
    
#     return current_user

@router.get('/me', response_model=schemas.UserOut)
def get_current_user(db: Session = Depends(get_db), user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == user.id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {user.id} does not exist")
    
    return user

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user


