"""Convierte a un csv como la gente... Netflix te odio!.

Nuevo formato:
currentMovieID, userID, rating, rating_date
1,1488844,3,2005-09-06
1,822109,5,2005-05-13
1,885013,4,2005-10-19
1,30878,4,2005-12-26
1,823519,3,2004-05-03
1,893988,3,2005-11-17
1,124105,4,2004-08-05
1,1248029,3,2004-04-22
1,1842128,4,2004-05-09
1,2238063,3,2005-05-11

"""

import time
import datetime


with open('file3.csv', 'w') as output:
    with open('combined_data_3.txt', 'r') as f:

        currentMovieID = 0
        for line in f:
            line = line.strip()
            if (line[len(line) - 1] == ":"):
                currentMovieID = int(line[0: len(line) - 1])
                # assert currentMovieID >= 1 and currentMovieID <= 17770
            else:
                (userID, rating, rating_date) = line.split(',')
                # assert int(userID) >= 1 and int(userID) <= 2649429
                # assert float(rating) >= 1.0 and float(rating) <= 5.0
                rating_date = int(time.mktime(datetime.datetime.strptime(rating_date, "%Y-%m-%d").timetuple()))
                output.write('%s,%s,%s,%s\n' % (currentMovieID, userID, rating, rating_date))
