import numpy as np
import pandas as pd


def main():
    print("Hello, World!")
    print("This is a scratch file for testing and experimenting with code.")
    print("You can modify this file as needed.")

    # Example: Create a simple DataFrame
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"],
    }
    df = pd.DataFrame(data)
    print("\nSample DataFrame:")
    print(df)

    # Example: Perform a simple calculation using NumPy
    numbers = np.array([1, 2, 3, 4, 5])
    squared_numbers = np.square(numbers)
    print("\nSquared Numbers:")
    print(squared_numbers)

if __name__ == "__main__":
    main()
