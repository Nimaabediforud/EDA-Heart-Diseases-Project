import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



""" 
Classify cardiovascular patients and non-patient individuals
bsade on chest pain type,
SECTION THIRD
"""

# Load the Dataframe
df = pd.read_csv("../data/heart-data.csv")

"""
Customize some properties of visualizations
"""
title = {"fontname": "Comic Sans MS", "fontsize": 16, "fontweight": "bold"}
label = {"fontname": "Comic Sans MS", "fontsize": 12, "fontweight": "bold"}

# Adjust the position of x ticks and determine their labels
xticks_labels = ["ASY","NAP", "ATA", "TA"]
xticks = np.arange(len(xticks_labels))

# Calculate the number of patients in each chest pain type and sort by 'xticks_labels'
patients = df[(df["HeartDisease"]==1)]["ChestPainType"].value_counts().reindex(xticks_labels)
patient_counts = list(patients)


# Calculate the number of non-patients in each chest pain type and sort by 'xticks_labels'
non_patients = df[(df["HeartDisease"]==0)]["ChestPainType"].value_counts().reindex(xticks_labels)
non_patient_counts = list(non_patients)


"""
Create the visualizations, 
SECTION THIRD
"""


def stacked_bar(ax, xticks, xticks_labels, patient_counts, non_patient_counts):
    # Adjust satacked bars
    ax.bar(xticks, non_patient_counts, width=0.4, label="Non-Patients", edgecolor="black", color="skyblue")
    ax.bar(xticks, patient_counts, width=0.4, bottom=non_patient_counts, label="Patients",edgecolor="black", color="lightcoral")

    # Customize the plot and figure
    ax.set_title("Distribution of Patients & Non-Patients in Each Chest Pain Type", fontdict=title)
    ax.set_xlabel("Chest Pain Types", fontdict=label)
    ax.set_ylabel("Population", fontdict=label)
    ax.grid(axis="y")

    # Set x ticks and their labels
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks_labels)

    for l in ax.get_xticklabels():
        l.set_fontname("Times New Roman")
        l.set_fontweight("bold")

    # Set y ticks and their labels
    ax.set_yticks(np.arange(0, 650, 100))
    ax.set_yticklabels(np.arange(0, 650, 100))

    for l in ax.get_yticklabels():
        l.set_fontname("Times New Roman")
        l.set_fontweight("bold")

    # Customize and add annotations to (patients) segment to indicate the population of this segment
    for i, v in enumerate(patient_counts):
        ax.annotate(v, xy=(xticks[i], np.add(non_patient_counts[i], patient_counts[i])), xytext=(0, 0), textcoords="offset points",
                    ha="center", va="bottom", fontname="Times New Roman", fontweight="bold",
                    bbox=dict(facecolor="white", edgecolor="lightcoral", boxstyle="round,pad=0.1"))
        

    # Customize and add annotations to (non-patients) segment to indicate the population of this segment
    for i, v in enumerate(non_patient_counts):
        ax.annotate(v, xy=(xticks[i], non_patient_counts[i]), xytext=(0, 0), textcoords="offset points",
                    ha="center", va="top", fontname="Times New Roman", fontweight="bold",
                    bbox=dict(facecolor="white", edgecolor="skyblue", boxstyle="round,pad=0.1"))
        

    # Customize and add annotations to the stacked bars to indicate (the total population) of the segments
    for i, _ in enumerate(patient_counts):
        total_text =f"{5*' '}Total: {np.add(non_patient_counts[i], patient_counts[i])}{5*' '}"

        ax.annotate(total_text, xy=(xticks[i], np.add(non_patient_counts[i], patient_counts[i])),
                    xytext=(0, 30), textcoords="offset points",
                    ha="center", va="top", fontname="Times New Roman", fontweight="bold",
                    bbox=dict(facecolor="whitesmoke", edgecolor="black", boxstyle="round,pad=0.3")
                    )
        
    # Adjust the legend box
    legend = ax.legend(edgecolor="gray")
    for text in legend.get_texts():
        text.set_fontname("Times New Roman")
        text.set_fontsize(12)



fig, axs= plt.subplots(2, 1, figsize=[10, 10])
stacked_bar(axs[0], xticks, xticks_labels, patient_counts, non_patient_counts)
plt.tight_layout()
plt.show()

print(xticks_labels,"\n", xticks,"\n",
      "\n",patients,"\n",non_patients,"\n")

