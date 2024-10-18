import random
def f(x):
    return x**2 - 4*x + 4
def hill_climbing(starting_point, max_iterations, step_size=0.1):
    current = starting_point
    for _ in range(max_iterations):
        neighbor = current + random.uniform(-step_size, step_size)
        neighbor = max(0, min(4, neighbor))
        if f(neighbor) < f(current):
            current = neighbor
    return current
starting_point = random.uniform(0, 4)
max_iterations = 100
best_x = hill_climbing(starting_point, max_iterations)
print(f"Best x: {best_x}, Best f(x): {f(best_x)}")
