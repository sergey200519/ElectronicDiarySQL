def tables_create(db):
    if db.table_is_exists("admins"):
        print("admins table created successfully ------------")
        fields = {
            "username": "VARCHAR(255)",
            "password": "TEXT",
            "fullname": "TEXT"
        }
        db.create_table("admins", fields=fields, id=True)
    
    if db.table_is_exists("groups"):
        print("groups table created successfully ------------")
        fields = {
            "name": "VARCHAR(255)"
        }
        db.create_table("groups", fields=fields, id=True)
    
    if db.table_is_exists("teachers"):
        print("teachers table created successfully ------------")
        fields = {
            "username": "VARCHAR(255)",
            "password": "TEXT",
            "fullname": "TEXT",
            "groups": "TEXT",
            "subject": "TEXT"
        }
        db.create_table("teachers", fields=fields, id=True)
    
    if db.table_is_exists("students"):
        print("students table created successfully -------------")
        fields = {
            "username": "VARCHAR(255)",
            "password": "TEXT",
            "fullname": "TEXT",
            "group_id": "INTEGER"
        }
        other = "FOREIGN KEY(group_id) REFERENCES groups(ID) ON DELETE CASCADE"
        db.create_table("students", fields=fields, id=True, other=other)

    if db.table_is_exists("homeworks"):
        print("homeworks table created successfully ------------")
        fields = {
            "teacher_id": "INTEGER",
            "group_id": "INTEGER",
            "homework": "TEXT",
            "deadline": "VARCHAR(255)",
            "students_completed": "TEXT"
        }
        other = "FOREIGN KEY(group_id) REFERENCES groups(ID) ON DELETE CASCADE"
