# Coupon Collector Simulation

This project contains a simulation script `CouponCollector.py` for running hiring simulations based on different suitability functions. The results are saved in a CSV file (`simulation_results.csv`).

---

## Folder Structure

```
src/
├── CouponCollector.py    # Main Python script
README.md                 # Project documentation
requirements.txt          # Python dependencies
```

---

## Requirements

This project requires the following:
- Python 3.7 or higher
- Python libraries:
  - `pandas`
  - `matplotlib`

---

## How to Run

1. **Install Python Dependencies:**
   Make sure you have Python installed and run the following command to install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script:**
   Navigate to the `src/` directory and execute the script:
   ```bash
   cd src
   python CouponCollector.py
   ```

3. **Check the Results:**
   Once the script completes, the simulation results will be saved as `simulation_results.csv` in the `src/` directory.

---

## Sample Output

1. Terminal Output: When simulation is executed for 10 iterations
![terminal output](https://github.com/Aditya-Dawadikar/DAA_HW_01/blob/master/src/views/terminal_output.png)
3. Matplotlib Visualization Output for 3 different suitability functions
![visualization](https://github.com/Aditya-Dawadikar/DAA_HW_01/blob/master/src/views/visualization.png)
