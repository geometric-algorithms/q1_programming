
# Chan's Convex Hull Algorithm

This repository implements the **Chan's Algorithm** for finding the convex hull of a set of points. Chan's algorithm is a combination of **Graham's Scan** and **Gift Wrapping** algorithms, offering an efficient approach to computing the convex hull in \(O(n \log h)\) time, where \(n\) is the number of points and \(h\) is the number of points on the convex hull.

## Files in this Repository

- **convex_hull.py**: The main code implementation for Chan's Algorithm and other related functions like Graham's Scan and binary search for tangent finding.
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
   git clone https://github.com/yourusername/repository-name.git
   ```

2. **Navigating to the Project Directory**:
   After cloning the repository, navigate to the project directory:
   
   ```bash
   cd repository-name
   ```

3. **Running the Code**:
   To run the main convex hull algorithm, execute the following command:

   ```bash
   python convex_hull.py <list_of_coordinates>
   ```

   For example:

   ```bash
   python convex_hull.py 1.0 1.0 2.0 3.0 4.0 2.0 5.0 1.0
   ```

   This will compute the convex hull for the points `(1.0, 1.0)`, `(2.0, 3.0)`, `(4.0, 2.0)`, and `(5.0, 1.0)`.

   The script will display a plot with the points and the convex hull in **matplotlib** and print the convex hull points in clockwise order.

4. **Testing the Code**:
   You can use the `test.sh` script to test the convex hull algorithm with predefined sets of points. To run the script, execute the following command:

   ```bash
   bash test.sh or "./test.sh"
   ```

   This will run the algorithm on the points specified in the script, and you’ll see the output and plot for each test case.

5. **Modifying and Extending the Code**:
   You can modify the code to handle different input formats or improve the functionality. Make sure to follow these steps if you make changes:

   - **Testing**: After making modifications, test the code to ensure it still works as expected.
   - **Adding New Features**: Feel free to add new features or optimize the algorithm. Be sure to document your changes clearly in the code.
   - **Committing Changes**: After making your changes, commit them to your local repository and push them to GitHub using the following commands:

     ```bash
     git add .
     git commit -m "Your commit message"
     git push origin main
     ```

## Output

The script will output the points of the convex hull in clockwise order. It will also display a plot of the points and the convex hull using `matplotlib`.
