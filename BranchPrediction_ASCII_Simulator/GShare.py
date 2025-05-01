class GSHAREBP:
    def __init__(self, m, n):
        self.m = m  # Number of PC bits used for indexing 
        self.n = n  # Number of bits for GBHR
        self.table = [4] * (2 ** m)  # Prediction table 
        self.gbhr = 0  

    def predict(self, PC):
        #extract m bits from PC
        pc_index = (PC >> 2) & ((1 << self.m) - 1)
        # Split into lower n bits and remaining upper bits
        lower_n = pc_index & ((1 << self.n) - 1)
        upper_mn = pc_index >> self.n
        # XOR lower n bits with GBHR for mixing history
        mixed = lower_n ^ self.gbhr        
        index = (upper_mn << self.n) | mixed
        # Predict taken if counter >= 4, else not taken
        prediction = "t" if self.table[index] >= 4 else "n"
        return prediction, index

    def update(self, outcome, index):
        # Update the saturating counters
        if outcome == "t":
            self.table[index] = min(self.table[index] + 1, 7)
        else:
            self.table[index] = max(self.table[index] - 1, 0)
        # Update GBHR shift right and insert new outcome at the MSB
        self.gbhr = ((1 if outcome == "t" else 0) << (self.n - 1)) | (self.gbhr >> 1)
    
    def run(self, trace_file):
        total_preds = 0
        mispreds = 0
        # Process each branch from the trace file
        with open(trace_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                addr, outcome = line.split()
                PC = int(addr, 16)
                pred, index = self.predict(PC)
                if pred != outcome:
                    mispreds += 1
                total_preds += 1
                self.update(outcome, index)
        
        
        print("number of predictions:\t\t", total_preds)
        print("number of mispredictions:\t", mispreds)
        print("misprediction rate:\t\t{:.2f}%".format((mispreds / total_preds) * 100))
        print("FINAL GSHARE CONTENTS")
        for i in range(len(self.table)):
            print(f"{i}\t{self.table[i]}")
