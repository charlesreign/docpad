from fastapi import APIRouter, Depends
from lib.docpad.utils.database import get_db
from sqlalchemy.orm import Session
from lib.docpad.models import UsersModel
from lib.docpad.schema.ResponseModel import ResponseModel
from lib.docpad.utils import oauth2

router = APIRouter()


@router.get('/me', response_model=ResponseModel.UserResponse)
def get_me(db: Session = Depends(get_db), user_id: str = Depends(oauth2.require_user)):
    user = db.query(UsersModel.User).filter(UsersModel.User.id == user_id).first()
    return user