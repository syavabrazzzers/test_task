import io
from typing import List

from fastapi import APIRouter, Form, File, UploadFile, HTTPException
from .queries import get_product_by_slug, create_new_product, add_images, edit_product, remove_product, get_products_per_page
from .models import Product, NewProduct, Images, UpdateProduct, FullProduct
from PIL import Image


router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@router.get('', response_model=List[FullProduct])
async def get_products(page: int = 0):
    products = await get_products_per_page(page)
    return products


@router.get('/{slug}', response_model=Product)
async def get_product(slug: str):
    return await get_product_by_slug(slug)


@router.put('/create', response_model=Product)
async def create_product(product: NewProduct = Form(...), image: UploadFile = File(...)):
    new_product: Product = await create_new_product(product)
    new_image = Image.open(io.BytesIO(await image.read()))
    await add_images(new_image, new_product.id)
    return new_product


@router.patch('/{slug}/update')
async def update_product(slug: str, product: UpdateProduct = Form(...), image: UploadFile = File(...)):
    current_product: Product = await get_product_by_slug(slug)
    if current_product:
        await edit_product(slug, product)
        if image:
            new_image = Image.open(io.BytesIO(await image.read()))
            await add_images(new_image, current_product.id)
    else:
        raise HTTPException(status_code=404, detail='Product not found')


@router.delete('/{id}/delete')
async def delete_product(id: int):
    await remove_product(id)

