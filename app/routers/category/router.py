import aiofiles as aiofiles
from fastapi import APIRouter, Depends, Request, Response, UploadFile, File, Form, HTTPException
from .models import Category, NewCategory, UpdateCategory
from .queries import create_category, remove_category, edit_category, get_category_by_slug, get_tree
import time
import os


router = APIRouter(
    prefix='/category',
    tags=['Categoies']
)


@router.get('/{slug}')
async def get_category(slug: str):
    return await get_category_by_slug(slug)


@router.put('/create')
async def new_category(file: UploadFile = File(...), category: NewCategory = Form(...)):
    stamp = time.time()
    new_category: Category = await create_category(category, f"{stamp}.png")
    new_file = f'{os.getcwd()}/static/category_image/{stamp}.png'
    async with aiofiles.open(new_file, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)


@router.delete('/{slug}/delete')
async def delete_category(slug: str):
    await remove_category(slug)


@router.patch('/{slug}/update')
async def update_category(slug: str, file: UploadFile = None, category: UpdateCategory = Form(...)):
    print(category)
    print(file)
    current_category = await get_category_by_slug(slug)
    if current_category:
        if file:
            stamp = time.time()
            new_file = f'{os.getcwd()}/static/category_image/{stamp}.png'
            async with aiofiles.open(new_file, 'wb') as out_file:
                content = await file.read()
                await out_file.write(content)
            category.image = f'{stamp}.png'
        else:
            category.image = current_category.image
        await edit_category(slug, category)
    else:
        raise HTTPException(status_code=404, detail='Category not found')


@router.get('/tree/{page}')
async def get_category_tree(page: int = 0):
    return await get_tree(page)


