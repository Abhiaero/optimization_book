import numpy as np
import os

# ==========================================
# 1. EXPERIMENTAL SETUP & BENCHMARK FUNCTIONS
# ==========================================
DIM = 30
RUNS = 2
POP_SIZE = 50
MAX_FES = DIM * 10000
MAX_ITER = MAX_FES // POP_SIZE
NUM_RECORD_POINTS = 100
RECORD_INTERVAL = MAX_ITER // NUM_RECORD_POINTS

# Create results directory if it doesn't exist
os.makedirs("results", exist_ok=True)


def F1_Sphere(x): return np.sum(x ** 2, axis=-1)


def F2_Rosenbrock(x): return np.sum(100.0 * (x[..., 1:] - x[..., :-1] ** 2) ** 2 + (1 - x[..., :-1]) ** 2, axis=-1)


def F3_Rastrigin(x): return np.sum(x ** 2 - 10 * np.cos(2 * np.pi * x) + 10, axis=-1)


def F4_Ackley(x):
    n = x.shape[-1]
    sum_sq = np.sum(x ** 2, axis=-1)
    sum_cos = np.sum(np.cos(2 * np.pi * x), axis=-1)
    return -20 * np.exp(-0.2 * np.sqrt(sum_sq / n)) - np.exp(sum_cos / n) + 20 + np.e


def F5_Griewank(x):
    i = np.arange(1, x.shape[-1] + 1)
    return np.sum(x ** 2) / 4000 - np.prod(np.cos(x / np.sqrt(i)), axis=-1) + 1


def F6_Camel(x):  # 2D only
    x1, x2 = x[..., 0], x[..., 1]
    return (4 - 2.1 * x1 ** 2 + (x1 ** 4) / 3) * x1 ** 2 + x1 * x2 + (-4 + 4 * x2 ** 2) * x2 ** 2


FUNCTIONS = {
    "F1": (F1_Sphere, [-100, 100], DIM),
    "F2": (F2_Rosenbrock, [-30, 30], DIM),
    "F3": (F3_Rastrigin, [-5.12, 5.12], DIM),
    "F4": (F4_Ackley, [-32, 32], DIM),
    "F5": (F5_Griewank, [-600, 600], DIM),
    "F6": (F6_Camel, [-5, 5], 2)  # Camel is historically 2D
}


# ==========================================
# 2. ALGORITHM IMPLEMENTATIONS
# ==========================================
def init_population(pop_size, dim, bounds):
    return np.random.uniform(bounds[0], bounds[1], (pop_size, dim))


def run_PSO(func, bounds, dim):
    X = init_population(POP_SIZE, dim, bounds)
    V = np.zeros_like(X)
    P_best = np.copy(X)
    P_best_fit = func(P_best)
    G_best = P_best[np.argmin(P_best_fit)]
    G_best_fit = np.min(P_best_fit)

    w, c1, c2 = 0.729, 1.49445, 1.49445  # Standard Clerc-Kennedy parameters
    history = []

    for it in range(MAX_ITER):
        r1, r2 = np.random.rand(POP_SIZE, dim), np.random.rand(POP_SIZE, dim)
        V = w * V + c1 * r1 * (P_best - X) + c2 * r2 * (G_best - X)
        X = np.clip(X + V, bounds[0], bounds[1])

        fit = func(X)
        improve = fit < P_best_fit
        P_best[improve] = X[improve]
        P_best_fit[improve] = fit[improve]

        if np.min(P_best_fit) < G_best_fit:
            G_best_fit = np.min(P_best_fit)
            G_best = P_best[np.argmin(P_best_fit)]

        if it % RECORD_INTERVAL == 0 and len(history) < NUM_RECORD_POINTS:
            history.append(G_best_fit)

    return history


def run_DE(func, bounds, dim, F=0.5, CR=0.9):
    X = init_population(POP_SIZE, dim, bounds)
    fitness = func(X)
    best_fit = np.min(fitness)
    history = []

    for it in range(MAX_ITER):
        # rand/1/bin strategy
        idxs = [np.random.permutation(POP_SIZE) for _ in range(3)]
        V = X[idxs[0]] + F * (X[idxs[1]] - X[idxs[2]])
        V = np.clip(V, bounds[0], bounds[1])

        cross_points = np.random.rand(POP_SIZE, dim) < CR
        U = np.where(cross_points, V, X)

        U_fit = func(U)
        improve = U_fit < fitness
        X[improve] = U[improve]
        fitness[improve] = U_fit[improve]

        best_fit = min(best_fit, np.min(fitness))
        if it % RECORD_INTERVAL == 0 and len(history) < NUM_RECORD_POINTS:
            history.append(best_fit)

    return history


def run_GA(func, bounds, dim, mutation_rate=0.1):
    X = init_population(POP_SIZE, dim, bounds)
    fitness = func(X)
    best_fit = np.min(fitness)
    history = []

    for it in range(MAX_ITER):
        # Tournament Selection
        tourney = np.random.randint(0, POP_SIZE, (POP_SIZE, 2))
        winners = np.argmin(np.array([fitness[tourney[:, 0]], fitness[tourney[:, 1]]]), axis=0)

        # CORRECTED LINE: Rows first, then winning column
        parents = X[tourney[np.arange(POP_SIZE), winners]]

        # Arithmetic Crossover
        alpha = np.random.rand(POP_SIZE // 2, dim)
        P1, P2 = parents[0::2], parents[1::2]
        C1 = alpha * P1 + (1 - alpha) * P2
        C2 = alpha * P2 + (1 - alpha) * P1
        X_new = np.vstack((C1, C2))

        # Gaussian Mutation
        mut_mask = np.random.rand(POP_SIZE, dim) < mutation_rate
        X_new += mut_mask * np.random.normal(0, 0.1 * (bounds[1] - bounds[0]), (POP_SIZE, dim))
        X = np.clip(X_new, bounds[0], bounds[1])

        fitness = func(X)

        # Update best fitness
        current_best = np.min(fitness)
        if current_best < best_fit:
            best_fit = current_best

        if it % RECORD_INTERVAL == 0 and len(history) < NUM_RECORD_POINTS:
            history.append(best_fit)

    # Make sure we return exactly NUM_RECORD_POINTS even if loop ends early/late
    while len(history) < NUM_RECORD_POINTS:
        history.append(best_fit)

    return history

def run_ABC(func, bounds, dim, limit=100):
    X = init_population(POP_SIZE, dim, bounds)
    fitness = func(X)
    trials = np.zeros(POP_SIZE)
    best_fit = np.min(fitness)
    history = []

    for it in range(MAX_ITER):
        # Employed Bees
        for i in range(POP_SIZE):
            k = np.random.choice([j for j in range(POP_SIZE) if j != i])
            phi = np.random.uniform(-1, 1, dim)
            V = np.clip(X[i] + phi * (X[i] - X[k]), bounds[0], bounds[1])
            v_fit = func(V)
            if v_fit < fitness[i]:
                X[i], fitness[i], trials[i] = V, v_fit, 0
            else:
                trials[i] += 1

        # Onlooker Bees (Roulette Wheel based on inverse fitness)
        fit_probs = 1.0 / (1.0 + fitness - np.min(fitness))
        fit_probs /= np.sum(fit_probs)
        for _ in range(POP_SIZE):
            i = np.random.choice(POP_SIZE, p=fit_probs)
            k = np.random.choice([j for j in range(POP_SIZE) if j != i])
            phi = np.random.uniform(-1, 1, dim)
            V = np.clip(X[i] + phi * (X[i] - X[k]), bounds[0], bounds[1])
            v_fit = func(V)
            if v_fit < fitness[i]:
                X[i], fitness[i], trials[i] = V, v_fit, 0
            else:
                trials[i] += 1

        # Scout Bees
        scouts = np.where(trials >= limit)[0]
        for i in scouts:
            X[i] = init_population(1, dim, bounds)
            fitness[i] = func(X[i])
            trials[i] = 0

        best_fit = min(best_fit, np.min(fitness))
        if it % RECORD_INTERVAL == 0 and len(history) < NUM_RECORD_POINTS:
            history.append(best_fit)

    return history


# ==========================================
# 3. EXECUTE EXPERIMENTS AND SAVE DATA
# ==========================================
ALGORITHMS = {"PSO": run_PSO, "DE": run_DE, "GA": run_GA, "ABC": run_ABC}

if __name__ == "__main__":
    print(f"Starting experiments: {RUNS} runs, {DIM} dimensions (F6 is 2D)...")

    for func_name, (func, bounds, dim) in FUNCTIONS.items():
        print(f"\nEvaluating {func_name}...")

        for alg_name, algo_runner in ALGORITHMS.items():
            print(f"  Running {alg_name}...", end=" ", flush=True)
            results_matrix = np.zeros((RUNS, NUM_RECORD_POINTS))

            for run in range(RUNS):
                history = algo_runner(func, bounds, dim)
                results_matrix[run, :] = history[:NUM_RECORD_POINTS]

            # Save to CSV (e.g., results/DE_F1.csv)
            np.savetxt(f"results/{alg_name}_{func_name}.csv", results_matrix, delimiter=",")
            print("Done!")

    print("\nAll experiments complete! Data saved to the 'results' folder.")
    print("You can now run your visualization script!")