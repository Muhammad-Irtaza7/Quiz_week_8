import matplotlib.pyplot as plt
import sqlite3
def fetch_data():
    try:
        connection = sqlite3.connect('climate.db')  # Update with your database connection details
        cursor = connection.cursor()

        years = []
        co2 = []
        temp = []

        cursor.execute("SELECT year, co2, temperature FROM ClimateData")

        rows = cursor.fetchall()

        for row in rows:
            year, co2_val, temp_val = row
            years.append(year)
            co2.append(co2_val)
            temp.append(temp_val)
        connection.close()

        return years, co2, temp

    except Exception as e:
        print(f"Error: {e}")
        return [], [], []

if __name__ == "__main__":
    years, co2, temp = fetch_data()

    plt.subplot(2, 1, 1)
    plt.plot(years, co2, 'b--')
    plt.title("Climate Data")
    plt.ylabel("[CO2]")
    plt.xlabel("Year (decade)")

    plt.subplot(2, 1, 2)
    plt.plot(years, temp, 'r*-')
    plt.ylabel("Temp (C)")
    plt.xlabel("Year (decade)")
    plt.show()
    plt.savefig("co2_temp_1.png")
