import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # тестируем add_two_books - добавление двух книг, тест №1
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # проверяем установку жанра, тест №2
    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    # проверяем установку несуществующего жанра, тест №3
    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Какой-то неизвестный жанр')
        assert collector.get_book_genre('Гарри Поттер') == ''

    # проверяем наличие жанра и книги под него,тест №4
    @pytest.mark.parametrize('books, genre, expected', [
    #есть книга с жанром
    ([('Гарри Поттер', 'Фантастика'), ('Оно', 'Ужасы')], 'Фантастика', ['Гарри Поттер']),
     # жанр есть, но книг с ним нет
      ([('Гарри Поттер', 'Фантастика')], 'Мультфильмы', []),
    # жанр не из допустимых
    ([('Гарри Поттер', 'Фантастика')], 'Неизвестный жанр', []),
    # книг нет вообще
    ([], 'Фантастика', [])])
    def test_get_books_with_specific_genre_parametrized(self, collector, books, genre, expected):
        # добавляем книги в коллекцию
        for name, book_genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
        # вызываем метод, который тестируем
        result = collector.get_books_with_specific_genre(genre)
        # сравниваем фактический результат с ожидаемым
        assert result == expected

    # проверяем возврат пустого словаря,если еще книги не добавлены, тест №5
    def test_get_books_genre_not_empty(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        result = collector.get_books_genre()
        assert result == {'Гарри Поттер': 'Фантастика'}

    # проверяем возврат детских книг, тест №6
    def test_get_books_for_children_only_children(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        result = collector.get_books_for_children()
        assert result == ['Гарри Поттер']

    # проверяем добавление книги в избранное, тест №7
    def test_add_book_in_favorites_done(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        result = collector.get_list_of_favorites_books()
        assert result == ['Гарри Поттер']
    
    # проверяем удаление книги из Избранного,тест №8
    def test_delete_book_from_favorites_done(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        result = collector.get_list_of_favorites_books()
        assert result == []

    # проверяем получение списка Избранных книг, тест №9
    def test_get_list_of_favorites_books_done(self, collector):
        collector.favorites = ['Гарри Поттер', 'Шрек']
        result = collector.get_list_of_favorites_books()
        assert result == ['Гарри Поттер', 'Шрек']
    # проверяем работу метода get_book_genre, тест №10
    def test_get_book_genre_return_correct_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        result = collector.get_book_genre('Гарри Поттер')
        assert result == 'Фантастика'


    


