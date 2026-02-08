# qa_python 4 sprint

# Написана фикстура для создания экземпляра класса в каждом тесте conftest.py

# Реализованные тесты:
# 1  test_add_new_book_positive_and_negative проверка добавления книг 0,1,12,40,41 символ
# 2  test_set_book_genre_added_genre_book_positive_result(self, collector): # проверка установки жанра книги
# 3  test_get_books_genre_returns_correct_dictionary(self, collector): # проверка получения всего словаря книг
# 4  test_set_book_genre_add_genre_is_not_list(self, collector):  # проверка что жанр книги не устанавливается если его нет в списке жанров
# 5  test_get_book_genre_for_name_positive_result(self, collector): # проверка возврата жанра книги по названию
# 6  test_get_books_with_specific_genre_get_two_books_fantasy(self, collector): # проверка возврата словаря книг с жанром 'Фантастика' 
# 7  test_get_books_for_children_two_books(self, collector): # проверка возврата книг доступных для детей
# 8  test_add_book_in_favorites_add_one_book(self, collector): # проверка добавления книг в избранное
# 9  test_add_book_in_favorites_add_two_twin_book(self, collector): # проверка на задвоение книг в избранном
# 10 test_delete_book_from_favorites(self, collector): # проверка удаления книг из избранного
