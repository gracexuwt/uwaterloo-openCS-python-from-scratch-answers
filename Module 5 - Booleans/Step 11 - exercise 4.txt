def order_ors(any):
    return type(any) != type("") or len(any) < 2 or any[1] == "a"