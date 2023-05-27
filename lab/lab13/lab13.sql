.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT name, store FROM products AS p, lowest_prices AS l
    WHERE p.name = l.item
    GROUP BY category HAVING MIN(MSRP / rating);


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs) FROM stores AS s, shopping_list AS l
    WHERE s.store = l.store;

