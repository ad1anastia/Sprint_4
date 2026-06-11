import pytest
import constants as c
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def collector_book_with_genre( collector):
    collector.add_new_book(c.BOOK_ANIMATION_FILMS)
    collector.set_book_genre(c.BOOK_ANIMATION_FILMS, c.GENRE_ANIMATED_FILM)
    return collector

@pytest.fixture
def collector_with_many_books(collector):
    books = [
        (c.BOOK_FANTACY, c.GENRE_FANTACY),
        (c.BOOK_HORROR, c.GENRE_HORROR), 
        (c.BOOK_ANIMATION_FILMS, c.GENRE_ANIMATED_FILM),
        (c.BOOK_COMEDY, c.GENRE_COMEDY), 
        (c.BOOK_DETECTIVE, c.GENRE_DETECTIVE)
    ]
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector

@pytest.fixture
def collector_with_favorite(collector):
    collector.add_new_book(c.BOOK_ANIMATION_FILMS)
    collector.add_book_in_favorites(c.BOOK_ANIMATION_FILMS)
    return collector

