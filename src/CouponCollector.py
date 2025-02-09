import math
import random
import pandas as pd
import matplotlib.pyplot as plt

# Constants
simulation_count = 10  # Number of simulations
max_n = 1000  # Max value of n

# Suitability functions
suitability_functions = ["LOG2N", "N", "NPOW3"]

# Suitability function implementations
def generate_suitability_1(n):
    return math.ceil(math.log2(n)) if n > 1 else 1

def generate_suitability_2(n):
    return n

def generate_suitability_3(n):
    return pow(n, 3)

# Hiring simulation
def coupon_collector(function_name, max_n):
    """Simulates the hiring process based on the suitability function."""
    max_x = 0
    if function_name == suitability_functions[0]:
        max_x = generate_suitability_1(max_n)
    elif function_name == suitability_functions[1]:
        max_x = generate_suitability_2(max_n)
    else:
        max_x = generate_suitability_3(max_n)

    max_rating = float("-inf")
    hiring_count = 0

    for _ in range(max_n):
        random_suitability = random.randrange(0, max_x)
        if random_suitability > max_rating:
            max_rating = random_suitability
            hiring_count += 1

    return hiring_count

# Simulation function
def simulate():
    """Runs the simulation for all three functions and computes the average hiring count."""
    data_1 = [[] for _ in range(simulation_count)]
    data_2 = [[] for _ in range(simulation_count)]
    data_3 = [[] for _ in range(simulation_count)]

    # Run simulations
    for j in range(simulation_count):
        print("Simulation Iteration: ", j)
        for n in range(1, max_n + 1):  # Ensure n goes from 1 to 1000
            data_1[j].append(coupon_collector(suitability_functions[0], n))
            data_2[j].append(coupon_collector(suitability_functions[1], n))
            data_3[j].append(coupon_collector(suitability_functions[2], n))

    # Compute average hiring count for each n
    avg_hiring_count_1 = [sum(data_1[j][i] for j in range(simulation_count)) / simulation_count for i in range(max_n)]
    avg_hiring_count_2 = [sum(data_2[j][i] for j in range(simulation_count)) / simulation_count for i in range(max_n)]
    avg_hiring_count_3 = [sum(data_3[j][i] for j in range(simulation_count)) / simulation_count for i in range(max_n)]

    # Create a DataFrame to store results
    df_results = pd.DataFrame({
        "n": list(range(1, max_n + 1)),
        "LOG2N": avg_hiring_count_1,
        "N": avg_hiring_count_2,
        "NPOW3": avg_hiring_count_3
    })

    print("Simulation Completed")

    return df_results

def visualize_simulation_results(df):
    """
    Generate three separate graphs for visualizing the simulation results
    corresponding to LOG2N, N, and NPOW3 functions.
    """
    plt.figure(figsize=(12, 12))

    # LOG2N Visualization
    plt.subplot(3, 1, 1)
    plt.plot(df["n"], df["LOG2N"], label="LOG2N", color="blue", linestyle='-', linewidth='1')
    plt.xlabel("Candidate Count")
    plt.ylabel("Average Hiring Count")
    plt.title("Hiring Simulation for LOG2N")
    plt.legend()
    plt.grid(True)

    # N Visualization
    plt.subplot(3, 1, 2)
    plt.plot(df["n"], df["N"], label="N", color="green", linestyle='-', linewidth='1')
    plt.xlabel("Candidate Count")
    plt.ylabel("Average Hiring Count")
    plt.title("Hiring Simulation for N")
    plt.legend()
    plt.grid(True)

    # NPOW3 Visualization
    plt.subplot(3, 1, 3)
    plt.plot(df["n"], df["NPOW3"], label="NPOW3", color="red", linestyle='-', linewidth='1')
    plt.xlabel("Candidate Count")
    plt.ylabel("Average Hiring Count")
    plt.title("Hiring Simulation for NPOW3")
    plt.legend()
    plt.grid(True)

    # plt.tight_layout()
    plt.subplots_adjust(hspace=1)
    plt.show()



# Run the simulation
df_simulation_results = simulate()
# Generate the visualizations
visualize_simulation_results(df_simulation_results)
