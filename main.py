import logging
from src.data_loader import generate_synthetic_collections_data
from src.evaluation import CollectionsABTestEvaluator

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_pipeline():
    logging.info("Generating synthetic delinquent account cohort...")
    df = generate_synthetic_collections_data(num_accounts=20000)
    
    logging.info("Evaluating overall Cure Rate A/B test results...")
    evaluator = CollectionsABTestEvaluator(alpha=0.05)
    
    ctrl = df[df['variant'] == 'control']
    trt = df[df['variant'] == 'treatment']
    
    results = evaluator.evaluate_cure_rate(
        control_success=int(ctrl['is_cured'].sum()),
        control_n=len(ctrl),
        treatment_success=int(trt['is_cured'].sum()),
        treatment_n=len(trt)
    )
    
    logging.info(f"--- A/B TEST RESULTS SUMMARY ---")
    logging.info(f"Control Cure Rate: {results['control_cure_rate']*100}%")
    logging.info(f"Treatment Cure Rate: {results['treatment_cure_rate']*100}%")
    logging.info(f"Relative Lift: {results['relative_lift_pct']}% (p-value: {results['p_value']})")
    logging.info(f"Statistically Significant at alpha=0.05? {results['is_stat_sig']}")

if __name__ == "__main__":
    run_pipeline()