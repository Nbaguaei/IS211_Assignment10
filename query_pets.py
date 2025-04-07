import sqlite3

if __name__ == "__main__":
    print("Running query_pets.py")

    DB_FILE = 'pets.db'

    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        while True:
            person_id_input = input("Enter a person's ID number (-1 to exit): ")
            if person_id_input == '-1':
                break

            try:
                person_id = int(person_id_input)
            except ValueError:
                print("Invalid input. Please enter an integer ID or -1.")
                continue

            cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
            person_data = cursor.fetchone()

            if person_data:
                first_name, last_name, age = person_data
                print(f"\nData on person: {first_name} {last_name}, {age} years old")

                cursor.execute("SELECT pet_id FROM person_pet WHERE person_id = ?", (person_id,))
                pet_ids = cursor.fetchall()

                if pet_ids:
                    print(f"{first_name} {last_name} owned:")
                    for pet_id_tuple in pet_ids:
                        pet_id = pet_id_tuple[0]
                        cursor.execute("SELECT name, breed, age FROM pet WHERE id = ?", (pet_id,))
                        pet_data = cursor.fetchone()
                        if pet_data:
                            pet_name, pet_breed, pet_age = pet_data
                            print(f"- {pet_name}, a {pet_breed}, that was {pet_age} years old")
                else:
                    print(f"{first_name} {last_name} does not own any pets in our records.")
            else:
                print(f"Error: Person with ID {person_id} not found.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()