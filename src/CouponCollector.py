import math
import random
import pandas as pd
import statistics as st

simulation_count = 10
max_n = 1000

suitability_functions = ["LOG2N","N","NPOW3"]

def generate_suitability_1(n):
    return math.ceil(math.log2(n))

def generate_suitability_2(n):
    return n

def generate_suitability_3(n):
    return pow(n,3)

def coupon_collector(function_name, max_n):
    max_x = 0
    if function_name == suitability_functions[0]:
        # generate_suitability_1
        max_x = generate_suitability_1(max_n)
    elif function_name == suitability_functions[1]:
        # generate_suitability_2
        max_x = generate_suitability_2(max_n)
    else:
        #generate_suitability_3
        max_x = generate_suitability_3(max_n)
    

    max_rating = float("-inf")
    hiring_count = 0
    generated_suitabilities = []
    compounding_mean = []
    compounding_std = []
    for i in range(0,max_n):
        random_suitability = random.randrange(0,max_x)
        generated_suitabilities.append(random_suitability)
        if i<=2:
            compounding_mean.append(0)
            compounding_std.append(0)
        else:
            compounding_mean.append(st.mean(generated_suitabilities[:i]))
            compounding_std.append(st.stdev(generated_suitabilities[:i]))

        if random_suitability > max_rating:
            hiring_count += 1
            max_rating = random_suitability


    aggregates = {
        "random_sequence": generated_suitabilities,
        "compounded_mean": compounding_mean,
        "compounded_std": compounding_std
    }

    return hiring_count, aggregates


def simulate():
    suitability_1,suitability_2,suitability_3 = [],[],[]
    aggregate_1,aggregate_2,aggregate_3 = [],[],[]
    for i in range(simulation_count):
        hiring_count_1, agg_1 = coupon_collector(suitability_functions[0],max_n)
        hiring_count_2, agg_2 = coupon_collector(suitability_functions[1],max_n)
        hiring_count_3, agg_3 = coupon_collector(suitability_functions[2],max_n)
    
        suitability_1.append(hiring_count_1)
        suitability_2.append(hiring_count_2)
        suitability_3.append(hiring_count_3)

        aggregate_1.append(agg_1)
        aggregate_2.append(agg_2)
        aggregate_3.append(agg_3)

    data_1 = {
        "Function 1": suitability_1,
        "Function 2": suitability_2,
        "Function 3": suitability_3
    }

    for i in range(simulation_count):
        sim_results_func_1,sim_results_func_2,sim_results_func_3 = aggregate_1[i],aggregate_2[i],aggregate_3[i]

        df_sim1 = pd.DataFrame.from_dict(sim_results_func_1)
        df_sim2 = pd.DataFrame.from_dict(sim_results_func_2)
        df_sim3 = pd.DataFrame.from_dict(sim_results_func_3)

        df_sim1.to_csv(path_or_buf=f"../exports/sim_0{i}_func_1.csv", index=None)
        df_sim2.to_csv(path_or_buf=f"../exports/sim_0{i}_func_2.csv", index=None)
        df_sim3.to_csv(path_or_buf=f"../exports/sim_0{i}_func_3.csv", index=None)


    df1 = pd.DataFrame.from_dict(data_1)

    df1.to_csv(path_or_buf='../exports/hiring_count.csv', index=None)


if __name__=="__main__":
    simulate()