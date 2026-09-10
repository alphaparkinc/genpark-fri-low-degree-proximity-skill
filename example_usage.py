from client import FRIProximityTester

def main():
    print("=== Testing FRI Low-Degree Proximity Testing ===")
    fri = FRIProximityTester()
    
    # 8-point codeword
    evals = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    print(f"Initial Codeword ({len(evals)} evals): {evals}")
    
    alphas = [0.5, 0.25]
    layers = fri.full_fri_commit_rounds(evals, alphas)
    for idx, layer in enumerate(layers):
        print(f"  Layer {idx} (size {len(layer)}): {layer}")
        
    assert len(layers[-1]) == 2
    print("=== FRI Proximity Test Verification Complete ===")

if __name__ == "__main__":
    main()
