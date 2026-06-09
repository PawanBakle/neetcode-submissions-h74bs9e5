-- Write your query below
-- 1 person may have many addresses
-- i have to join person and address based on person.id
-- SELECT first_name, last_name, COALESCE(city, null) , COALESCE(state, null)  FROM person JOIN address on 
-- person.person_id = address.person_id

SELECT first_name, last_name, COALESCE(city, NULL) AS city, COALESCE(state, NULL) AS state
FROM person
LEFT JOIN address ON person.person_id = address.person_id;   