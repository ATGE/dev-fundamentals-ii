"""
utils
"""
def get_dict_by_key_value_from_list(key,value, array):
    """
    get_dict_by_key_value_from_list --> get dict by ke value from list
    Args:
        key: a key to lookup a value
        value: a value to lookup
        array: a array to search a matching value
    Return:
        Dictionary(dict): a dic
    """
    item_to_return = {}
    for item in array:
        if str(item.get(key)) == str(value):
            item_to_return = item
            break
    return item_to_return
    