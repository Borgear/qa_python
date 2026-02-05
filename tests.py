import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector): # проверка добавления двух книг
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_names', ['', 'Джордж Оруэлл 1984 война - это мир 41 сим',])
    def test_add_new_book_add_negative_book(self, collector, book_names): # негативная проверка количества символов в названии книги (0 символов, 41 символ) 
        collector.add_new_book(book_names)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_added_genre_book_positive_result(self, collector): # проверка установки жанра книги
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.books_genre.get('1984') == 'Фантастика'

    def test_set_book_genre_add_genre_is_not_list(self, collector):  # проверка что жанр книги не устанавливается если его нет в списке жанров
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Жанр')
        assert collector.books_genre.get('1984') == ''

    def test_get_book_genre_for_name_positive_result(self, collector): # проверка возврата жанра книги по названию
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_get_books_with_specific_genre_get_two_books_fantasy(self, collector): # проверка возврата словаря книг с жанром 'Фантастика' 
        collector.books_genre = {'1984': 'Фантастика', 'Азазель': 'Детективы', 'Отель Оюнсу': 'Ужасы',
                               'Скотный двор': 'Фантастика'}
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_for_children_two_books(self, collector): # проверка возврата книг доступных для детей
        collector.books_genre = {'1984': 'Фантастика', 'Азазель': 'Детективы', 'Отель Оюнсу': 'Ужасы',
                               'Данте': 'Комедии'}
        assert len(collector.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_one_book(self, collector): # проверка добавления книг в избранное
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert len(collector.get_list_of_favorites_books()) == 1 and collector.favorites[0] == '1984'

    def test_add_book_in_favorites_add_two_twin_book(self, collector): # проверка на задвоение книг в избранном
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('1984')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector): # проверка удаления книг из избранного
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert len(collector.favorites) == 0
