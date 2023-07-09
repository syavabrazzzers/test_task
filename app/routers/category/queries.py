from src.state import state
from src.models import rec_to_model
from .models import Category, NewCategory, UpdateCategory
from slugify import slugify


async def get_category_by_slug(slug: str):
    category = await state.pgdb.select('categories', where=f"slug='{slug}'")
    print(category)
    return rec_to_model(Category, category[0])


async def get_category_tree(page: int):
    pass


async def create_category(category: NewCategory, image: str):
    if category.parent or category.parent != 0:
        fields = ('name', 'slug', 'image', 'parent')
        values = (category.name, slugify(category.name), image, category.parent)
    else:
        fields = ('name', 'slug', 'image')
        values = (category.name, slugify(category.name), image)
    new_category = await state.pgdb.insert(
                       table='categories',
                       fields=fields,
                       values=values
                   )
    return rec_to_model(Category, new_category[0])


async def remove_category(slug: str):
    await state.pgdb.delete(table='categories', where=f"slug='{slug}'")


async def edit_category(slug: str, category: UpdateCategory):
    if category.parent == 0:
        category.parent = None
    await state.pgdb.update(table='categories',
                            fields=[k for k, v in category if v],
                            values=[v for k, v in category if v],
                            where=f"slug='{slug}'")


async def get_tree(page: int):
    print(page)
    query = f"""select c.*, c2."name" "parent_category"  from categories c 
left join categories c2 on c.parent = c2.id
limit 2 offset ({page}*2*1);"""
    return await state.pgdb.execute(query)
