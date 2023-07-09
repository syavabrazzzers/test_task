import os
import time

from src.state import state
from src.models import rec_to_model
from .models import Product, NewProduct, Images, UpdateProduct, FullProduct
from slugify import slugify
from PIL import Image

async def get_product_by_slug(slug: str):
    product = await state.pgdb.select(table='products', where=f"slug='{slug}'")
    return rec_to_model(Product, product[0])


async def create_new_product(product: NewProduct):
    new_product = await state.pgdb.insert('products',
                                          fields=('name', 'slug', 'category_id', 'price'),
                                          values=(product.name, slugify(product.name), product.category_id, product.price)
                                          )
    return rec_to_model(Product, new_product[0])


async def add_images(image: Image, product_id: int):
    stamp = time.time()
    high_image = image.resize((500, 500))
    medium_image = image.resize((250, 250))
    low_image = image.resize((100, 100))
    new_images = await state.pgdb.insert(
        'product_images',
        fields=('product_id', 'high_quality', 'medium_quality', 'low_quality'),
        values=(product_id,
                f'high_{stamp}.png',
                f'medium_{stamp}.png',
                f'low_{stamp}.png')
    )
    if new_images:
        high_image.save(f'{os.getcwd()}/static/product_images/high_{stamp}.png')
        medium_image.save(f'{os.getcwd()}/static/product_images/medium_{stamp}.png')
        low_image.save(f'{os.getcwd()}/static/product_images/low_{stamp}.png')
    return rec_to_model(Images, new_images[0])


async def edit_product(slug: str, product: UpdateProduct):
    updated = await state.pgdb.update(table='categories',
                                      fields=[k for k, v in product if v is not None],
                                      values=[v for k, v in product if v is not None],
                                      where=f"slug='{slug}'")
    return rec_to_model(Product, updated[0])


async def remove_product(id: int):
    await state.pgdb.delete('products', where=f'id={id}')


async def get_products_per_page(page: int):
    query = f"""select p.id
    , p."name" 
    , p.slug 
    , p.price
    , c2."name" "parent_category"
    , c."name" "category"
    , pi2.high_quality "hq_image"
    , pi2.medium_quality "mq_image"
    , pi2.low_quality "lq_image" 
    from products p 
left join categories c on p.category_id = c.id
left join categories c2 on c.parent = c2.id 
left join product_images pi2 on pi2.product_id = p.id
limit 10 offset {page * 10 * 1};"""
    products = await state.pgdb.execute(query)
    print(products)
    return [rec_to_model(FullProduct, product) for product in products]
