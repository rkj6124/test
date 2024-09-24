def convert_str_to_bool(value: str, default: bool) -> bool:
    try:
        if value is None:
            return default
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
        else:
            return default
    except Exception as e:
        return default
