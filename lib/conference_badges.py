def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for n in names:
        badges.append(f'Hello, my name is {n}.')
    return badges

def assign_rooms(names):
    rooms = []
    room = 1
    for n in names:
        rooms.append(f"Hello, {n}! You'll be assigned to room {room}!")
        room += 1
    return rooms

def printer(names):
    for n in batch_badge_creator(names):
        print(n)
    for n in assign_rooms(names):
        print(n)
