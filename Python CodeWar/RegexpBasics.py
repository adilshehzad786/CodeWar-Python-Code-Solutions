def ipv4_address(address):
    ip_range = [str(x) for x in range(0, 256)]
    if not address or len(address.split('.')) != 4:
        return False

    for i in address.split('.'):
        if not i in ip_range:
            return False

    return True