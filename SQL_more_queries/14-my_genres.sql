-- a script that uses the hbtn_0d_tvshows.
SELECT tv_genres.nam FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show ON tv_show_genres.show_id = tv_shows.id
WHERE tv.shows.title = "Dexter"
ORDER BY tv_genres.name ASC;