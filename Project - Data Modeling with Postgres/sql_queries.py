# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"


# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time timestamp, userId int, level varchar, songId varchar, artistId varchar, sessionId int, location Varchar, userAgent Varchar);")

user_table_create = ("""Create table if not exists users(userId INT, firstName Varchar, lastName Varchar, gender varchar, level varchar)""")

song_table_create = ("""Create table if not exists songs(song_id varchar, title varchar, artist_id varchar, year INT, duration float)""")


artist_table_create = ("""Create table if not exists artists(artist_id varchar, artist_name varchar, artist_location varchar, artist_latitude varchar, artist_longitude varchar)""")

time_table_create = ("""Create table if not exists time(start_time varchar, hour INT, day INT, week INT, month INT, year INT, weekday varchar)
""")


# INSERT RECORDS


songplay_table_insert = ("""INSERT INTO songplays (start_time, userId, level, songId, artistId, sessionId, location, userAgent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")

user_table_insert = ("""insert into users(userId, firstName, lastName, gender, level) Values (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""")

song_table_insert = ("""insert into songs(song_id, title, artist_id, year, duration) Values (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""")

artist_table_insert = ("""insert into artists(artist_id, artist_name, artist_location, artist_latitude, artist_longitude) Values(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""")


time_table_insert = ("""insert into time(start_time, hour, day, week, month, year, weekday) Values (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING""")

# FIND SONGS

song_select = ("""Select song_id, artist_id from songs""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create, Dsong_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop,Dsong_table_drop]