def print_table(headers=["ID", "Username", "Password Hashed"], rows=[]):

    col_widths = [max(len(str(item)) for item in col) for col in zip(*rows, headers)]
    print(" | ".join(f"{str(headers[i]).ljust(col_widths[i])}" for i in range(len(headers))))
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    for row in rows:
        print(" | ".join(f"{str(row[i]).ljust(col_widths[i])}" for i in range(len(row))))

def add_row(data, id:int, username:str, password:str):
    data.append([id, username, password])