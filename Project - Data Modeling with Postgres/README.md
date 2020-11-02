# Sparkify Project

Sparkify is a music streaming company that collects data on songs and user activities. The objectives of this project is to create a data pipline for the company so that the songs and user activities data can be easily queried and analyzed to make informed decisions.

I obtained Sparkify's existing data from two directories containing JSON files containing songs and activities data.

For my Data Modeling, I chose Star Schema in order to enable simple, fast queries for analytical processing. I created the following tables

FACT Table:
songplay

Dimension Tables
user
song
artist
time

Included in this report as some supplemental files. These are:

sql_queries.py: This contains SQL script to drop the above-named tables if they already exist. It also contains queries to create all of the tables above and insert data into them.Lastly, it contains a query that selects data from the songs table.

create_tables.py : This is a python script that drops sparkifydb if it already exists and re-creates it. It uses the queries in sql_queries.py to create all the tables above. I ran this script by typingthe following in a python terminal
python3 create_tables.py

etl.ipynb: I used this notebook to read a single file from song_data and log_data and load the data into the tables tables above. This serves as a test before running my mail etl script.

test.ipynb: I used this notebook as a check to see if insert are successful. It contains codes to select records from the above tables after inserting records into them.

etl.py. This is the main script that reads all of the records in song_data and log_data and load the data into the tables tables above. I ran this script by typingthe following in a python terminal
python3 etl.py

While the etl.py script was running, the CLI showed the number of records found nd the number of records processed.

![Song_data_files_processed](/home/workspace/Song_data_files_processed.png)

![Song_data_files_processed](https://r766469c826263xjupyterllyjhwqkl.udacity-student-workspaces.com/lab/tree/Song_data_files_processed.PNG)