import csv

def read_users():
    with open("users.csv", "r") as f:
        reader = csv.reader(f)
        return list(reader)
    
def write_users(users):
    with open("users.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(users)
        
def update_user(name, score):
    users = read_users()
    for user in users:
        if user[0] == name:
            user[1] = score
            write_users(users)
            return
    users.append([name, score])
    write_users(users)
