# Створити dataset та працювати з ним
def convert_2_dict(lst):
    if len(lst[0]) == 2:
        return {'quantity': lst[0][0], 'price': lst[0][1]}
    dct = {}
    for sublst in lst:
        key = sublst[0]
        if key not in dct:
            dct[key] = []
        dct[key].append(sublst[1:])
    for key in dct:
        dct[key] = convert_2_dict(dct[key])
    return dct
with open('orders.csv', encoding='utf-8') as mydataset:
    mydataset.readline()
    file = [[el.strip() for el in line.split(',')] for line in mydataset]
    result = convert_2_dict(file)



# Які продукти купляли усі покупці?
empty_set=set()
for humen, data in result.items():
    for data,product in data.items():
        empty_set=empty_set.union(product.keys())
for humen in result:
    second_set=set()
    for data in result[humen]:
        second_set=second_set.union(result[humen][data].keys())
    #print(empty_set)
    empty_set=empty_set.intersection(second_set)

#print(empty_set)
    


# Як змінювалась ціна на яблука? (графік)
'''
apples_price=[]
time=[]
for dates in result.values():
    for data,more_data in dates.items():
        for i_need_more_data, wtf in more_data.items():
            if i_need_more_data=='apple':
                apples_price.append(wtf['price'])
                time.append(data)
print(apples_price)
print(time)
'''
#import plotly.offline as pl
#import plotly.graph_objs as go
'''
data = go.Scatter(x=time.sort(),  y=apples_price)
pl.plot([data])

                
   '''             

# Скільки грошей витрачає кожний покупець на покупки? (графік)
'''
empty_dct=dict()
for human,about_human in result.items():
    products=[]
    for a,product in about_human.items():
        for __,product_info in product.items():
            products.append(product_info['price'])
            products=[float(a) for a in products]
            empty_dct[human]=sum(products)
list_of_names=[]
[list_of_names.append(a) for a in empty_dct.keys()]
list_of_price=[]
[list_of_price.append(a) for a in empty_dct.values()]
data=go.Bar(x=list_of_names, y=list_of_price)
pl.plot([data])

print(empty_dct)

'''
# Який найпопулярніший товар?
'''
products=[]
for human,about_human in result.items():
    for a,product in about_human.items():
        [products.append(a) for a in product.keys()]
products.sort()
popular_list=[]
sort_set_products=list(set(products))
sort_set_products.sort()
empty_dct=dict()
products=[products.count(item) for item in sort_set_products]
def sas(sort_set_products, products, empty_dct=dict()):
    if products==[]:
        return empty_dct
    empty_dct[products[0]]=sort_set_products[0]
    return sas(sort_set_products[1:], products[1:], empty_dct)
print(sas(sort_set_products, products).pop(max(sas(sort_set_products, products).keys())))
'''


# Якого товару було куплено найменше?
'''
empty_dct=dict()
products=[]
for human,about_human in result.items():
    for a,product in about_human.items():
        for key,product_info in product.items():
            for a,b in product_info.items():
                if a=='quantity':
                    if key not in empty_dct.keys():
                        empty_dct[key]=[float(b)]
                    else:
                        empty_dct[key].append(float(b))
for key, value in empty_dct.items():
    empty_dct[key]=sum(value)
max=0
for key, value in empty_dct.items():
    if float(value)>max:
        max=float(value)
mini=max
for value in empty_dct.values():
    if float(value)<mini:
        mini=float(value)
for a,b in empty_dct.items():
    if b==mini:
        print(a, b)
'''

# Який найдорожчий товар?
'''
empty_dct=dict()
for human,about_human in result.items():
    for a,product in about_human.items():
        for key,product_info in product.items():
            for a,b in product_info.items():
                if a=='price':
                    if key not in empty_dct.keys():
                        empty_dct[key]=[float(b)]
                    else:
                        empty_dct[key].append(float(b))
for key, value in empty_dct.items():
    empty_dct[key]=max(value)
print(empty_dct)
max=0
for key, value in empty_dct.items():
    if float(value)>max:
        max=float(value)
for a,b in empty_dct.items():
    if b==max:
        print(a, b)
        '''
# Якого товару, скільки покупців купляє? (графік)

# Написати функціонал для додавання нових даних
def convert_two_dict(lst):
    if len(lst[0]) == 2:
        return {'quantity': lst[0][0], 'price': lst[0][1]}
    dct = {}
    for sublst in lst:
        key = sublst[0]
        if key not in dct:
            dct[key] = []
        dct[key].append(sublst[1:])
    for key in dct:
        dct[key] = convert_two_dict(dct[key])
    return dct
