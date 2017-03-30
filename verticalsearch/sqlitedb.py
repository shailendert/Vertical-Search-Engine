import sqlite3

sqlite_file = 'db.sqlite3'
# name of the sqlite database file
table_name = 'db_table'
# name of the table to be created
col1 = 'Title'
col2 = 'Price'
col3 = 'Availaibility'
col4 = 'Info'
col5 = 'URL'
# name of the column
field_type = 'Text'
# column data type  

# Connecting to the database
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()  


def new_table():
    c.execute('CREATE TABLE {tn} ({nf} {ft})'\
          .format(tn=table_name, nf=col1, ft=field_type))  
    #Adding columns in Table
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'{ct}"\
          .format(tn=table_name, cn=col2, ct=field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'{ct}"\
          .format(tn=table_name, cn=col3, ct=field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'{ct}"\
          .format(tn=table_name, cn=col4, ct=field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'{ct}"\
          .format(tn=table_name, cn=col5, ct=field_type))

    conn.commit()
#conn.close()
