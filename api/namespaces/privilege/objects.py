from database.dbconnection import connect_to_postgres


class Privilege:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_privilege(privilege_name: str):
        conn = connect_to_postgres()
        cursor = conn.cursor()
        try:
            cursor.execute("""]
                SELECT privilege FROM userprivileges 
                WHERE privilege = %s;
            """, (privilege_name,)
            )
            fetch = cursor.fetchone()
            if not fetch:
                return None

            privilege = Privilege(fetch[0])
        except:
            return None
        finally:
            conn.close()

        return privilege

    def register(self):
        conn = connect_to_postgres()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT privilege FROM userprivileges
                WHERE privilege = %s
            """, (self.name,))

            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO userprivileges (privilege)
                    VALUES (%s);
                """, (self.name,))
                conn.commit()

                return True
        except Exception as e:
            print(e)
            return False
        finally:
            conn.close()

        return True