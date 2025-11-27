import time

def profile_function(func, *args, **kwargs):
    """Mesure le temps d'exécution d'une fonction."""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    print(f"Temps d'exécution: {end - start:.4f} secondes")
    return result
