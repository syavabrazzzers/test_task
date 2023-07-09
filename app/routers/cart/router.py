from fastapi import APIRouter, Depends, Request, Response
from .queries import get_user_cart_by_id, clear_user_cart, add_product_to_cart, remove_product_from_cart
from ..auth.service import get_current_user


router = APIRouter(
    prefix='/cart',
    tags=['Cart']
)


@router.get('')
async def get_user_cart(session=Depends(get_current_user)):
    return await get_user_cart_by_id(int(session[0]['id']))


@router.get('/clear')
async def clear_cart(session=Depends(get_current_user)):
    await clear_user_cart(int(session[0]['id']))


@router.put('/add/{product_id}')
async def add_product(product_id: int, count: int, session=Depends(get_current_user)):
    await add_product_to_cart(product_id, count, int(session[0]['id']))


@router.delete('/remove/{product_id}')
async def delete_product_from_cart(product_id: int, count: int = None, session=Depends(get_current_user)):
    await remove_product_from_cart(product_id, int(session[0]['id']), count)




