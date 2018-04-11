
CREATE TABLE celebs (
  id INTEGER,
  name TEXT,
  age INTEGER);

INSERT INTO celebs (id, name, age) VALUES (1, 'Justin Bieber', 21);
INSERT INTO celebs (id, name, age) VALUES (2, 'Beyonce Knowles', 33);
INSERT INTO celebs (id, name, age) VALUES (3, 'Jeremy Lin', 26);
INSERT INTO celebs (id, name, age) VALUES (4, 'Taylor Swift', 26);

UPDATE celebs
SET age = 22
WHERE id = 1;

/* 'NULL' is assigned to previously existing records' twitter_handle */
ALTER TABLE celebs ADD COLUMN twitter_handle TEXT;
DELETE FROM celebs WHERE twitter_handle is NULL;


/* Returns a new table with specified results */
SELECT * FROM celebs; /* Returns all */
SELECT name FROM celebs; /* Returns a table of only names */
SELECT name, genre FROM movies; /* Returns multiple columns in one query */
SELECT name AS 'Favorite Films' FROM movies; /* Use an alias in the returned table */
SELECT DISTINCT genre FROM movies; /* Filters out duplicates, returns one instance of each genre */
SELECT * FROM movies WHERE imdb_rating < 5; /* Use 'WHERE' for conditional querys */

/* Wildcards - 'LIKE' is not case-sensitive*/
SELECT * FROM movies WHERE name LIKE 'Se_en'; /* For a single character */
SELECT * FROM movies WHERE name LIKE '%man%'; /* % is for multiple chars */

/* Can't use = NULL or != NULL */
SELECT name FROM movies WHERE imdb_rating IS NULL;
SELECT name FROM movies WHERE imdb_rating IS NOT NULL;

/* BETWEEN works with numbers, text, dates. It's inclusive w/numbers, not with text */
SELECT * FROM movies WHERE name BETWEEN 'A' AND 'J'; /* A thru i */
SELECT * FROM movies WHERE year BETWEEN 1990 AND 1999; /* 1990 thru 1999 */
SELECT * FROM movies WHERE year BETWEEN 1970 AND 1979 AND imdb_rating > 8;
SELECT * FROM movies WHERE year < 1985 AND genre = 'horror';
SELECT * FROM movies WHERE year > 2014 OR genre = 'action';
SELECT * FROM movies WHERE genre = 'romance' OR genre = 'comedy';

/* ORDER BY has to follow WHERE (if used) and can be ASC or DESC
   and you can ORDER BY a field not returned in the results table */
SELECT name, year, imdb_rating FROM movies ORDER BY imdb_rating DESC;
SELECT * FROM movies ORDER BY imdb_rating DESC LIMIT 3; /* LIMIT goes at the end */

SELECT name,
	CASE
  	WHEN genre = 'romance' THEN 'fun' /* Give alt classifications to genres*/
    WHEN genre = 'comedy' THEN 'fun'
    ELSE 'serious'
  END AS 'mood' /* Make a new col in the return table called 'mood' */
FROM movies;

CREATE TABLE awards (
  /* PRIMARY KEY assigns unique value to rows - only one such key allowed */
  id INTEGER PRIMARY KEY,
  recipient TEXT NOT NULL,
  award_name TEXT DEFAULT "Grammy");

CREATE TABLE members (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    date_of_birth TEXT NOT NULL,
    date_of_death TEXT DEFAULT 'Not Applicable',
);

/* COUNT takes a col name as an arg */
SELECT COUNT(*) FROM fake_apps WHERE price = 0;
SELECT SUM(downloads) FROM fake_apps;
SELECT MAX(downloads) FROM fake_apps; /* or MIN or AVG */
SELECT name, ROUND(price, 0) FROM fake_apps; /* Rounds price to 0 decimal places */
SELECT ROUND(AVG(price), 2) FROM fake_apps; /* Rounds AVG price to 2 dec places */

/* Returns the count of apps at each price point */
SELECT price, COUNT(*)
FROM fake_apps
WHERE downloads > 20000
GROUP BY price; /* Has to come after any WEHRE clauses, but before ORDER BY or LIMIT */

/* Returns total downloads for each category */
SELECT category, SUM(downloads)
FROM fake_apps
GROUP BY category;

/* Returns avg downloads for each category at each price point */
SELECT category,
    price,
    AVG(downloads)
FROM fake_apps
GROUP BY 1, 2; /* Can reference cols by theorder in w/c they are selected */

/* Returns num of movies of diff genres were produced each year, but only for
yrs and genres w/at least ten movies */
SELECT year,
   genre,
   COUNT(name)
FROM movies
GROUP BY 1, 2
HAVING COUNT(name) > 10 /* HAVING comes after GROUP BY, before ORDER BY or LIMIT */

/* When we want to limit the results of a query based on values of the individual rows, we use WHERE.
When we want to limit the results of a query based on an aggregate property, we use HAVING. */

/* Joining tables - Gets all records from both tables, matching sub id from each */
SELECT
FROM orders
JOIN subscriptions
	ON subscriptions.subscription_id = orders.subscription_id;

/* Above is an inner join, below a left join. Inner join drops unmatched data,
Left join keeps the entry from the left table */
SELECT *
FROM newspaper
LEFT JOIN online
	ON newspaper.id = online.id
  WHERE online.id IS NULL;

/* A primary key like id is a foreign key in another table, and is often given a
descriptive name, as below */
SELECT *
FROM classes
JOIN students
	ON classes.id = students.class_id;

/* UNION stacks one dataset on another */
SELECT * FROM newspaper UNION SELECT * FROM online;


/* WITH combines tables when one is the result of another calculation */
WITH previous_query AS (
SELECT customer_id,
       COUNT(subscription_id) as subscriptions
FROM orders
GROUP BY customer_id)
SELECT customers.customer_name,
previous_query.subscriptions
FROM previous_query
JOIN customers
	ON customers.customer_id = previous_query.customer_id;
