from core.domain import Book

def by_genre(genre_id: str):
    def pred(book: Book) -> bool:
        return book.genre == genre_id
    return pred

def by_tag(tag_id: str):
    def pred(book: Book) -> bool:
        return tag_id in book.tags
    return pred

def by_author(author_id: str):
    def pred(book: Book) -> bool:
        return book.author == author_id
    return pred

def by_year_range(start: int, end: int):
    def pred(book: Book) -> bool:
        return start <= book.year <= end
    return pred
