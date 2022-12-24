from math import ceil
# p_c = 1 | #0 + 2
# p_c = 2 | #2 + 2
# p_c = 1 | #4 + 2
products = [ # list > dict > str, float
    { "name": "Salad", "price": 25.00 }, #0
    { "name": "Soup", "price": 15.00 },  #1 < min_i     < 1
    { "name": "Bread", "price": 5.00 },  #2
    { "name": "Kebab", "price": 50.00 }, #3

    { "name": "Pizza", "price": 100.00 }, #4
]

# ################filter data #################
# filter price: 15.00 .. 50
price_min = 15.00
price_max = 50.00
products_filtered = []

for i in range(len(products)):
    if products[i]["price"] >= price_min and products[i]["price"] <= price_max:
        products_filtered.append(products[i])
################# filtred data ###################

################# print  data ###################
# for i in range(len(products_filtered)):
#     print(f'{i} > {products_filtered[i]["name"]:25} {products_filtered[i]["price"]:7}MDL')
################# print  data ###################

################# min  ###################
min_i = 0
for i in range(len(products)):
    if products[i]["price"] <= products[min_i]["price"]:
        min_i = i

# print(f'{min_i} > {products[min_i]["name"]:25} {products[min_i]["price"]:7}MDL')
#################  /max ###################
#################  max ###################

# HW1: write algo FIND MAX
max_i = 0
for i in range(len(products)):
    if products[i]["price"] >= products[max_i]["price"]:
        max_i = i

# print(f'{max_i} < {products[max_i]["name"]:10} {products[max_i]["price"]:7}MDL')
#################  /max ###################

#################  SWAPPING ###################
index_a = 1
index_b = 3
# USE TRIANGLE algo
# product_temp = products[index_a]
# products[index_a] = products[index_b]
# products[index_b] = product_temp
#################  SWAPPING ###################

################## print  data ###################
#for i in range(len(products)):
#    print(f'{i} > {products[i]["name"]:25} {products[i]["price"]:7}MDL')
################## print  data ###################

# HW2. find by name ##############
# product_name = " ... " 
# for .. in .. + if + break

# f_product = input("Input product name: >") 
# for i in range(len(products)):
#     if products[i]["name"] == f_product:
#         print(f'{i} > {products[i]["name"]:25} {products[i]["price"]:7}MDL')
#         break
##########  /find by name ##############

###################SIMPLE PAGINATOR ##################
# --------
# [1] 2 3
from os import system

page_current = 4
while True:
    system("clear")  
    iteam_count  = len(products)
    per_page     = 2
    pages_total  = ceil(iteam_count / per_page)
    # ################ limits checker ####################
    if page_current > pages_total:
        page_current = pages_total
    elif page_current < 1:
        page_current = 1
    # ################ limits checker ####################
    start_index  = (page_current - 1) * per_page
    end_index    = start_index + per_page
    ################## print  data ###################
    for i in range(len(products)):
        if i >= start_index and i < end_index:
            print(f'{i} > {products[i]["name"]:25} {products[i]["price"]:7}MDL')
    ################## print  data ###################
    print()
    for page in range(1, pages_total + 1 ):
        if page == page_current:
            print(f"[{page}]", end= " ")
        else:
            print(page, end= " ")
    move = input("Use < and > move the page: ")
    if move == "<":
        page_current -= 1
    elif move == ">":
        page_current += 1
    print()
###################SIMPLE PAGINATOR ##################

# HW3: finish paginator 
# check limits
# < > - arrow 
# add page current 
# < ... 100 [101] 102 ... >









