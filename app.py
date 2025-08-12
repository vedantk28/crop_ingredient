import csv, re
import streamlit as st

csv_file = "converted_file.csv"
header_row = True
header_col = True
prompt_cells = {f"B{i}" for i in range(2, 8)}  # B2 to B7
computed_cache = {}    # cache for already computed cells

def parse_cell_ref(cell_ref):
    col_letters = ''.join(filter(str.isalpha, cell_ref)).upper()
    row_number_1based = int(''.join(filter(str.isdigit, cell_ref)))
    col_index_0based = 0
    for ch in col_letters:
        col_index_0based = col_index_0based * 26 + (ord(ch) - ord('A') + 1)
    col_index_0based -= 1
    return row_number_1based, col_index_0based, col_letters

def excel_to_csv_indices(row_number_1based, col_index_0based):
    csv_row = row_number_1based if header_row else (row_number_1based - 1)
    csv_col = (col_index_0based + 1) if header_col else col_index_0based
    return csv_row, csv_col

def parse_number(s):
    if s is None:
        return None
    s = str(s).strip()
    if s == "":
        return None
    s2 = s.replace(",", "")
    m = re.search(r"-?\d+(?:\.\d+)?", s2)
    if m:
        return float(m.group())
    return None

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    sheet = list(reader)

def get_cell_value(cell):
    if cell in computed_cache:
        return computed_cache[cell]

    # Hardcode H20 and H21 as constants to break circular reference
    if cell == "H20":
        computed_cache[cell] = 0.0
        return 0.0
    if cell == "H21":
        computed_cache[cell] = 3000.0
        return 3000.0

    row1b, col0b, _ = parse_cell_ref(cell)
    csv_r, csv_c = excel_to_csv_indices(row1b, col0b)

    try:
        raw = sheet[csv_r][csv_c]
        num = parse_number(raw)
        if num is not None:
            computed_cache[cell] = num
            return num
    except IndexError:
        pass

    computed_cache[cell] = 0.0
    return 0.0

def sum_range(start_cell, end_cell):
    start_row, start_col, col_letters = parse_cell_ref(start_cell)
    end_row, _, _ = parse_cell_ref(end_cell)
    total = 0
    for r in range(start_row, end_row + 1):
        total += get_cell_value(f"{col_letters}{r}")
    return total

def sum_range_cells(cell_list):
    total = 0
    for cell in cell_list:
        total += get_cell_value(cell)
    return total

def sumproduct(range1_start, range1_end, range2_start, range2_end):
    start_row1, start_col1, col_letters1 = parse_cell_ref(range1_start)
    end_row1, _, _ = parse_cell_ref(range1_end)
    start_row2, start_col2, col_letters2 = parse_cell_ref(range2_start)
    total = 0
    for i in range(end_row1 - start_row1 + 1):
        total += get_cell_value(f"{col_letters1}{start_row1 + i}") * get_cell_value(f"{col_letters2}{start_row2 + i}")
    return total

# --- Define formula logic ---
def calc_F1():
    val = sum_range("B2", "B41")
    computed_cache["F1"] = val
    return val

def calc_C83():
    val = sumproduct("B2", "B41", "C43", "C82")
    computed_cache["C83"] = val
    return val

def calc_F83():
    val = sumproduct("B2", "B41", "F43", "F82")
    computed_cache["F83"] = val
    return val

def calc_D83():
    val = sumproduct("B2", "B41", "D43", "D82")
    computed_cache["D83"] = val
    return val

def calc_J83():
    val = sumproduct("B2", "B41", "J43", "J82")
    computed_cache["J83"] = val
    return val

def calc_K83():
    val = sumproduct("B2", "B41", "K43", "K82")
    computed_cache["K83"] = val
    return val

def calc_L83():
    val = sumproduct("B2", "B41", "L43", "L82")
    computed_cache["L83"] = val
    return val

def calc_M83():
    val = sumproduct("B2", "B41", "M43", "M82")
    computed_cache["M83"] = val
    return val

def calc_G83():
    val = sumproduct("B2", "B41", "G43", "G82")
    computed_cache["G83"] = val
    return val

def calc_H83():
    val = sumproduct("B2", "B41", "H43", "H82")
    computed_cache["H83"] = val
    return val

def calc_I83():
    val = sumproduct("B2", "B41", "I43", "I82")
    computed_cache["I83"] = val
    return val

def calc_W83():
    val = sumproduct("B2", "B41", "W43", "W82")
    computed_cache["W83"] = val
    return val

def calc_X83():
    val = sumproduct("B2", "B41", "X43", "X82")
    computed_cache["X83"] = val
    return val

def calc_Y83():
    val = sumproduct("B2", "B41", "Y43", "Y82")
    computed_cache["Y83"] = val
    return val

def calc_Z83():
    val = sumproduct("B2", "B41", "Z43", "Z82")
    computed_cache["Z83"] = val
    return val

def calc_AA83():
    val = sumproduct("B2", "B41", "AA43", "AA82")
    computed_cache["AA83"] = val
    return val

def calc_AB83():
    val = sumproduct("B2", "B41", "AB43", "AB82")
    computed_cache["AB83"] = val
    return val

def calc_AC83():
    val = sumproduct("B2", "B41", "AC43", "AC82")
    computed_cache["AC83"] = val
    return val

def calc_AD83():
    val = sumproduct("B2", "B41", "AD43", "AD82")
    computed_cache["AD83"] = val
    return val

def calc_AE83():
    val = sumproduct("B2", "B41", "AE43", "AE82")
    computed_cache["AE83"] = val
    return val

def calc_AF83():
    val = sumproduct("B2", "B41", "AF43", "AF82")
    computed_cache["AF83"] = val
    return val

def calc_B83():
    val = sumproduct("B2", "B41", "B43", "B82")
    computed_cache["B83"] = val
    return val

def calc_M2():
    val = get_cell_value("K2") * get_cell_value("L2") / 1000
    computed_cache["M2"] = val
    return val

def calc_M25():
    val = get_cell_value("K25") * get_cell_value("L25") / 1000
    computed_cache["M25"] = val
    return val

def calc_M26():
    val = sum_range("M2", "M25")
    computed_cache["M26"] = val
    return val

def calc_T18():
    val = sum_range("T16", "T17")
    computed_cache["T18"] = val
    return val

def calc_Z19():
    val = sum_range("Z2", "Z17") / get_cell_value("Z18") if get_cell_value("Z18") != 0 else 0.0
    computed_cache["Z19"] = val
    return val

def calc_F2():
    val = calc_C83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F2"] = val
    return val

def calc_F3():
    val = calc_F83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F3"] = val
    return val

def calc_F4():
    val = (calc_F3() / calc_F2() * 1000) if calc_F2() != 0 else 0.0
    computed_cache["F4"] = val
    return val

def calc_F5():
    val = calc_D83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F5"] = val
    return val

def calc_F6():
    val = calc_J83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F6"] = val
    return val

def calc_F7():
    val = calc_K83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F7"] = val
    return val

def calc_F8():
    val = calc_L83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F8"] = val
    return val

def calc_F9():
    val = calc_F7() + calc_F8()
    computed_cache["F9"] = val
    return val

def calc_F10():
    val = calc_M83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F10"] = val
    return val

def calc_F11():
    val = calc_G83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F11"] = val
    return val

def calc_F12():
    val = calc_H83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F12"] = val
    return val

def calc_F13():
    val = calc_I83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F13"] = val
    return val

def calc_F24():
    val = calc_W83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F24"] = val
    return val

def calc_F25():
    val = calc_X83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F25"] = val
    return val

def calc_F26():
    val = calc_Y83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F26"] = val
    return val

def calc_F27():
    val = calc_Z83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F27"] = val
    return val

def calc_F28():
    val = calc_AA83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F28"] = val
    return val

def calc_F29():
    val = calc_AB83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F29"] = val
    return val

def calc_F30():
    val = calc_AC83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F30"] = val
    return val

def calc_F31():
    val = calc_AD83() / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F31"] = val
    return val

def calc_F32():
    val = calc_AE83() / 1000
    computed_cache["F32"] = val
    return val

def calc_F33():
    val = calc_AF83() / 1000
    computed_cache["F33"] = val
    return val

def calc_F34():
    val = (get_cell_value("K2") * 82500) / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F34"] = val
    return val

def calc_F35():
    val = (get_cell_value("K3") * 40 / calc_F1() if calc_F1() != 0 else 0.0) + \
          (get_cell_value("K12") * 0.5 * 1000 / calc_F1() if calc_F1() != 0 else 0.0)
    computed_cache["F35"] = val
    return val

def calc_F36():
    val = (get_cell_value("K2") * 10) / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F36"] = val
    return val

def calc_F37():
    val = (get_cell_value("K11") * 0.02 * 1000 * 1000) / calc_F1() if calc_F1() != 0 else 0.0
    computed_cache["F37"] = val
    return val

def calc_F38():
    val = get_cell_value("K7") * 0.6
    computed_cache["F38"] = val
    return val

def calc_F17():
    val = calc_F24() / 10
    computed_cache["F17"] = val
    return val

def calc_F18():
    val = calc_F25() / 10
    computed_cache["F18"] = val
    return val

def calc_F16():
    val = calc_F26() / calc_F25() if calc_F25() != 0 else 0.0
    computed_cache["F16"] = val
    return val

def calc_F15():
    val = calc_F17() / calc_F18() if calc_F18() != 0 else 0.0
    computed_cache["F15"] = val
    return val

def calc_F19():
    val = calc_F26() / 10
    computed_cache["F19"] = val
    return val

def calc_F14():
    val = (calc_F25() / 23 + calc_F26() / 39 - calc_F24() / 35) * 100
    computed_cache["F14"] = val
    return val

def calc_F20():
    val = sum_range_cells(["B83", "M26", "T18", "Z19"]) / calc_F1() if calc_F1() != 0 else 0.0
    val += (get_cell_value("H21") / 0.075 * get_cell_value("H20") / 100) / 1000
    computed_cache["F20"] = val
    return val

def calc_F21():
    val = calc_F20() * 75
    computed_cache["F21"] = val
    return val

def calc_F22():
    val = get_cell_value("H21") - calc_F21()
    computed_cache["F22"] = val
    return val

# --- Run ---
st.title("Crop Ingredient Calculator")

labels = {
    "B2": "maize",
    "B3": "jowar",
    "B4": "B.rice",
    "B5": "Wheat",
    "B6": "Bajra",
    "B7": "Ragi"  # Assuming for B7, adjust if needed
}

for cell in sorted(prompt_cells):
    label = labels.get(cell, "Unknown")
    computed_cache[cell] = st.number_input(f"Quantity of {label} ({cell})", min_value=0.0, value=0.0)

# Set B8 to B41 to 0.0
for i in range(8, 42):
    computed_cache[f"B{i}"] = 0.0

if st.button("Calculate"):
    st.write(f"F1: {calc_F1()}")
    st.write(f"F2: {calc_F2()}")
    st.write(f"F3: {calc_F3()}")
    st.write(f"F4: {calc_F4()}")
    st.write(f"F5: {calc_F5()}")
    st.write(f"F6: {calc_F6()}")
    st.write(f"F7: {calc_F7()}")
    st.write(f"F8: {calc_F8()}")
    st.write(f"F9: {calc_F9()}")
    st.write(f"F10: {calc_F10()}")
    st.write(f"F11: {calc_F11()}")
    st.write(f"F12: {calc_F12()}")
    st.write(f"F13: {calc_F13()}")
    st.write(f"F14: {calc_F14()}")
    st.write(f"F15: {calc_F15()}")
    st.write(f"F16: {calc_F16()}")
    st.write(f"F17: {calc_F17()}")
    st.write(f"F18: {calc_F18()}")
    st.write(f"F19: {calc_F19()}")
    st.write(f"F20: {calc_F20()}")
    st.write(f"F21: {calc_F21()}")
    st.write(f"F22: {calc_F22()}")
    st.write(f"F24: {calc_F24()}")
    st.write(f"F25: {calc_F25()}")
    st.write(f"F26: {calc_F26()}")
    st.write(f"F27: {calc_F27()}")
    st.write(f"F28: {calc_F28()}")
    st.write(f"F29: {calc_F29()}")
    st.write(f"F30: {calc_F30()}")
    st.write(f"F31: {calc_F31()}")
    st.write(f"F32: {calc_F32()}")
    st.write(f"F33: {calc_F33()}")
    st.write(f"F34: {calc_F34()}")
    st.write(f"F35: {calc_F35()}")
    st.write(f"F36: {calc_F36()}")
    st.write(f"F37: {calc_F37()}")
    st.write(f"F38: {calc_F38()}")