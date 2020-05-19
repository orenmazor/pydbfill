# Usage

```
from pydbfill.pydbfill import fill_table, connection

connection = connection(
    host="db", username="root", password="0xDEADBEEF", port=3306, db="b5"
)

# remove constraints! nobody tells us what to do
with connection.cursor() as cursor:
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

fill_table(conn=connection, table_name="foo", count=1000)
fill_table(conn=connection, table_name="bar", count=1000)
fill_table(conn=connection, table_name="bat", count=100000)
fill_table(conn=connection, table_name="waldo", count=123)
fill_table(conn=connection, table_name="baz", count=1000)
```



# Licensing

```
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
