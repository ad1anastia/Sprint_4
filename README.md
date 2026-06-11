# qa_python

Приложение `BooksCollector` позволяет устанавливать жанр книг и добавлять их в избранное.

Тесты для приложения `BooksCollector` из [main.py](main.py).

## Запустить тесты из терминала можно такой командой:

```bash
pytest -v tests.py 
```

## Описание тестов

### `add_new_book` — добавление книги

- `test_add_new_book_add_one_book` —  добавляется книга в словарь
- `test_add_new_book_genre_is_empty` —  добавляется книга с пустым жанром
- `test_add_new_book_not_added` — книга с именем длиннее 40 символов или пустым именем не добавляется
- `test_add_new_book_add_two_books` — успешно добавляются две разные книги
- `test_add_new_book_add_duplicate_book` — дубликат книги не добавляется повторно

### `set_book_genre` — установка жанра

- `test_set_book_genre_add_genre_book` — книге успешно присваивается жанр
- `test_set_book_genre_not_set` — несуществующий жанр не перезаписывает текущий

### `get_book_genre` — получение жанра книги

- `test_get_book_genre_existing_book_returns_genre` —  после добавления книги, возвращает правильный жанр
- `test_get_book_genre_affter_adding_book_list_not_empty` — после добавления книги, у книги поле жанра не пустое

### `get_books_with_specific_genre` — книги по жанру

- `test_get_books_with_specific_genre_expecting_genge_returns_books` — возвращается список книг нужного жанра
- `test_get_books_with_specific_genre_returns_empty_list` — несуществующий жанр возвращает пустой список

### `get_books_for_children` — книги для детей

- `test_get_books_for_children_without_age_rating_returned` — книги без возрастного рейтинга попадают в список
- `test_get_books_for_children_with_age_rating_not_returned` — книги с возрастным рейтингом не попадают в список

### `add_book_in_favorites` — добавление в избранное

- `test_dd_book_in_favorites_book_not_from_dick_not_added` — книга не из словаря не добавляется в избранное
- `test_dd_book_in_favorites_book_from_dick_added` — книга из словаря успешно добавляется в избранное
- `test_add_book_in_favorites_duplicate_book_added_once` — дубликат в избранное не добавляется

### `delete_book_from_favorites` — удаление из избранного

- `test_delete_book_from_favoritesbook_removed` — книга успешно удаляется из избранного

### `get_list_of_favorites_books` — список избранного

- `test_get_list_of_favorites_books_returns_only_added_books` — список содержит только добавленные книги
# Sprint_4
