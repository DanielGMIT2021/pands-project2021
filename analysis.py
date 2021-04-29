# Code for pands-project2021
# Author: Daniel Gonzalez

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


### --- Description:

dataset = pd.read_csv("iris.data.csv", header=None, names=["sepal length", "sepal width", "petal lenght", "petal width", "variety"])
# Reads data from file

print(dataset.head(1))
#prints 1 instance as a sample

variable_summary = dataset.groupby("variety").describe()
# Describes all variables grouped by variety of flower

variable_summary.to_csv("summary.txt")
#saves the summary as a text file

variable_summary.to_csv("summary_table.txt")
# Copy of the file as a readable table


# Accessing data grouped by each variety
setosa = dataset[dataset["variety"] =="Iris-setosa"]
versicolor = dataset[dataset["variety"] =="Iris-versicolor"]
virginica = dataset[dataset["variety"] =="Iris-virginica"]


#Printing description of each variety
print("Iris setosa:")
print(setosa.describe())

print("Iris versicolor:")
print(versicolor.describe())

print("Iris virginica:")
print(virginica.describe())


### --- Visualisation:

## HISTOGRAMS:

def histograms(attribute):
    # Takes in an flower attribute
    # Displays a histogram with all variety of flower

    sns.distplot(setosa[attribute], label = "Iris setosa")
    sns.distplot(virginica[attribute], label = "Iris virginica")
    sns.distplot(versicolor[attribute],label = "Iris versicolor")
    plt.title(attribute)
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig(attribute + ".png")
    plt.show()


def scatterplot(attribute1, attribute2):
    # Takes two attributes
    # Displays a scatterplot of those attributes
    # For all varieties
    sns.scatterplot(data = dataset, x = attribute1, y = attribute2, hue="variety", marker = "o")
    plt.title(attribute1 + "-" + attribute2)
    plt.xlabel(attribute1)
    plt.ylabel(attribute2)
    plt.legend()
    plt.savefig(attribute1 +"-"+ attribute2 + ".png")
    plt.show()

histograms("petal width")
histograms("sepal length")
histograms("sepal width")
histograms("petal lenght")

scatterplot("petal width", "petal lenght")
scatterplot("sepal width", "sepal length")
