import psycopg2

print("Welcome to the dictionary, the following commands are available:")
print("Use commands: list, add, delete, quit")

conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="postgres",
   password="Vera1234?"
)
# read_dict: returns the list of all dictionary entries: 
#   argument: C - the database connection
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# read_dict: returns the list of all dictionary entries: 
#   argument: C - the database connection
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# read_dict: returns the list of all dictionary entries: 
#   argument: C - the database connection
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# read_dict: returns the list of all dictionary entries: 
#   argument: C - the database connection
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
