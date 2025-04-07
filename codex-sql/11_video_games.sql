

--SELECT *
--FROM games;

--What is the most popular game in the list?

--SELECT title, MAX(players)
--FROM games;

--What are the counts of all the programming languages?

--SELECT COUNT(language)
--FROM games;

--What are the average Metascores for each of the genres?

SELECT genre, AVG(metascore)
FROM games
GROUP BY genre;
