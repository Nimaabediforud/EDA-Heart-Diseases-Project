import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


""" 
Classify cardiovascular patients
based on Age,
SECTION TWO
"""

# Load the Dataframe
df = pd.read_csv("data/heart-data.csv")

# Get and Calculate needed values
card_patients = df[df["HeartDisease"]==1]["Age"]
min_age = card_patients.min()
max_age = card_patients.max()
mean_age = card_patients.mean()


"""
Customize some properties of visualizations
"""
title = {"fontname": "Comic Sans MS", "fontsize": 16, "fontweight": "bold"}
label = {"fontname": "Comic Sans MS", "fontsize": 12, "fontweight": "bold"}
annotations ={"fontname": "Times New Roman", "bbox":{"facecolor": "white", "edgecolor": "black", "boxstyle": "round,pad=0.3"}}

"""
Create the visualizations, 
SECTION TWO
"""

def histogram(title, label, annotations):
    n, bins, patches = plt.hist(card_patients, range=(min_age, max_age),bins=20, color="firebrick", edgecolor="black")

    # Adjust the figure customization
    plt.title("Distribution of Patients' Age", fontdict=title)
    plt.xlabel("Patients' Age", fontdict=label)
    plt.ylabel("Number of Patients", fontdict=label)
    plt.ylim(top=max(n) + 10)
    plt.grid(axis="y")
    plt.tight_layout()

    # Add vertical line to indicate the mean age of patients
    plt.axvline(mean_age, linestyle="--", c="black", linewidth=2, label=f"Mean Age of Patients = {mean_age:.1f}")

    # Customize and set x and y ticks
    _, xlabels = plt.xticks(np.arange(min_age, max_age + 1, np.divide(np.subtract(max_age, min_age), 20)))
    _, ylabels = plt.yticks()

    for xl in xlabels:
        xl.set_fontname("Times New Roman")
        xl.set_fontweight("bold")

    for yl in  ylabels:
        yl.set_fontname("Times New Roman")
        yl.set_fontweight("bold")

    # Adjust and Add annotations 
    for count, left_bin, right_bin in zip(n, bins[:-1], bins[1:]):
        center_bin = np.divide(np.add(left_bin, right_bin), 2)
        plt.text(center_bin, count + 1, int(count), ha="center",
                fontdict=annotations)
        
    # Adjust the legend box
    custom_line = Line2D([0], [0], linestyle="--", c="black", linewidth=3 ,label=f"Mean Age of Patients = {mean_age:.1f}")
    [t.set_fontname("Times New Roman") for t in plt.legend(handles=[custom_line], handlelength=3, edgecolor="gray").get_texts()]

    # Adjust and add the 'Total number of patients' text box
    plt.text(69, 73, f"Total Number of Patients = {card_patients.count()}",
            fontname="Times New Roman", fontsize=10, bbox=dict(facecolor="white", edgecolor="gray", boxstyle="round,pad=0.3"))


def age_df():
    # Make the dataframe
    age_data = {"minimum age of patients": min_age, "maximum age of patients": max_age,
                "mean age of patients": mean_age}
    age_df = pd.DataFrame(age_data, index=[''])
    #age_df.to_csv(...)
    return age_df

# Set histogram, Show distribution of patients' age
plt.figure(figsize=[10, 5])
histogram(title, label, annotations)
#plt.savefig(...)
plt.show()

