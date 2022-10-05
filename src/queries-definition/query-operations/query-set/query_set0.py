import edgedb
from edgeql_queries import from_path

conn = edgedb.connect()
queries = from_path("./queries.edgeql", async_driver=False)

users = queries.select_all_users(conn)
for user in users:
    print("user:", user.first_name)
