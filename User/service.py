from fastapi import APIRouter, Path, Query
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError
from User.api_models import User as SchemaUser
from User.api_models import UserResponse as SchemaUserResponse
from User.api_models import UserOptional as SchemaUserPatch
from User.db_models import User as ModelUser
from dotenv import load_dotenv
from general_response import wrap_response

load_dotenv('../.env')


def user_add(user: SchemaUser):
    try:
        user_obj = ModelUser(**user.dict())
        db.session.add(user_obj)
        db.session.commit()
        user = db.session.get(ModelUser, user_obj.id)
    except IntegrityError as e:
        return wrap_response({"error": "Email or Phone Number already exists"}, status_code=400)
    except Exception as e:
        return wrap_response({"error": str(e)}, status_code=400)

    return wrap_response({"user": SchemaUserResponse(**user.__dict__).dict()})


def users_retrieve(
        sort: str = Query(None, alias="sort"),
        search: str = Query(None, alias="search"),
        search_fname: str = Query(None, alias="search-fname"),
        page: int = Query(1, ge=1),
        page_size: int = Query(10, ge=1, le=100)
):
    query = db.session.query(ModelUser)
    if sort and hasattr(ModelUser, sort):
        query = query.order_by(sort)
    if search_fname:
        query = query.filter(ModelUser.first_name.contains(search_fname))
    if search:
        query = query.filter(
            *[
                getattr(ModelUser, field).contains(search)
                for field in [field.key for field in ModelUser.table.columns]
            ]
        )
    users = query.offset((page - 1) * page_size).limit(page_size).all()
    if not users:
        return wrap_response({"error": "User not found"}, status_code=404)

    return wrap_response({"users": [SchemaUserResponse(**user.__dict__).dict() for user in users]})


def single_user(user_id: int = Path(..., title="The ID of the user to retrieve. ")):
    user = db.session.get(ModelUser, user_id)
    if not user:
        return wrap_response({"error": "User with supplied id not found"}, status_code=404)
    return wrap_response({"users": SchemaUserResponse(**user.__dict__).dict()})


def user_update_patch(id: int, user: SchemaUserPatch):
    try:
        user_obj = db.session.query(ModelUser).get(id)
        if not user_obj:
            return wrap_response({"error": "User not found"}, status_code=404)

        for key, value in user.dict().items():
            if value is not None:
                setattr(user_obj, key, value)

        db.session.commit()
        user = db.session.get(ModelUser, id)
    except IntegrityError as e:
        return wrap_response({"error": "Email or Phone Number already exists"}, status_code=400)
    except Exception as e:
        return wrap_response({"error": str(e)}, status_code=400)

    return wrap_response({"user": SchemaUserResponse(**user.__dict__).dict()})


def single_user_delete(user_id: int):
    user = db.session.get(ModelUser, user_id)
    if not user:
        return wrap_response({"error": "User with supplied id not found"}, status_code=404)
    db.session.delete(user)
    db.session.commit()
    return wrap_response({"message": "User deleted Successfully."})


def all_users_delete():
    db.session.query(ModelUser).delete()
    db.session.commit()
    return wrap_response({"message": "Users deleted successfully."})
