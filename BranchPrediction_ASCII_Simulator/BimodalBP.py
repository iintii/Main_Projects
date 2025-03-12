class BimodalBP:
    def __init__(self, m2):
        self.m2 = m2  # Number of PC bits used for indexing
        self.table = [4] * (2 ** m2)  # 3-bit counters initialized to 4

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

    def run(self, trace_file):
        total_preds = 0
        mispreds = 0

        with open(trace_file, 'r') as f:
            for line in f:
                addr, outcome = line.strip().split()
                PC = int(addr, 16)
                prediction, index = self.predict(PC)
                if prediction != outcome:
                    mispreds += 1
                total_preds += 1
                self.update(outcome, index)

        print("number of predictions:\t\t", total_preds)
        print("number of mispredictions:\t", mispreds)
        print("misprediction rate:\t\t{:.2f}%".format((mispreds / total_preds) * 100))
        print("FINAL BIMODAL CONTENTS")
        for i in range(len(self.table)):
            print(f"{i}\t{self.table[i]}")