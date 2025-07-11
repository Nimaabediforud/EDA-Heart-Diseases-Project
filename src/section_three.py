import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec




""" 
Classify cardiovascular patients and non-patient 
bsade on chest pain type,
SECTION THREE
"""

# Load the Dataframe
df = pd.read_csv("data/heart-data.csv")

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
SECTION THREE
"""


def stacked_bar(ax, xticks, xticks_labels, patient_counts, non_patient_counts):
    # Adjust satacked bars
    ax.bar(xticks, non_patient_counts, width=0.4, label="Non-Patients", edgecolor="black", color="skyblue")
    ax.bar(xticks, patient_counts, width=0.4, bottom=non_patient_counts, label="Patients",edgecolor="black", color="lightcoral")

    # Customize the plot and figure
    ax.set_title("Distribution of Chest Pain Types in Patients and Non-Patients", fontdict=title)
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



def donutChart1(axs2, patients_counts,xticks_labels, label):
    # Set colors and donut chart
    colors = plt.get_cmap("Set3")(np.arange(len(xticks_labels)))
    patch1, text1, autotext1 = axs2.pie(patients_counts, labels=xticks_labels, colors=colors,
                           autopct="%1.1f%%", pctdistance=0.75, wedgeprops=dict(width=0.5))
    # Add edgecolor
    for p1 in patch1:
        p1.set_edgecolor("black")

    # Adjust labels font and style 
    for t1 in text1:
        t1.set_fontname("Comic Sans MS")
        t1.set_fontweight("bold")

    for a1 in autotext1:
        a1.set_fontname("Times New Roman")
        a1.set_fontweight("bold")
    
    # Add text in the center of donut chart
    axs2.text(0, 0, "Patients", fontdict=label, ha="center", va="center")


def donutChart2(axs3, non_patient_counts,xticks_labels, label):
    # Set colors and donut chart
    colors = plt.get_cmap("Set3")(np.arange(len(xticks_labels)))
    patch2, text2, autotext2 = axs3.pie(non_patient_counts, labels=xticks_labels, colors=colors,
                           autopct="%1.1f%%", pctdistance=0.75, wedgeprops=dict(width=0.5))
    
    # Add edgecolor
    for p2 in patch2:
        p2.set_edgecolor("black")

    # Adjust labels font and style 
    for t2 in text2:
        t2.set_fontname("Comic Sans MS")
        t2.set_fontweight("bold")
    
    for a2 in autotext2:
        a2.set_fontname("Times New Roman")
        a2.set_fontweight("bold")
    
    # Add text in the center of donut chart
    axs3.text(0, 0, "Non-Patients", fontdict=label, ha="center", va="center")


def chest_p_t_df(patients, non_patients):
    # Make the dataframe
    patients_ = patients.reset_index(name="counts")
    non_patients_ = non_patients.reset_index(name="counts")
    chest_p_t_df = pd.merge(patients_, non_patients_, on="ChestPainType", suffixes=[" of Patients", " of Non-Patients"])
    #chest_p_t_df.to_csv(...)
    print(chest_p_t_df)




# Make the figure and subplots
fig = plt.figure(figsize=(12, 12)) 
gs = GridSpec(nrows=2, ncols=2, figure=fig, hspace=0.4)
axs1 = fig.add_subplot(gs[0, :])
axs2 = fig.add_subplot(gs[1, 0])
axs3 = fig.add_subplot(gs[1, 1])

# Adjust and add the super title for pie charts
sup_title = plt.suptitle(x=0.5, y=0.45, t="Distribution of Chest Pain Types in Patients and Non-Patients (%)",
                         fontname="Comic Sans MS", fontsize=16, fontweight="bold")

# Run and Show 
stacked_bar(axs1, xticks, xticks_labels, patient_counts, non_patient_counts)
donutChart1(axs2, patient_counts, xticks_labels, label)
donutChart2(axs3, non_patient_counts, xticks_labels, label)
#plt.savefig(...)
plt.show()

chest_p_t_df(patients, non_patients)

