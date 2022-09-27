def sneakers_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "brand": item["brand"],
        "price": item["price"],
    }


def sneakers_list_entity(entity) -> list:
    return [sneakers_entity(item) for item in entity]
