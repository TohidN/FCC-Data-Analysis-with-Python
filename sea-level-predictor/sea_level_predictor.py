import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], c=np.sign(df['CSIRO Adjusted Sea Level']))


    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    xA = np.arange(df['Year'].min(),2050,1)
    yA = xA*slope + intercept
    plt.plot(xA,yA)

    # Create second line of best fit
    start = 2000
    end = 2050
    slope, intercept, r, p, se = linregress(df.loc[df["Year"] >= start]["Year"], df.loc[df["Year"] >= start]["CSIRO Adjusted Sea Level"])
    xB = np.arange(start,end,1)
    yB = xB*slope + intercept
    plt.plot(xB,yB)

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()