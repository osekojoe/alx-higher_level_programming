-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
--   You can use a maximum of two SELECT statement
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN
(
	SELECT tv_genres.id, tv_genres.name -- Query to get Dexter genres
	FROM tv_genres
	JOIN tv_show_genres
	     ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows
	     ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = "Dexter"
	ORDER BY tv_genres.id
) dexter_genres ON dexter_genres.id = tv_genres.id
WHERE dexter_genres.id is NULL
ORDER BY tv_genres.name;