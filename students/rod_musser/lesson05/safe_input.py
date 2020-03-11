def safe_input():
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        return None
