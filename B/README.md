# Dynamic Convex Hull using Segment Tree

This repository implements a **Dynamic Convex Hull** using a **segment tree** in Python. Points can be inserted or deleted on-the-fly, the convex hull is maintained efficiently, and you can query whether a point lies on the hull. An interactive menu and Matplotlib plotting make it easy to experiment.

---

## Files in this Repository

- **convex_hull.py**  
  Main Python script implementing the dynamic convex hull data structure:
  - `insert(point)`  
  - `delete(point)`  
  - `point_on_hull(point)`  
  - `plot_and_print_hull()`  
  - Command-line interactive menu

- **test.sh**  
  Bash script to run `convex_hull.py` on a predefined set of points.

- **README.md**  
  This file: project overview, installation, usage, development guidelines.

---

## Features

- **Dynamic Updates**: Insert/delete points in amortized \(O(\log^2 n)\) time.  
- **Segment Tree**: Maintains local hulls per x-interval for efficient merging.  
- **Point-on-Hull Query**: Check if a point lies on the current hull boundary.  
- **Interactive Menu**: Perform operations without restarting the script.  
- **Visualization**: Plot points and hull using Matplotlib.

---

## Requirements

- Python 3.x  
- Matplotlib  

Install dependencies:

```bash
pip install matplotlib


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
