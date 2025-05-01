import sys

class SMITHNBP:
    def __init__(self, bit_num):
        # Maximum value for the n-bit counter 
        self.max_bit = (2 ** bit_num) - 1  
        # Initialize counter for bit_num > 1 set to mid-value otherwise set to 1
        self.counter = (self.max_bit // 2 + 1) if bit_num > 1 else 1

    def update(self, real_outcome):
        # If branch taken and counter not at maximum increment counter
        if real_outcome == "t" and self.counter < self.max_bit:
            self.counter += 1
        # If branch not-taken and counter not at minimum decrement counter
        elif real_outcome == "n" and self.counter > 0:
            self.counter -= 1

    def pred(self):
        # Calculate threshold for prediction 
        threshold = (self.max_bit // 2) + 1        
        return "t" if self.counter >= threshold else "n"

    def run(self, filename):
        total_preds = 0  # Total number of branches processed
        mispreds = 0     # Count of mispredictions
        with open(filename, 'r') as file:
            for line in file:
                total_preds += 1 
                address, outcome = line.strip().split()
                prediction = self.pred()  # Get current prediction based on counter
                if prediction != outcome:
                    mispreds += 1  
                self.update(outcome)  # Update the counter based on the actual outcome
                
        mispred_rate = (mispreds / total_preds) * 100
        
        print("number of predictions:\t\t{}".format(total_preds))
        print("number of mispredictions:\t{}".format(mispreds))
        print("misprediction rate:\t\t{:.2f}%".format(mispred_rate))
        print("FINAL COUNTER CONTENT:\t\t{}".format(self.counter))
