from client import FRIProximityTester
import json

def handle_request(req):
    fri = FRIProximityTester()
    action = req.get("action")
    if action == "fold":
        evals = req.get("evaluations", [])
        alpha = req.get("alpha", 1.0)
        folded = fri.fold_codeword(evals, alpha)
        return {"status": "ok", "folded": folded}
    elif action == "rounds":
        evals = req.get("evaluations", [])
        alphas = req.get("alphas", [])
        layers = fri.full_fri_commit_rounds(evals, alphas)
        return {"status": "ok", "layers": layers}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "fold", "evaluations": [1, 2, 3, 4], "alpha": 0.5})))
