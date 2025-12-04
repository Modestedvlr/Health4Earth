import time
import tracemalloc
import os
import sys

# On s'assure que Python trouve le package
sys.path.append(os.path.abspath("."))

from health4earth.data_ingest import load_merged_data
from health4earth.analytics import HealthAnalyzer

def measure_performance():
    print("Démarrage du Benchmark Health4Earth...")
    print("-" * 40)

    # 1. Démarrer le monitoring mémoire
    tracemalloc.start()
    
    # 2. Démarrer le chronomètre
    start_time = time.time()

    # --- DÉBUT DU SCÉNARIO ---
    
    # A. Ingestion (Le plus lourd)
    print("1. Chargement et fusion des données...")
    df = load_merged_data()
    print(f"   -> {len(df)} lignes chargées.")

    # B. Initialisation Analyseur
    print("2. Initialisation du moteur IA...")
    analyzer = HealthAnalyzer(df)

    # C. Calcul Lourd (Prédiction IA sur plusieurs pays)
    print("3. Calcul des prédictions 2050 (France, USA, China)...")
    analyzer.predict_evolution("France", "co2", year_end=2050)
    analyzer.predict_evolution("United States", "co2", year_end=2050)
    analyzer.predict_evolution("China", "co2", year_end=2050)
    
    # --- FIN DU SCÉNARIO ---

    # 3. Arrêter le chronomètre
    end_time = time.time()
    
    # 4. Mesurer la mémoire
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # 5. Calculs
    duration = end_time - start_time
    peak_mb = peak / 10**6  # Conversion en Méga-octets

    # 6. Rapport
    print("-" * 40)
    print("RAPPORT DE PERFORMANCE")
    print("-" * 40)
    print(f"Temps total d'exécution : {duration:.4f} secondes")
    print(f"Pic de mémoire RAM      : {peak_mb:.2f} MB")
    print("-" * 40)

if __name__ == "__main__":
    measure_performance()