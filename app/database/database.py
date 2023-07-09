from fastapi import HTTPException

import asyncpg
from asyncpg import UniqueViolationError, InternalServerError


class Connection:
    def __init__(self):
        self.pool = None
        self.connection = None

    async def connect(self, **kwargs):
        self.connection = await asyncpg.connect(host=kwargs['host'],
                                                port=kwargs['port'],
                                                user=kwargs['user'],
                                                password=kwargs['password'],
                                                database=kwargs['database'])

    async def create_pool(self, dsn):
        self.pool = await asyncpg.create_pool(dsn)

    async def close_pool(self):
        await self.pool.close()

    async def select(self, table: str, columns: str = '*', where: str = None, order_by_column: str = None,
                     limit: int = None, distinct: bool = False):
        query = f'select {"distinct" if distinct else ""} {columns} from {table} ' + \
                (f' where {where} ' if where else ' ') + \
                (f' order by {order_by_column} ' if order_by_column else ' ') + \
                (f' limit {limit} ' if limit else ' ')
        result = await self.pool.fetch(query)
        print(result)
        if not result:
            raise HTTPException(status_code=404, detail='Not found')
        return result

    async def insert(self, table: str, fields: tuple, values: tuple, on_conflict: (str, str) = None):
        def get_value(value):
            if type(value) is bool or type(value) is int or value is None:
                return f'{value}'
            else:
                return f"'{value}'"

        query = f'insert into {table} ({", ".join(fields)}) values ({", ".join(list(map(get_value, values)))}) ' + \
            (f"on conflict ({on_conflict[0]}) {on_conflict[1]}" if on_conflict else '') + \
                f' returning *'
        return await self.execute(query)

    async def update(self, table: str, fields: list, values: list, where: str):
        def get_set(field, value):
            return f'{field}' + ' = ' + (str(value) if type(value) is int else f"'{value}'") + ','

        sett = ' '.join(list(map(get_set, fields, values)))[:-1]
        query = f'update {table} \n' + \
                f'set ' + sett + '\n' + \
                f'where ' + where + \
                f'returning *'
        return await self.execute(query)

    async def delete(self, table: str, where: str = None):
        query = f'delete from {table}' + (f' where {where}' if where else '')
        return await self.pool.fetch(query)

    async def execute(self, query: str):
        try:
            result = await self.pool.fetch(query)
            print(result)
            if not result:
                raise HTTPException(status_code=404, detail='Not found')
            return result
        except UniqueViolationError:
            raise HTTPException(status_code=409, detail='Conflict')
        except InternalServerError:
            raise HTTPException(status_code=500, detail='Server error')
