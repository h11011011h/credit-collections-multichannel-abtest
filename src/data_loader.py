import numpy as np
import pandas as pd

def generate_synthetic_collections_data(num_accounts: int = 20000, seed: int = 42) -> pd.DataFrame:
    """Generates a synthetic 30-60 DPD delinquent account cohort with variant assignments."""
    np.random.seed(seed)
    
    account_ids = [f"ACC_{i:06d}" for i in range(num_accounts)]
    variants = np.random.choice(['control', 'treatment'], size=num_accounts, p=[0.5, 0.5])
    balances = np.random.exponential(scale=1500, size=num_accounts) + 200
    
    base_cure_prob = 0.22
    
    cured = []
    recoveries = []
    costs = []
    
    for v, bal in zip(variants, balances):
        boost = 0.04 if (v == 'treatment' and bal > 1500) else (0.02 if v == 'treatment' else 0.0)
        prob = np.clip(base_cure_prob + boost, 0, 1)
        
        is_cured = np.random.rand() < prob
        cured.append(is_cured)
        
        cost = 1.95 if v == 'treatment' else 1.20
        costs.append(cost)
        
        recovery = bal * np.random.uniform(0.8, 1.0) if is_cured else bal * np.random.uniform(0.0, 0.2)
        recoveries.append(recovery)
        
    df = pd.DataFrame({
        'account_id': account_ids,
        'variant': variants,
        'balance': np.round(balances, 2),
        'is_cured': cured,
        'total_recovery': np.round(recoveries, 2),
        'outreach_cost': costs
    })
    
    df['net_recovery'] = df['total_recovery'] - df['outreach_cost']
    return df