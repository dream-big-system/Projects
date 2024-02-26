import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Function to generate the bifurcation diagram
def bifurcation_diagram():
    r_values = []
    x_values = []

    # Iterate over different r values
    for r in [i / 1000.0 for i in range(2000, 4000)]:
        x = 0.5  # Initial value of x

        # Discard initial transient iterations
        for _ in range(100):
            x = logistic_map(r, x)

        # Collect data points after transient
        for _ in range(200):
            x = logistic_map(r, x)
            r_values.append(r)
            x_values.append(x)

    # Plot the bifurcation diagram
    plt.figure(figsize=(10, 6))
    plt.plot(r_values, x_values, ls='', marker=',', color='b')
    plt.title('Bifurcation Diagram of Logistic Map')
    plt.xlabel('r')
    plt.ylabel('x')
    plt.show()

# Generate and display the bifurcation diagram
bifurcation_diagram()
