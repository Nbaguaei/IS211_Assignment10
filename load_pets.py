import sqlite3

if __name__ == "__main__":
    print("Running load_pets.py")

    DB_FILE = 'pets.db'

    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        people_data = [
            (1, 'James', 'Smith', 41),
            (2, 'Diana', 'Greene', 23),
            (3, 'Sara', 'White', 27),
            (4, 'William', 'Gibson', 23)
        ]
        cursor.executemany("INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)", people_data)

        pet_data = [
            (1, 'Rusty', 'Dalmation', 4, 1),
            (2, 'Bella', 'Alaskan Malamute', 3, 0),
            (3, 'Max', 'Cocker Spaniel', 1, 0),
            (4, 'Rocky', 'Beagle', 7, 0),
            (5, 'Rufus', 'Cocker Spaniel', 1, 0),
            (6, 'Spot', 'Bloodhound', 2, 1)
        ]
        cursor.executemany("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", pet_data)

        person_pet_data = [
            (1, 1),
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 5),
            (4, 6)
        ]
        cursor.executemany("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", person_pet_data)

        conn.commit()
        print("Data loaded successfully into pets.db")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

    print("\nPurpose of the person_pet table:")
    print("The person_pet table serves as a linking table to establish a many-to-many relationship between the person and pet tables.")
    print("Each row connects a person's ID to a pet's ID, indicating ownership.")