import sqlite3

with open('stephen_king_adaptations.txt', 'r') as f:
    stephen_king_adaptations_list = f.readlines()

conn = sqlite3.connect('stephen_king_adaptations.db')
c = conn.cursor()

c.execute('''CREATE TABLE stephen_king_adaptations_table (movieID INTEGER PRIMARY KEY AUTOINCREMENT, movieName TEXT, movieYear INTEGER, imdbRating INTEGER)''')

for line in stephen_king_adaptations_list:
    line=line.strip('\n').split(',')
    a=line[1]
    b=int(line[2])
    d=float(line[3])
    c.execute("INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)", (a, b, d))

conn.commit()
conn.close()

while True:
    print("Please select an option:")
    print("1. Movie name")
    print("2. Movie year")
    print("3. Movie rating")
    print("4. STOP")
    option = input("Enter your option: ")
    
    if option == "1":
        movie_name = input("Enter the name of the movie: ")

        conn = sqlite3.connect('stephen_king_adaptations.db')
        c = conn.cursor()
        
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
        result = c.fetchone()
        
        if result:
            print(f"Movie found! Details: ID: {result[0]}, Name: {result[1]}, Year: {result[2]}, Rating: {result[3]}")
        else:
            print("No such movie exists in our database.")
        
        conn.close()
    
    elif option == "2":
        year = input("Enter a year: ")
        
        conn = sqlite3.connect('stephen_king_adaptations.db')
        c = conn.cursor()
        
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (year,))
        results = c.fetchall()
        
        if results:
            print(f"Movies from {year}:")
            for result in results:
                print(f"ID: {result[0]}, Name: {result[1]}, Year: {result[2]}, Rating: {result[3]}")
        else:
            print(f"No movies were found for that year in our database.")

        conn.close()
    
    elif option == "3":
        rating = input("Enter a rating: ")

        conn = sqlite3.connect('stephen_king_adaptations.db')
        c = conn.cursor()
        
        c.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating>=?", (rating,))
        results = c.fetchall()

        if results:
            print(f"Movies with rating {rating} or higher:")
            for result in results:
                print(f"ID: {result[0]}, Name: {result[1]}, Year: {result[2]}, Rating: {result[3]}")
        else:
            print(f"No movies at or above that rating were found in the database.")

        conn.close()
    
    elif option == "4":
        break