import sys

#######################
# Gshare Branch Predictor
#######################
class GSHAREBP:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        # Table with 2^m entries 
        self.table = [4] * (2 ** m)
        # Global branch history register (n bits), initially zero
        self.gbhr = 0

    def predict(self, PC):
        # Discard lowest 2 bits of PC and keep m bits.
        pc_index = (PC >> 2) & ((1 << self.m) - 1)
        lower_n = pc_index & ((1 << self.n) - 1)
        upper = pc_index >> self.n
        # XOR the lower n bits with the gbhr to mix history information
        mixed = lower_n ^ self.gbhr
        index = (upper << self.n) | mixed
        pred = "t" if self.table[index] >= 4 else "n"
        return pred, index

    def update(self, outcome, index):
        if outcome == "t":
            self.table[index] = min(self.table[index] + 1, 7)
        else:
            self.table[index] = max(self.table[index] - 1, 0)
        self.gbhr = (((1 if outcome == "t" else 0) << (self.n - 1)) | (self.gbhr >> 1)) & ((1 << self.n) - 1)

    def update_gbhr(self, outcome):
        # Update only the global branch history register without chanign the saturation counters
        self.gbhr = (((1 if outcome == "t" else 0) << (self.n - 1)) | (self.gbhr >> 1)) & ((1 << self.n) - 1)


##########################
# Bimodal Branch Predictor
##########################
class BimodalBP:
    def __init__(self, m2):
        self.m2 = m2  # Number of PC bits used for indexing
        self.table = [4] * (2 ** m2)  # 3bit counters initialized to 4

    def predict(self, PC):
        # Discard lowest 2 bits, then use m2 bits for index
        index = (PC >> 2) & ((1 << self.m2) - 1)
        prediction = "t" if self.table[index] >= 4 else "n"
        return prediction, index

    def update(self, outcome, index):
        if outcome == "t":
            if self.table[index] < 7:
                self.table[index] += 1
        else:
            if self.table[index] > 0:
                self.table[index] -= 1


#############################
# Hybrid Branch Predictor
#############################
class HybridBP:
    def __init__(self, k, m1, n, m2):
        self.k = k
        # Create chooser table with 2^k entries 
        self.chooser_table = [1] * (2 ** k)
        self.gshare = GSHAREBP(m1, n)
        self.bimodal = BimodalBP(m2)

    def run(self, trace_file):
        total_preds = 0
        mispreds = 0
        with open(trace_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                addr, outcome = line.split()
                PC = int(addr, 16)
                # Use PC bits for chooser index 
                chooser_index = (PC >> 2) & ((1 << self.k) - 1)

                # Get predictions from each predictor while still in the “old state"
                g_pred, g_index = self.gshare.predict(PC)
                b_pred, b_index = self.bimodal.predict(PC)

                # Chooser decision based on stored predictions
                if self.chooser_table[chooser_index] >= 2:
                    final_pred, chosen = g_pred, "gshare"
                else:
                    final_pred, chosen = b_pred, "bimodal"

                if final_pred != outcome:
                    mispreds += 1
                total_preds += 1

                # First, update the chooser counter using the stored predictions 
                if g_pred == outcome and b_pred != outcome:
                    self.chooser_table[chooser_index] = min(self.chooser_table[chooser_index] + 1, 3)
                elif b_pred == outcome and g_pred != outcome:
                    self.chooser_table[chooser_index] = max(self.chooser_table[chooser_index] - 1, 0)

                #  Now update the selected predictor and its associated state 
                if chosen == "gshare":
                    self.gshare.update(outcome, g_index)
                else:
                    self.bimodal.update(outcome, b_index)
                    # update gshare's global branch history register even if bimodal was used
                    self.gshare.update_gbhr(outcome)

        mispred_rate = (mispreds / total_preds) * 100
        print("number of predictions:\t\t{}".format(total_preds))
        print("number of mispredictions:\t{}".format(mispreds))
        print("misprediction rate:\t\t{:.2f}%".format(mispred_rate))
        print("FINAL CHOOSER CONTENTS:")
      
        for i, val in enumerate(self.chooser_table):           
            print("{}\t{}".format(i, val))
        print("FINAL GSHARE CONTENTS:")
        for i, val in enumerate(self.gshare.table):
            print("{}\t{}".format(i, val))
        print("FINAL BIMODAL CONTENTS:")
        for i, val in enumerate(self.bimodal.table):
            print("{}\t{}".format(i, val))


