def title_case(name):
    name = name.strip()
    if len(name) == 0:
        return name
    if len(name) == 1:
        return name.upper()
    prefix = name[:1]
    suffix = name[1:]
    return prefix.upper() + suffix.lower()