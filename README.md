# Sprint_4
# qa_python

Приложение `BooksCollector` позволяет устанавливать жанр книг и добавлять их в избранное.

Тесты для приложения `BooksCollector` из [main.py](main.py).

## Запустить тесты из терминала можно такой командой:

```bash
pytest -v tests.py 
```

## Описание тестов

### `add_new_book` — добавление книги

- `test_add_new_book_add_one_book` —  Добавляется книга в словарь
- `test_add_new_book_genre_is_empty` —  Добавляется книга с пустым жанром
- `test_add_new_book_not_added` — Книга с именем длиннее 40 символов или пустым именем не добавляется
- `test_add_new_book_add_two_books` — Успешно добавляются две разные книги
- `test_add_new_book_add_duplicate_book` — Повторное добавление книги не создает дубликат в словаре 

### `set_book_genre` — установка жанра

- `test_set_book_genre_add_genre_book` — Соществующей книге успешно присваивается жанр
- `test_set_book_genre_not_set` — Несуществующий жанр не перезаписываети текущий жанр книги

### `get_book_genre` — получение жанра книги

- `test_get_book_genre_existing_book_returns_genre` —  После добавления книги, возвращает правильный жанр 
- `test_get_book_genre_after_adding_book_list_not_empty` — После добавления книги, у книги поле жанра не пустое

### `get_books_with_specific_genre` — книги по жанру

- `test_get_books_with_specific_genre_expecting_genre_returns_books` — Для каждого жанра должена вернуться книга этого же жанра
- `test_get_books_with_specific_genre_returns_empty_list` — Если жанр не входит в список доступных, должен вернуться пустой список 

### `get_books_for_children` — книги для детей

- `test_get_books_for_children_without_age_rating_returned` — Книга без возрастного рейтинга должны присутствовать в детском списке
- `test_get_books_for_children_with_age_rating_not_returned` — Книги с возрастным рейтингом не попадают в список для детей

### `add_book_in_favorites` — добавление в избранное

- `test_add_book_in_favorites_book_not_from_dict_not_added` — Книга не находящаяся в словаре не добавляется в избранное
- `test_add_book_in_favorites_book_from_dict_added` — Книга из основного словаря должна успешно добавиться в избранное
- `test_add_book_in_favorites_duplicate_book_added_once` — Повторое добавление книги в избранное не создает дубликат в списке
### `delete_book_from_favorites` — удаление из избранного

- `test_delete_book_from_favoritesbook_removed` — Книга успешно удалилась из избранного и больше не отображается в списке 

### `get_list_of_favorites_books` — список избранного

- `test_get_list_of_favorites_books_returns_only_added_books` — Добавляем одну книгу в избранное - ожидаем список из одного элемента
