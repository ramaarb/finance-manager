import streamlit as st
from core.domain import Book
from core.transforms import by_genre, by_tag, by_author, by_year_range

# Пример данных
BOOKS = [
    Book("1", "Война и мир", "Толстой", "novel", ("classic",), 1869),
    Book("2", "Преступление и наказание", "Достоевский", "novel", ("classic",), 1866),
    Book("3", "Мастер и Маргарита", "Булгаков", "novel", ("fantasy",), 1967),
]

st.title("Library Manager — Lab 1")

# Фильтры
genre = st.text_input("Фильтр по жанру")
author = st.text_input("Фильтр по автору")
year_start = st.number_input("Год с", value=1800)
year_end = st.number_input("Год по", value=2025)

# Собираем предикаты
preds = []
if genre:
    preds.append(by_genre(genre))
if author:
    preds.append(by_author(author))
preds.append(by_year_range(year_start, year_end))

# Функция фильтрации
def match(book):
    return all(p(book) for p in preds)

filtered = [b for b in BOOKS if match(b)]

# Вывод
st.write("### Найденные книги:")
for b in filtered:
    st.write(f"**{b.title}** — {b.author} ({b.year})")
