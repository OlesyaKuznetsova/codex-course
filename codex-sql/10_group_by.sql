

SELECT artist, AVG(duration)
FROM playlist
GROUP BY artist;