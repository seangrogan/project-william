def banner(msg=None, *, fill='*', width=80):
    if msg is None:
        msg = 'Tornado Drone Routing Program'
    width = max(width, len(msg) + 4)
    print(f"{'':{fill}<{width}}")
    print(f"{fill}{msg: ^{width - 2}}{fill}")
    print(f"{'':{fill}<{width}}")
