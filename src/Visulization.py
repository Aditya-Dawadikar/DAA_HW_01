import statistics as st
import pandas as pd
import matplotlib.pyplot as plt

def visualize(df):
    func_1_avg, func_2_avg, func_3_avg = st.mean(df["Function 1"]),st.mean(df["Function 2"]),st.mean(df["Function 3"])
    func_1_std, func_2_std, func_3_std = st.stdev(df["Function 1"]),st.stdev(df["Function 2"]),st.stdev(df["Function 3"])
    print(func_1_avg,func_2_avg, func_3_avg)
    print(round(func_1_std,4),round(func_2_std,4), round(func_3_std,4))

def load_data():
    df = pd.read_csv("../exports/Simulation_01.csv")
    return df

if __name__=="__main__":
    df = load_data()
    visualize(df)