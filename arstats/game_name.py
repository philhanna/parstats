def to_section_name(gameName: str) -> str:
    """
    Converts a game name to the corresponding section name.  Hyphens are
    converted to underscores and ".scm" is appended.
    """
    sName = gameName.strip()
    if sName != "":
        sName = sName.lower()
        sName = sName.replace(" ", "_")
        sName = sName.replace("-", "_")
        sName += ".scm"
    return sName

def to_title_case(name: str) -> str:
    """
    Makes the first character of a name uppercase, and the remainder (if
    any) lower case. Leading and trailing spaces are removed.
    """
    name = name.strip()
    if len(name) == 0:
        return name
    if len(name) == 1:
        return name.upper()
    prefix = name[:1]
    suffix = name[1:]
    return prefix.upper() + suffix.lower()
