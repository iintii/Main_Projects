import curses
import time

# Import predictor classes from your existing modules.
from GShare import GSHAREBP
from nBIT import SMITHNBP
from BimodalBP import BimodalBP
from HybridBP import HybridBP

# ------------------------------
# Utility Function for Input
# ------------------------------
def get_input(stdscr, prompt, row, col):
    curses.echo()  # Enable echoing of typed characters
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()
    inp = stdscr.getstr(row, col + len(prompt)).decode('utf-8')
    curses.noecho()  # Disable echoing after input is done
    return inp

# ------------------------------
# Menus for Selection and Parameter Input
# ------------------------------
def predictor_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "Select a Predictor:", curses.A_BOLD)
    stdscr.addstr(3, 4, "1) Smith n-bit Predictor")
    stdscr.addstr(4, 4, "2) GShare Predictor")
    stdscr.addstr(5, 4, "3) Bimodal Predictor")
    stdscr.addstr(6, 4, "4) Hybrid Predictor")
    stdscr.addstr(8, 2, "Press 1-4 to select, or 'q' to quit.")
    stdscr.refresh()
    while True:
        c = stdscr.getch()
        if c == ord('1'):
            return "Smith"
        elif c == ord('2'):
            return "GShare"
        elif c == ord('3'):
            return "Bimodal"
        elif c == ord('4'):
            return "Hybrid"
        elif c == ord('q'):
            return None
        time.sleep(0.1)

def trace_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "Select a Trace File:", curses.A_BOLD)
    stdscr.addstr(3, 4, "1) traces/gcc_trace.txt")
    stdscr.addstr(4, 4, "2) traces/jpeg_trace.txt")
    stdscr.addstr(5, 4, "3) traces/perl_trace.txt")
    stdscr.addstr(7, 2, "Press 1-3 to select, or 'q' to quit.")
    stdscr.refresh()
    while True:
        c = stdscr.getch()
        if c == ord('1'):
            return "traces/gcc_trace.txt"
        elif c == ord('2'):
            return "traces/jpeg_trace.txt"
        elif c == ord('3'):
            return "traces/perl_trace.txt"
        elif c == ord('q'):
            return None
        time.sleep(0.1)

def parameter_input(stdscr, predictor_type):
    stdscr.clear()
    params = {}
    row = 2
    col = 2
    stdscr.addstr(row, col, f"Enter parameters for {predictor_type} Predictor:", curses.A_BOLD)
    row += 2
    if predictor_type == "Smith":
        inp = get_input(stdscr, "Bit number (e.g., 3): ", row, col)
        params["bit_num"] = int(inp)
    elif predictor_type == "GShare":
        inp = get_input(stdscr, "m (PC bits, e.g., 9): ", row, col)
        params["m"] = int(inp)
        row += 1
        inp = get_input(stdscr, "n (GBHR bits, e.g., 3): ", row, col)
        params["n"] = int(inp)
    elif predictor_type == "Bimodal":
        inp = get_input(stdscr, "m2 (PC bits, e.g., 9): ", row, col)
        params["m2"] = int(inp)
    elif predictor_type == "Hybrid":
        inp = get_input(stdscr, "k (chooser PC bits, e.g., 8): ", row, col)
        params["k"] = int(inp)
        row += 1
        inp = get_input(stdscr, "m1 (GShare PC bits, e.g., 14): ", row, col)
        params["m1"] = int(inp)
        row += 1
        inp = get_input(stdscr, "n (GBHR bits, e.g., 10): ", row, col)
        params["n"] = int(inp)
        row += 1
        inp = get_input(stdscr, "m2 (Bimodal PC bits, e.g., 5): ", row, col)
        params["m2"] = int(inp)
    return params

# ------------------------------
# Hybrid Predictor Per-Branch Wrapper
# ------------------------------
def hybrid_predict_and_update(predictor, PC, outcome):
    # Compute chooser index: discard 2 LSBs and extract k bits
    chooser_index = (PC >> 2) & ((1 << predictor.k) - 1)
    # Get predictions from GShare and Bimodal predictors inside the hybrid predictor
    g_pred, g_index = predictor.gshare.predict(PC)
    b_pred, b_index = predictor.bimodal.predict(PC)
    # Select predictor using chooser counter (>=2 selects GShare)
    if predictor.chooser_table[chooser_index] >= 2:
        final_pred = g_pred
        chosen = "gshare"
    else:
        final_pred = b_pred
        chosen = "bimodal"
    # Always update GShare predictor (updates both counter and GBHR)
    predictor.gshare.update(outcome, g_index)
    # Update Bimodal predictor only if it was selected
    if chosen == "bimodal":
        predictor.bimodal.update(outcome, b_index)
    # Update chooser counter based on which predictor was correct
    if g_pred == outcome and b_pred != outcome:
        predictor.chooser_table[chooser_index] = min(predictor.chooser_table[chooser_index] + 1, 3)
    elif b_pred == outcome and g_pred != outcome:
        predictor.chooser_table[chooser_index] = max(predictor.chooser_table[chooser_index] - 1, 0)
    return final_pred

# ------------------------------
# Simulation Loop
# ------------------------------
def simulation_loop(stdscr, predictor, predictor_type, trace_file):
    total_preds = 0
    mispreds = 0
    try:
        with open(trace_file, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        stdscr.addstr(0, 0, f"Error reading trace file: {e}")
        stdscr.refresh()
        time.sleep(2)
        return

    num_lines = len(lines)
    line_index = 0

    stdscr.nodelay(True)  # Non-blocking input
    curses.curs_set(0)    # Hide cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    stdscr.bkgd(' ', curses.color_pair(1))

    while True:
        max_y, max_x = stdscr.getmaxyx()
        if max_y < 20 or max_x < 60:
            stdscr.erase()
            stdscr.addstr(0, 0, "Terminal too small. Please enlarge.", curses.A_BLINK)
            stdscr.refresh()
            time.sleep(0.5)
            continue

        if line_index >= num_lines:
            line_index = 0  # Loop back to the start of the trace file

        line = lines[line_index].strip()
        line_index += 1
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        addr, outcome = parts[0], parts[1]
        try:
            PC = int(addr, 16)
        except Exception:
            continue

        # Process branch according to predictor type
        if predictor_type == "Hybrid":
            pred = hybrid_predict_and_update(predictor, PC, outcome)
        elif predictor_type == "GShare":
            pred, index = predictor.predict(PC)
            predictor.update(outcome, index)
        elif predictor_type == "Bimodal":
            pred, index = predictor.predict(PC)
            predictor.update(outcome, index)
        elif predictor_type == "Smith":
            pred = predictor.pred()
            predictor.update(outcome)
        else:
            pred = "?"

        total_preds += 1
        if pred != outcome:
            mispreds += 1

        # Update display with simulation stats and predictor internal state.
        stdscr.erase()
        stdscr.addstr(1, 2, "Real-Time Branch Predictor Simulation", curses.A_BOLD)
        stdscr.addstr(2, 2, f"Predictor Type: {predictor_type}")
        stdscr.addstr(3, 2, f"Trace File: {trace_file}")
        stdscr.addstr(4, 2, f"Total Predictions: {total_preds}")
        stdscr.addstr(5, 2, f"Mispredictions: {mispreds}")
        rate = (mispreds / total_preds) * 100 if total_preds > 0 else 0
        stdscr.addstr(6, 2, f"Misprediction Rate: {rate:.2f}%")
        
        if predictor_type == "GShare":
            stdscr.addstr(7, 2, f"GBHR: {bin(predictor.gbhr)[2:].zfill(predictor.n)}")
        elif predictor_type == "Smith":
            stdscr.addstr(7, 2, f"Counter: {predictor.counter}")
        elif predictor_type == "Hybrid":
            stdscr.addstr(7, 2, "Chooser Table (first 5): " + " ".join(str(x) for x in predictor.chooser_table[:5]))
            stdscr.addstr(8, 2, f"GBHR: {bin(predictor.gshare.gbhr)[2:].zfill(predictor.gshare.n)}")
        
        # Display a few entries of the prediction tables
        if predictor_type in ["GShare", "Bimodal"]:
            stdscr.addstr(10, 2, "Predictor Table (first 10 entries):")
            for i in range(min(10, len(predictor.table))):
                if 11 + i < max_y - 2:
                    stdscr.addstr(11 + i, 4, f"Index {i}: {predictor.table[i]}")
        elif predictor_type == "Hybrid":
            stdscr.addstr(10, 2, "GShare Table (first 10 entries):")
            for i in range(min(10, len(predictor.gshare.table))):
                if 11 + i < max_y - 4:
                    stdscr.addstr(11 + i, 4, f"Index {i}: {predictor.gshare.table[i]}")
            stdscr.addstr(21, 2, "Bimodal Table (first 10 entries):")
            for i in range(min(10, len(predictor.bimodal.table))):
                if 22 + i < max_y - 2:
                    stdscr.addstr(22 + i, 4, f"Index {i}: {predictor.bimodal.table[i]}")
        
        stdscr.addstr(max_y - 2, 2, "Press 'q' to quit.")
        stdscr.refresh()
        time.sleep(0.05)
        
        try:
            key = stdscr.getch()
            if key == ord('q'):
                break
        except Exception:
            pass

def main(stdscr):
    predictor_type = predictor_menu(stdscr)
    if predictor_type is None:
        return
    params = parameter_input(stdscr, predictor_type)
    trace_file = trace_menu(stdscr)
    if trace_file is None:
        return

    # Instantiate the selected predictor using the provided parameters.
    if predictor_type == "Smith":
        predictor = SMITHNBP(bit_num=params["bit_num"])
    elif predictor_type == "GShare":
        predictor = GSHAREBP(m=params["m"], n=params["n"])
    elif predictor_type == "Bimodal":
        predictor = BimodalBP(m2=params["m2"])
    elif predictor_type == "Hybrid":
        predictor = HybridBP(k=params["k"], m1=params["m1"], n=params["n"], m2=params["m2"])
    else:
        predictor = None

    if predictor is not None:
        simulation_loop(stdscr, predictor, predictor_type, trace_file)

if __name__ == "__main__":
    curses.wrapper(main)
