

def create_block_key(row):
    pan = str(row.get('pan', '')).strip()
    if pan:
        return pan  # strongest key

    name = str(row.get('name', ''))[:3]
    pincode = str(row.get('pincode', ''))
    return f"{pincode}_{name}"