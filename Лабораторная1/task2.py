# TODO Найдите количество книг, которое можно разместить на дискете
i_volume = 1509949 #байты
c_page = 100
c_str = 50
c_symbols = 25
book_c = c_page*c_str*c_symbols*4
count_of_books = 0
while (i_volume - book_c) >= 0:
    i_volume -= book_c
    count_of_books += 1

print("Количество книг, помещающихся на дискету:", count_of_books)
