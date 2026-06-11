import pytest
import constants as c
from main import BooksCollector

class TestBooksCollector:
    
    # === add_new_book ===
    
    # Добавляется книга в словарь
    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book(c.BOOK_ANIMATION_FILMS)
        assert c.BOOK_ANIMATION_FILMS in collector.get_books_genre()

    # Добавляется книга с пустым жанром
    def test_add_new_book_genre_is_empty(self, collector):
        collector.add_new_book(c.BOOK_ANIMATION_FILMS)
        assert collector.get_book_genre(c.BOOK_ANIMATION_FILMS) == ''

    # Книга с именем длиннее 40 символов или пустым именем не добавляется
    @pytest.mark.parametrize('name_book', [
        'a' * 41,
        ''])
    def test_add_new_book_not_added(self, collector, name_book):
        collector.add_new_book(name_book)
        assert name_book not in collector.get_books_genre()

    # Успешно добавляются две разные книги
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book(c.BOOK_ANIMATION_FILMS)
        collector.add_new_book(c.BOOK_DETECTIVE)
        assert len(collector.get_books_genre()) == 2

    # Повторное добавление книги не создает дубликат в словаре 
    def test_add_new_book_add_duplicate_book(self, collector): 
        collector.add_new_book(c.BOOK_ANIMATION_FILMS)
        collector.add_new_book(c.BOOK_ANIMATION_FILMS)
        assert len(collector.get_books_genre()) == 1 

    # === set_book_genre ===
    
    # Соществующей книге успешно присваивается жанр
    def test_set_book_genre_add_genre_book(self, collector):
        collector.add_new_book(c.BOOK_ANIMATION_FILMS)
        collector.set_book_genre(c.BOOK_ANIMATION_FILMS, c.GENRE_ANIMATED_FILM)
        assert collector.get_book_genre(c.BOOK_ANIMATION_FILMS) == c.GENRE_ANIMATED_FILM

    # Несуществующий жанр не перезаписываети текущий жанр книги
    def test_set_book_genre_not_set(self, collector_book_with_genre):
        collector_book_with_genre.set_book_genre(c.BOOK_ANIMATION_FILMS, c.GENRE_UNKNOWN)
        assert collector_book_with_genre.get_book_genre(c.BOOK_ANIMATION_FILMS) == c.GENRE_ANIMATED_FILM

    # === get_book_genre ===

    # После добавления книги, возвращает правильный жанр 
    def test_get_book_genre_existing_book_returns_genre(self, collector_book_with_genre):
        assert collector_book_with_genre.get_book_genre(c.BOOK_ANIMATION_FILMS) == c.GENRE_ANIMATED_FILM
   
    # После добавления книги, у книги поле жанра не пустое
    def test_get_book_genre_after_adding_book_list_not_empty(self, collector_book_with_genre):
        assert collector_book_with_genre.get_book_genre(c.BOOK_ANIMATION_FILMS)
 
    # === get_books_with_specific_genre ===

    # Для каждого жанра должена вернуться книга этого же жанра
    @pytest.mark.parametrize('genre, expected', [
        (c.GENRE_FANTACY, [c.BOOK_FANTACY]), 
        (c.GENRE_HORROR, [c.BOOK_HORROR]), 
        (c.GENRE_ANIMATED_FILM, [c.BOOK_ANIMATION_FILMS])
        ])
    def test_get_books_with_specific_genre_expecting_genre_returns_books(self, collector_with_many_books, genre, expected):
        assert collector_with_many_books.get_books_with_specific_genre(genre) == expected


    # Если жанр не входит в список доступных, должен вернуться пустой список 
    def test_get_books_with_specific_genre_returns_empty_list(self, collector_book_with_genre):
        assert collector_book_with_genre.get_books_with_specific_genre(c.GENRE_UNKNOWN) == []

    # === get_books_for_children ===

    # Книга без возрастного рейтинга должны присутствовать в детском списке
    @pytest.mark.parametrize('book', [
        c.BOOK_ANIMATION_FILMS, 
        c.BOOK_COMEDY,
        c.BOOK_FANTACY
    ])
    def test_get_books_for_children_without_age_rating_returned(self, collector_with_many_books, book):
        assert book in collector_with_many_books.get_books_for_children()

    # Книги с возрастным рейтингом не попадают в список для детей
    @pytest.mark.parametrize('book', [
        c.BOOK_HORROR, 
        c.BOOK_DETECTIVE
    ])
    def test_get_books_for_children_with_age_rating_not_returned(self, collector_with_many_books, book):
        assert book not in collector_with_many_books.get_books_for_children()

    # === add_book_in_favorites ===

    # Книга не находящаяся в словаре не добавляется в избранное
    def test_add_book_in_favorites_book_not_from_dict_not_added(self, collector):
        collector.add_book_in_favorites(c.BOOK_NOT_IN_DICT)
        assert c.BOOK_NOT_IN_DICT not in collector.get_list_of_favorites_books()

    # Книга из основного словаря должна успешно добавиться в избранное
    def test_add_book_in_favorites_book_from_dict_added(self, collector_book_with_genre):
        collector_book_with_genre.add_book_in_favorites(c.BOOK_ANIMATION_FILMS)
        assert c.BOOK_ANIMATION_FILMS in collector_book_with_genre.get_list_of_favorites_books()

    # Повторое добавление книги в избранное не создает дубликат в списке
    def test_add_book_in_favorites_duplicate_book_added_once(self, collector_book_with_genre):
        collector_book_with_genre.add_book_in_favorites(c.BOOK_ANIMATION_FILMS)
        collector_book_with_genre.add_book_in_favorites(c.BOOK_ANIMATION_FILMS)
        assert collector_book_with_genre.get_list_of_favorites_books().count(c.BOOK_ANIMATION_FILMS) == 1
 
    # === delete_book_from_favorites ===

    # Книга успешно удалилась из избранного и больше не отображается в списке 
    def test_delete_book_from_favoritesbook_removed(self, collector_with_favorite):
        collector_with_favorite.delete_book_from_favorites(c.BOOK_ANIMATION_FILMS)
        assert c.BOOK_ANIMATION_FILMS not in collector_with_favorite.get_list_of_favorites_books()


    # === get_list_of_favorites_books ===

    # Добавляем одну книгу в избранное - ожидаем список из одного элемента
    def test_get_list_of_favorites_books_returns_only_added_books(self, collector_with_many_books):
        collector_with_many_books.add_book_in_favorites(c.BOOK_ANIMATION_FILMS)
        favorites = collector_with_many_books.get_list_of_favorites_books()
        assert len(favorites) == 1