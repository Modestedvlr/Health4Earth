import time
import tracemalloc
import pandas as pd
from health4earth.data_ingest import load_co2_data
from health4earth.analytics import HealthAnalyzer

def measure_performance():
    print("--- Démarrage de l'analyse de performance ---")

    # 1. Démarrer le suivi de la mémoire
    tracemalloc.start()
    
    # 2. Démarrer le chronomètre
    start_time = time.time()

    # --- CODE À TESTER ---
    print("1. Chargement des données...")
    df = load_co2_data()
    
    print("2. Analyse statistique...")
    if 'pollution' not in df.columns:
        df['pollution'] = df['co2'] # Simulation pour le test
    if 'life_expectancy' not in df.columns:
        df['life_expectancy'] = 70.0
        
    analyzer = HealthAnalyzer(df)
    corr = analyzer.correlation_analysis()
    # ---------------------

    # 3. Arrêter le chronomètre
    end_time = time.time()
    
    # 4. Mesurer la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # 5. Afficher le rapport
    execution_time = end_time - start_time
    peak_mb = peak / 10**6

    print("\n--- RAPPORT DE PERFORMANCE ---")
    print(f"⏱️  Temps d'exécution : {execution_time:.4f} secondes")
    print(f"💾  Mémoire Pic       : {peak_mb:.2f} MB")
    print("------------------------------")

if __name__ == "__main__":
    measure_performance()