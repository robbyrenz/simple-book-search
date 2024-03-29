import csv, os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    skip_first_line = True
    f = open("books.csv")
    reader = csv.reader(f)

    for isbn, title, author, year in reader:
        if skip_first_line == True:
            skip_first_line = False
            continue
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Added the book '{title}', by '{author}', published in {year}, isbn: {isbn}.")

    db.commit()
    print()
    print("*****Program Ended*****")


if __name__ == "__main__":
    main()
