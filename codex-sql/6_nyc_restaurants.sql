
--SELECT *
--FROM restaurants;

--What are all the unique cuisines in the table?

--SELECT DISTINCT cuisine
--FROM restaurants; 

--What are all the Chinese restaurants? Italian?

--SELECT *
--FROM restaurants
--WHERE cuisine LIKE '%Chinese%';

--SELECT *
--FROM restaurants
--WHERE cuisine LIKE '%Italian%';

--What are all the spots in Greenpoint (a neighborhood in Brooklyn)?

--SELECT *
--FROM restaurants 
--WHERE neighborhood = 'Greenpoint';

--Where are the cheap eats? The bougie ones?
SELECT *
FROM restaurants
WHERE price = '$';
