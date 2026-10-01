# expermient 1
n_values = [10, 100, 1000, 10000, 100000]
import numpy as np
import matplotlib.pyplot as plt
xpoints = []
ypoints = []

for n in n_values:
    tosses = np.random.randint(0, 2, n)
    probability_of_head = tosses.mean()

    xpoints.append(n)
    ypoints.append(probability_of_head)

plt.plot(xpoints, ypoints, marker="o")
plt.xlabel("Total number of coin tosses")
plt.ylabel("Probability of getting a head")
plt.title("Convergence of the empirical probability of heads")
plt.axhline(y=0.5, label="Theoretical probability")
plt.xscale("log")
plt.legend()
plt.show()

# expriment 2
# for a fixed sample size n,how much does the estimate pn vary between independent experiments?
# work out for a simulation of n=1000 first.

ypoints = []
tosses=np.random.randint(0,2,size=(1000,1000))
ypoints = tosses.mean(axis=1)
experiment_number = list(range(1, 1001))
plt.plot(experiment_number, ypoints)
plt.axhline(y=0.5)
plt.xlabel("Experiment number")
plt.ylabel("Estimated probability of heads")
plt.title("Estimated probability across independent experiments")
plt.show()
plt.axvline(x=0.5)
plt.hist(ypoints,bins=10,edgecolor='black')
plt.xlabel('vaule range')
plt.ylabel('Frequency')
plt.title('Histogram with 10 Bins')
plt.show()
mean_probability = np.mean(ypoints)

print("Simulated mean:", mean_probability)

variance_probability = np.var(ypoints)

print("Simulated variance:", variance_probability)
mean_probability = np.mean(ypoints)
variance_probability = np.var(ypoints)

print("Simulated mean:", mean_probability)
print("Theoretical mean:", 0.5)

print("Simulated variance:", variance_probability)
print("Theoretical variance:", 0.00025)

# experiment 3
n_values = [10, 100, 1000, 10000, 100000]
xpoints = []
ypoints = []

for n in n_values:
    tosses = np.random.randint(0, 2, n)
    probability_of_head = tosses.mean()

    xpoints.append(n)
    ypoints.append(probability_of_head)

plt.plot(xpoints, ypoints, marker="o")
plt.xlabel("Total number of coin tosses")
plt.ylabel("Probability of getting a head")
plt.title("Convergence of the empirical probability of heads")
plt.axhline(y=0.5, label="Theoretical probability")
plt.xscale("log")
plt.legend()
plt.show()

# First year project of coin toss simulation and investigation.
# Experiment 4 - Central Limit Theorem

n_values = [10, 100, 1000, 10000]
number_of_experiments = 1000
theoretical_mean = 0.5

for n in n_values:
    # 1. TODO: Generate the entire 2D matrix of shape (1000, n) instantly
    matrix = np.random.randint(0, 2, size=(1000,n))
    
    # 2. TODO: Calculate the mean across columns (axis=1) to eliminate the inner loop
    probability_of_head_list = matrix.mean(axis=1)
    
    # 3. Calculate statistics instantly
    theoretical_standard_deviation = np.sqrt(0.25 / n)
    simulated_mean = probability_of_head_list.mean()
    simulated_standard_deviation = probability_of_head_list.std()
    
    print(f"n = {n:<5} | Sim Mean: {simulated_mean:.4f} | Sim SD: {simulated_standard_deviation:.5f} (Theo SD: {theoretical_standard_deviation:.5f})")
    
    # 4. Standardise and plot
    standardised_values = (probability_of_head_list - theoretical_mean) / theoretical_standard_deviation
    
    plt.hist(standardised_values, bins=30, density=True, edgecolor="black", alpha=0.6)
    plt.axvline(x=0, color="red", linestyle="--", label="Theoretical Mean = 0")
    
    
    x = np.linspace(-4, 4, 100)
    normal_curve = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
    plt.plot(x, normal_curve, color="black", label="Standard Normal Curve")
    
    plt.xlabel("Standardised $\hat{p}$")
    plt.ylabel("Density")
    plt.title(f"Central Limit Theorem: n = {n}")
    plt.legend()
    plt.show()

