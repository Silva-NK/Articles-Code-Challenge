-- SQL schema definitions

-- Authors Table
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


-- Magazines table
CREATE TABLE IF NOT EXISTS magazines (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    category VARCHAR(255) NOT NULL
);


-- Article Table
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INTEGER NOT NULL,
    magazine_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (magazine_id) REFERENCES magazines(id)
);