use sakila;

SELECT first_name, last_name FROM actor; -- 1a.

ALTER TABLE actor ADD COLUMN Actor_Name VARCHAR(50);

SET SQL_SAFE_UPDATES=0;
UPDATE actor SET Actor_Name = CONCAT(UPPER(first_name)," ",UPPER(last_name)); -- 1b.

SELECT actor_id,first_name,last_name FROM actor WHERE first_name = 'Joe'; -- 2a

SELECT actor_id,first_name,last_name FROM actor WHERE last_name LIKE '%GEN%' ; -- 2b

SELECT actor_id,first_name,last_name FROM actor WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name; -- 2c

SELECT country_id,country FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China'); -- 2d

ALTER TABLE actor ADD COLUMN middle_name VARCHAR(50) AFTER first_name; -- 3a

ALTER TABLE actor MODIFY middle_name BLOB; -- 3b

ALTER TABLE actor DROP COLUMN middle_name; -- 3c

SELECT last_name, COUNT(*) as 'Count of Same Last Names' FROM actor GROUP BY last_name /* Extra flair */ ORDER BY COUNT(*) DESC; -- 4a

SELECT last_name, COUNT(*) as 'Count of Same Last Names' FROM actor GROUP BY last_name HAVING COUNT(*) > 1; -- 4b

UPDATE actor SET first_name = 'HARPO' WHERE (first_name ='GROUCHO' AND last_name ='Williams'); -- 4c

UPDATE actor SET first_name = CASE
								WHEN first_name = 'HARPO' THEN 'GROUCHO'
                                WHEN first_name = 'GROUCHO' THEN 'MUCHO GROUCHO'
                                ELSE first_name
							END; -- 4d
                            
SHOW CREATE TABLE address; -- 5a

SELECT staff.first_name, staff.last_name, address.address FROM staff JOIN address ON address.address_id = staff.address_id; -- 6a

SELECT staff.first_name, staff.last_name, SUM(payment.amount) as Rung_up_Amount FROM staff 
	JOIN payment ON staff.staff_id = payment.staff_id 
		WHERE payment.payment_date LIKE '2005-08%' GROUP BY staff.last_name; -- 6b

SELECT film.title, COUNT(film_actor.actor_id) as Actor_Count FROM film 
	INNER JOIN film_actor ON film.film_id=film_actor.film_id 
		GROUP BY film.title ORDER BY Actor_Count DESC; -- 6c

SELECT film.title, COUNT(inventory.inventory_id) FROM film 
	JOIN inventory ON film.film_id=inventory.film_id WHERE film.title = 'Hunchback Impossible'; -- 6d

SELECT customer.first_name, customer.last_name, SUM(payment.amount) 
	FROM customer JOIN payment ON customer.customer_id = payment.customer_id
GROUP BY customer.last_name
ORDER BY customer.last_name ASC; -- 6e

SELECT title FROM film
WHERE title LIKE 'K%' OR title LIKE 'Q%'
AND film.language_id =  (SELECT language_id 
FROM language WHERE name = 'English'); -- 7a

SELECT first_name, last_name FROM actor WHERE actor.actor_id IN
			(SELECT actor_id FROM film_actor WHERE film_actor.film_id = (SELECT film_id FROM film
							WHERE title = 'Alone Trip')); -- 7b

SELECT customer.first_name, customer.last_name, customer.email FROM customer
	JOIN address ON customer.address_id = address.address_id 
		JOIN city ON address.city_id=city.city_id 
			JOIN country ON city.country_id=country.country_id WHERE Country = 'Canada'; -- 7c

SELECT title FROM film WHERE film_id IN 
		(SELECT film_id FROM film_category WHERE category_id = 
			(SELECT category_id FROM category WHERE name = 'Family')); -- 7d

SELECT film.title, COUNT(*) as Number_of_Rentals FROM film 
	RIGHT JOIN inventory ON film.film_id=inventory.film_id 
		RIGHT JOIN rental ON inventory.inventory_id=rental.inventory_id
GROUP BY film.title
ORDER BY COUNT(*) DESC; -- 7e

SELECT store.store_id, SUM(payment.amount) FROM store
	JOIN inventory ON store.store_id=inventory.store_id 
		JOIN rental ON inventory.inventory_id = rental.inventory_id
			JOIN payment ON rental.rental_id=payment.rental_id
GROUP BY store_id; -- 7f

SELECT store.store_id, city.city, country.country FROM store
JOIN address ON store.address_id = address.address_id
		JOIN city ON address.city_id = city.city_id
			JOIN country ON city.country_id = country.country_id; -- 7g
            
SELECT category.name as Genre, SUM(payment.amount) as 'Gross Revenue' FROM category
	JOIN film_category ON category.category_id = film_category.category_id
		JOIN inventory ON film_category.film_id = inventory.film_id
			JOIN rental ON inventory.inventory_id = rental.inventory_id
				JOIN payment ON rental.rental_id = payment.rental_id
GROUP BY category.name
ORDER BY SUM(payment.amount) DESC
LIMIT 5; -- 7h

CREATE VIEW top_five_genres AS 
SELECT category.name as Genre, SUM(payment.amount) as 'Gross Revenue' FROM category
	JOIN film_category ON category.category_id = film_category.category_id
		JOIN inventory ON film_category.film_id = inventory.film_id
			JOIN rental ON inventory.inventory_id = rental.inventory_id
				JOIN payment ON rental.rental_id = payment.rental_id
GROUP BY category.name
ORDER BY SUM(payment.amount) DESC
LIMIT 5; -- 8a

SELECT * FROM top_five_genres; -- 8b

DROP VIEW top_five_genres; -- 8c

