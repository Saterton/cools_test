def get_attr_text(item, attr):
    return getattr(item.find(attr), 'text', '')
