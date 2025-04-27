
# Chan's Convex Hull Algorithm

This repository implements the **Chan's Algorithm** for finding the convex hull of a set of points. Chan's algorithm is a combination of **Graham's Scan** and **Gift Wrapping** algorithms, offering an efficient approach to computing the convex hull in \(O(n \log h)\) time, where \(n\) is the number of points and \(h\) is the number of points on the convex hull.

## Files in this Repository

- **a.py**: The main code implementation for Chan's Algorithm and other related functions like Graham's Scan and binary search for tangent finding.
- **test.sh**: A shell script that tests the convex hull algorithm with a set of points.
- **README.md**: This file, providing an overview of the project and usage instructions.

## Features

- **Chan's Algorithm**: Efficient convex hull computation combining Graham's scan and gift wrapping techniques.
- **Graham's Scan**: A sub-algorithm to compute the convex hull of a set of points.
- **Binary Search for Tangents**: Optimized search for tangents to the convex hull using binary search for improved performance.

## Requirements

- Python 3.x
- `matplotlib` library for plotting the convex hull and points.

You can install the required dependencies using the following:

```bash
pip install matplotlib
```

## Handling the Code

1. **Clone the Repository**:
   First, clone the repository to your local machine using Git:
   
   ```bash
   git clone https://github.com/geometric-algorithms/q1_programming.git
   ```

2. **Navigating to the Project Directory**:
   After cloning the repository, navigate to the project directory:
   
   ```bash
   cd A
   ```

3. **Running the Code**:
   To run the main convex hull algorithm, execute the following command:

   ```bash
   python3 a.py <list_of_coordinates>
   ```

   For example:

   ```bash
   python3 a.py 1.0 1.0 2.0 3.0 4.0 2.0 5.0 1.0
   ```

   This will compute the convex hull for the points `(1.0, 1.0)`, `(2.0, 3.0)`, `(4.0, 2.0)`, and `(5.0, 1.0)`.

   The script will display a plot with the points and the convex hull in **matplotlib** and print the convex hull points in clockwise order.

4. **Testing the Code**:
   You can use the `test.sh` script to test the convex hull algorithm with predefined sets of points. To run the script, execute the following command:

   ```bash
   ./test.sh
   ```

   This will run the algorithm on the points specified in the script, and you’ll see the output and plot for each test case.


## Output

The script will output the points of the convex hull in clockwise order. It will also display a plot of the points and the convex hull using `matplotlib`.
