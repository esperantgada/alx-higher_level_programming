-- List items
-- Lists all cities contained in the database hbtn_0d_us
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE state_id = states.id;
