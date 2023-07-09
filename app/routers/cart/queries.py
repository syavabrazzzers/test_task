from src.state import state


async def get_user_cart_by_id(id: int):
    query = f"""select p.*, c.count , (c.count * p.price) "full_price" from cart c
left join products p on p.id = c.product_id
where c.user_id = {id};"""
    cart = await state.pgdb.execute(query)
    return cart


async def clear_user_cart(id: int):
    await state.pgdb.delete('cart', where=f'user_id={id}')


async def add_product_to_cart(product_id: int, count: int, user_id: int):
    await state.pgdb.insert('cart',
                            fields=('user_id', 'product_id', 'count'),
                            values=(user_id, product_id, count),
                            on_conflict=('user_id, product_id', f'do update set count = (cart.count + {count})'))


async def remove_product_from_cart(product_id: int, user_id: int, count: int = None):
    current_count = await state.pgdb.select('cart', columns='count', where=f'product_id={product_id} and user_id={user_id}')
    if not count or count >= current_count[0]['count']:
        await state.pgdb.delete('cart', where=f'product_id={product_id} and user_id={user_id}')
    else:
        await state.pgdb.update('cart', fields=('count', ), values=(current_count[0]['count']-count, ), where=f'product_id={product_id} and user_id={user_id}')