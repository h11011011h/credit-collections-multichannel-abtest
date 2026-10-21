import numpy as np
import scipy.stats as stats
from typing import Dict, Any

class CollectionsABTestEvaluator:
    """Evaluates cure rates and net financial recovery for collections strategies."""
    
    def __init__(self, alpha: float = 0.05):
        self.alpha = alpha

    def evaluate_cure_rate(self, control_success: int, control_n: int, 
                           treatment_success: int, treatment_n: int) -> Dict[str, Any]:
        p1 = control_success / control_n
        p2 = treatment_success / treatment_n
        
        p_pooled = (control_success + treatment_success) / (control_n + treatment_n)
        se_pooled = np.sqrt(p_pooled * (1 - p_pooled) * (1 / control_n + 1 / treatment_n))
        
        z_stat = (p2 - p1) / se_pooled
        p_val = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        
        return {
            "control_cure_rate": round(p1, 4),
            "treatment_cure_rate": round(p2, 4),
            "absolute_lift": round(p2 - p1, 4),
            "relative_lift_pct": round(((p2 - p1) / p1) * 100, 2),
            "p_value": round(p_val, 5),
            "is_stat_sig": p_val < self.alpha
        }