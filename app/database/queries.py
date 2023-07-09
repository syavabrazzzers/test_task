# from asyncpg import UniqueViolationError
# from fastapi import HTTPException
# from pydantic import BaseModel
#
# from database.database import Connection
#
#
# async def get_all_servers(connection):
#     cursor = connection.cursor()
#     cursor.execute(f'SELECT * FROM servers')
#     data = cursor.fetchall()
#     cursor.close()
#     print(data)
#
#
# async def get_server_by_type(connection, type):
#     # cursor.execute(f"SELECT * FROM servers WHERE type={type}")
#     data = await connection.fetch(f"""SELECT
# 	s.id,
# 	s.host,
# 	s.name,
# -- 	s.type,
# 	st.type
# FROM servers as s
# JOIN (SELECT st.id, st.type FROM server_types AS st) as st on st.id = s.type
# WHERE s.type={type};""")
#
#     print(data)
#     return data
#
#
# async def get_server_by_id(connection, id):
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM servers JOIN server_types ON servers.type = server_types.id WHERE servers.id={id}")
#     data = cursor.fetchall()
#     return data
#
#
# async def insert_query(connection, table: str, model: BaseModel):
#     nmodel = model.dict()
#     nmodel.pop('id')
#     keys = ''
#     for key in nmodel.keys():
#         keys += ' '
#         keys += f'{key},'
#     keys = keys[:-1]
#     values = ""
#     for value in nmodel.values():
#         values += " "
#         values += f"'{value}',"
#     values = values[:-1]
#
#     query = f"INSERT INTO {table}({keys}) VALUES({values}) RETURNING *;"
#     print(query)
#     data = await fetch(connection, query)
#     return data
#
#
# async def select_user(conn: Connection.connect, user: User):
#     query = f"SELECT * FROM users WHERE login='{user.login}'"
#     data = await fetch(conn, query)
#     return data
#
#
# async def insert_user(conn: Connection.connect, user: User):
#     query = f"INSERT INTO users (login) values ('{user.login}') RETURNING *"
#     data = await fetch(conn, query)
#     return data
#
#
# async def get_all_users(connection):
#     cursor = connection.cursor()
#     cursor.execute(f'SELECT * FROM users')
#     data = cursor.fetchall()
#     print(data)
#
#
# async def get_server_types(connection):
#     # cursor = connection.cursor()
#     result = await connection.fetch(f'SELECT * FROM server_types')
#     data = result
#     print(data)
#     return data
#
#
# async def select(connection, table: str, like: str,
#                  fields: str = '*', where: str = '',
#                  order_by: str = ''):
#     pass
#
#
# async def fetch(conn: Connection.connect, query):
#     try:
#         data = await conn.fetch(query)
#         data = [dict(d.items()) for d in data]
#     except UniqueViolationError:
#         raise HTTPException(status_code=409, detail={'message': 'Already exists'})
#     # except Exception as e:
#     #     raise HTTPException(status_code=)
#     return data


