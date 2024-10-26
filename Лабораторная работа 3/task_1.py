# TODO Напишите функцию для поиска индекса товара

def finder(items, x):
    len_items = len(items)
    i = 0
    while i < len_items and items[i] != x:
        i+=1
    if i >= len_items:
        return None
    return i

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = finder(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
