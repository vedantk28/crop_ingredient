import csv
import re
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Suryacore Feed Formulator",
    page_icon="🌾",
    layout="wide"
)

csv_file = "converted_file.csv"
header_row = True
header_col = True
# Updated prompt_cells to include K2-K15 range
prompt_cells = {f"B{i}" for i in range(2, 32)} | {f"K{i}" for i in range(2, 16)}  # B2-B31 and K2-K15
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

try:
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        sheet = list(reader)
except FileNotFoundError:
    st.error("Error: converted_file.csv not found. Please ensure the CSV file is uploaded or available.")
    sheet = []
    st.stop()

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

# --- Define formula logic (keeping all your existing functions) ---
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
    # Check if all ingredients in the list have cost data
    for cell in st.session_state.ingredient_list:
        if st.session_state.ingredient_list[cell].get('cost', 0) <= 0:
            return "NA"  # Return "NA" if any ingredient lacks cost data
    
    # Calculate total cost if all ingredients have cost data
    total_cost = 0
    for cell, data in st.session_state.ingredient_list.items():
        total_cost += data['quantity'] * data['cost']
    
    total_quantity = calc_F1()
    if total_quantity == 0:
        return "NA"
    
    val = total_cost / total_quantity
    computed_cache["F20"] = val
    return val

def calc_F21():
    cost_per_kg = calc_F20()
    if cost_per_kg == "NA":
        return "NA"
    val = cost_per_kg * 75
    computed_cache["F21"] = val
    return val

def calc_F22():
    cost_per_bag = calc_F21()
    if cost_per_bag == "NA":
        return "NA"
    val = get_cell_value("H21") - cost_per_bag
    computed_cache["F22"] = val
    return val

# NEW OUTPUT CALCULATION FUNCTIONS FOR B39-B41
# CORRECTED OUTPUT CALCULATION FUNCTIONS FOR F34-F41
# CORRECTED OUTPUT CALCULATION FUNCTIONS FOR F34-F41
def calc_F34(): 
    # K2 is separate user input for Premix
    user_quantity_k2 = st.session_state.ingredient_list.get("K2", {}).get('quantity', 0)
    return user_quantity_k2 * 82500 / calc_F1() if calc_F1() != 0 else 0.0

def calc_F35(): 
    # K3 and K12 are separate user inputs for Bcomplex and Vit E 50%
    user_quantity_k3 = st.session_state.ingredient_list.get("K3", {}).get('quantity', 0)
    user_quantity_k12 = st.session_state.ingredient_list.get("K12", {}).get('quantity', 0)
    return (user_quantity_k3 * 40 + user_quantity_k12 * 0.5 * 1000) / calc_F1() if calc_F1() != 0 else 0.0

def calc_F36(): 
    # K2 is separate user input for Premix
    user_quantity_k2 = st.session_state.ingredient_list.get("K2", {}).get('quantity', 0)
    return user_quantity_k2 * 10 / calc_F1() if calc_F1() != 0 else 0.0

def calc_F37(): 
    # K11 is separate user input for Biotin 2%
    user_quantity_k11 = st.session_state.ingredient_list.get("K11", {}).get('quantity', 0)
    return user_quantity_k11 * 0.02 * 1000 * 1000 / calc_F1() if calc_F1() != 0 else 0.0

def calc_F38(): 
    # K7 is separate user input for Choline
    user_quantity_k7 = st.session_state.ingredient_list.get("K7", {}).get('quantity', 0)
    return user_quantity_k7 * 0.6

def calc_F39(): 
    # K3 is separate user input for Bcomplex
    user_quantity_k3 = st.session_state.ingredient_list.get("K3", {}).get('quantity', 0)
    return user_quantity_k3 * 3 / calc_F1() if calc_F1() != 0 else 0.0

def calc_F40(): 
    # K3 is separate user input for Bcomplex
    user_quantity_k3 = st.session_state.ingredient_list.get("K3", {}).get('quantity', 0)
    return user_quantity_k3 * 60 / calc_F1() if calc_F1() != 0 else 0.0

def calc_F41(): 
    # K3 is separate user input for Bcomplex
    user_quantity_k3 = st.session_state.ingredient_list.get("K3", {}).get('quantity', 0)
    return user_quantity_k3 * 40 / calc_F1() if calc_F1() != 0 else 0.0

# CORRECTED OUTPUT CALCULATION FUNCTIONS FOR H24-H39
# These are using sumproduct results which should be correct, but let me show the pattern:
def calc_H24(): return calc_N83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H25(): return calc_O83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H26(): return calc_P83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H27(): return calc_Q83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H28(): return calc_R83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H29(): return calc_S83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H30(): return calc_T83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H31(): return calc_U83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H32(): return calc_V83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H33(): return calc_AS83() / calc_F1() if calc_F1() != 0 else 0.0
def calc_H34(): return calc_E83() / calc_F1() if calc_F1() != 0 else 0.0

def calc_H35(): 
    # K3 is separate user input for Bcomplex
    user_quantity_k3 = st.session_state.ingredient_list.get("K3", {}).get('quantity', 0)
    return user_quantity_k3 * 8 / calc_F1() if calc_F1() != 0 else 0.0

def calc_H36(): 
    # K2 is separate user input for Premix
    user_quantity_k2 = st.session_state.ingredient_list.get("K2", {}).get('quantity', 0)
    return user_quantity_k2 * 50 / calc_F1() if calc_F1() != 0 else 0.0

def calc_H37(): 
    # K3 is separate user input for Bcomplex
    user_quantity_k3 = st.session_state.ingredient_list.get("K3", {}).get('quantity', 0)
    return user_quantity_k3 * 4 / calc_F1() if calc_F1() != 0 else 0.0

def calc_H38(): 
    # K3 is separate user input for Bcomplex
    user_quantity_k3 = st.session_state.ingredient_list.get("K3", {}).get('quantity', 0)
    return user_quantity_k3 * 40 / calc_F1() if calc_F1() != 0 else 0.0

def calc_H39(): 
    # K2 and K6 are separate user inputs for Premix and Dicerol
    user_quantity_k2 = st.session_state.ingredient_list.get("K2", {}).get('quantity', 0)
    user_quantity_k6 = st.session_state.ingredient_list.get("K6", {}).get('quantity', 0)
    return (user_quantity_k2 * 12000 + user_quantity_k6 * 600000) / calc_F1() if calc_F1() != 0 else 0.0

# You'll also need these missing sumproduct functions for the H24-H34 calculations:
def calc_N83():
    val = sumproduct("B2", "B41", "N43", "N82")
    computed_cache["N83"] = val
    return val

def calc_O83():
    val = sumproduct("B2", "B41", "O43", "O82")
    computed_cache["O83"] = val
    return val

def calc_P83():
    val = sumproduct("B2", "B41", "P43", "P82")
    computed_cache["P83"] = val
    return val

def calc_Q83():
    val = sumproduct("B2", "B41", "Q43", "Q82")
    computed_cache["Q83"] = val
    return val

def calc_R83():
    val = sumproduct("B2", "B41", "R43", "R82")
    computed_cache["R83"] = val
    return val

def calc_S83():
    val = sumproduct("B2", "B41", "S43", "S82")
    computed_cache["S83"] = val
    return val

def calc_T83():
    val = sumproduct("B2", "B41", "T43", "T82")
    computed_cache["T83"] = val
    return val

def calc_U83():
    val = sumproduct("B2", "B41", "U43", "U82")
    computed_cache["U83"] = val
    return val

def calc_V83():
    val = sumproduct("B2", "B41", "V43", "V82")
    computed_cache["V83"] = val
    return val

def calc_AS83():
    val = sumproduct("B2", "B41", "AS43", "AS82")
    computed_cache["AS83"] = val
    return val

def calc_E83():
    val = sumproduct("B2", "B41", "E43", "E82")
    computed_cache["E83"] = val
    return val


# Initialize session state for ingredient list
if 'ingredient_list' not in st.session_state:
    st.session_state.ingredient_list = {}

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        margin-bottom: 1rem;
    }
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    .calculate-btn {
        text-align: center;
        margin: 1rem 0;
    }
    .section-header {
        color: #4682B4;
        border-bottom: 2px solid #4682B4;
        padding-bottom: 5px;
        margin-bottom: 1rem;
        font-size: 1.2rem;
    }
    .result-item {
        background-color: #000000;
        padding: 6px;
        margin: 1px 0;
        border-radius: 3px;
        border-left: 3px solid #28a745;
        font-size: 0.85rem;
    }
    .ingredient-item {
        background-color: #f8f9fa;
        padding: 8px;
        margin: 3px 0;
        border-radius: 5px;
        border-left: 4px solid #2196f3;
        font-size: 0.85rem;
        display: flex;
        align-items: center;
    }
    .compact-input {
        font-size: 0.8rem !important;
    }
    .stSelectbox > div > div {
        font-size: 0.85rem;
    }
    .stNumberInput > div > div > input {
        font-size: 0.8rem;
    }
    .ingredient-row {
        display: flex;
        align-items: center;
        padding: 5px 0;
        border-bottom: 1px solid #eee;
    }
    /* Custom button styling for update buttons */
    div[data-testid="column"] button[kind="secondary"] {
        font-size: 0.7rem !important;
        padding: 0.25rem 0.4rem !important;
        height: auto !important;
        min-height: 28px !important;
        white-space: nowrap !important;
    }
    /* Better alignment for input containers */
    .input-container {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
    }
    .input-label {
        min-width: 120px;
        font-weight: bold;
    }
    .input-field {
        flex: 1;
    }
</style>
""", unsafe_allow_html=True)

# Main title with centered container
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🌾 Suryacore Feed Formulator</h1>', unsafe_allow_html=True)

# Create centered layout with reduced margins
col_spacer1, left_col, right_col, col_spacer2 = st.columns([0.5, 1, 1, 0.5], gap="medium")

# Left column - Input section
# Top-level trigger logic (place this near the top of your script)
if st.session_state.get("_queue_calculation", False):
    st.session_state.trigger_calculation = True
    st.session_state._queue_calculation = False

# Left column - Input section
with left_col:
    st.markdown('<h3 class="section-header"> 📋ADD INGREDIENTS</h3>', unsafe_allow_html=True)

    # Ingredient labels
    labels = {
        "B2": "Maize", "B3": "Jowar", "B4": "B.Rice", "B5": "Wheat", "B6": "Bajra", "B7": "Ragi",
        "B8": "R.Polish", "B9": "DORB", "B10": "SFOC", "B11": "DOGN", "B12": "SOYA", "B13": "Fish Meal",
        "B14": "RSM", "B15": "LSP", "B16": "SG", "B17": "Mustard Meal", "B18": "DCP", "B19": "MOLASES",
        "B20": "MEAT AND BONE Meal", "B21": "Oil", "B22": "MGM", "B23": "Methionine", "B24": "Lysine",
        "B25": "Betaine", "B26": "Cocktail Enzyme", "B27": "Phytase", "B28": "SodaBicarb", "B29": "Salt",
        "B30": "TM MIX", "B31": "Rice DDGS",
        "K2": "Premix", "K3": "Bcomplex", "K4": "Toxin Binder", "K5": "Liver", "K6": "Dicerol",
        "K7": "Choline", "K8": "Osconite", "K9": "Anti Coccidial", "K10": "Probiotic", "K11": "Biotin 2%",
        "K12": "Vit E 50%", "K13": "AGP", "K14": "Acidifier", "K15": "Emulsifier"
    }

    # Initialize session state
    if 'selected_ingredients' not in st.session_state:
        st.session_state.selected_ingredients = set()
    if 'ingredient_list' not in st.session_state:
        st.session_state.ingredient_list = {}
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ""

    # Handle clear all action - this must happen before rendering checkboxes
    if st.session_state.get("clear_all_triggered", False):
        # Clear the selected ingredients set first
        st.session_state.selected_ingredients = set()
        st.session_state.ingredient_list = {}
        st.session_state.trigger_calculation = False
        st.session_state._queue_calculation = False
        
        # Set all checkboxes to False
        for cell in sorted(prompt_cells):
            st.session_state[f"chk_{cell}"] = False
            st.session_state[f"qty_{cell}"] = 0.0
            st.session_state[f"cost_{cell}"] = 0.0
        
        # Reset the trigger
        st.session_state.clear_all_triggered = False

    # Search functionality
    st.markdown("##### 🔍 Search Ingredients")
    search_query = st.text_input(
        "Type to search ingredients...",
        value=st.session_state.search_query,
        placeholder="e.g., Maize, Soya, Oil, etc.",
        key="ingredient_search",
        help="Search by ingredient name to filter the list below"
    )
    
    # Update session state with search query
    st.session_state.search_query = search_query

    # Filter ingredients based on search query
    if search_query.strip():
        filtered_cells = [
            cell for cell in sorted(prompt_cells) 
            if search_query.lower() in labels.get(cell, cell).lower()
        ]
        if not filtered_cells:
            st.info(f"No ingredients found matching '{search_query}'")
    else:
        filtered_cells = sorted(prompt_cells)

    # Show ingredient count
    total_ingredients = len(prompt_cells)
    showing_count = len(filtered_cells)
    if search_query.strip():
        st.caption(f"Showing {showing_count} of {total_ingredients} ingredients")
    else:
        st.caption(f"Showing all {total_ingredients} ingredients")

    st.markdown('<h3 class="section-header"></h3>', unsafe_allow_html=True)
    
    # Display filtered ingredients
    with st.container(height=300):
        if filtered_cells:
            for cell in filtered_cells:
                label = labels.get(cell, cell)
                
                # The checkbox will use the session state value we set above
                checked = st.checkbox(label, key=f"chk_{cell}")
                
                if checked:
                    st.session_state.selected_ingredients.add(cell)
                else:
                    st.session_state.selected_ingredients.discard(cell)
        else:
            st.info("Use the search box above to find ingredients")

    st.markdown("### Current Ingredients:")
    updated_ingredients = {}

    if st.session_state.selected_ingredients:
        with st.container(height=300):
            for i, cell in enumerate(sorted(st.session_state.selected_ingredients)):
                label = labels.get(cell, cell)
                col1, col2, col3 = st.columns([2.5, 1.5, 1.5])

                with col1:
                    st.markdown(f"**{label}**")

                with col2:
                    qty = st.number_input(
                        "Qty",
                        min_value=0.0,
                        step=0.1,
                        format="%.2f",
                        key=f"qty_{cell}"
                    )

                with col3:
                    cost = st.number_input(
                        "Cost",
                        min_value=0.0,
                        step=0.01,
                        format="%.2f",
                        key=f"cost_{cell}"
                    )

                updated_ingredients[cell] = {'quantity': qty, 'cost': cost}

        # Calculate and Clear buttons
        col_calc, col_clear = st.columns([1, 1])
        with col_calc:
            if st.button("🔍 Calculate", type="primary"):
                for cell, data in updated_ingredients.items():
                    qty, cost = data['quantity'], data['cost']
                    if qty > 0:
                        st.session_state.ingredient_list[cell] = {
                            'name': labels.get(cell, cell),
                            'quantity': qty,
                            'cost': cost
                        }
                    else:
                        st.warning(f"{labels.get(cell)} skipped — quantity must be > 0")
                st.session_state._queue_calculation = True
                st.rerun()

        with col_clear:
            if st.button("Clear All", type="secondary"):
                # Set the trigger flag instead of doing the clearing directly
                st.session_state.clear_all_triggered = True
                st.rerun()
    else:
        st.info("No ingredients selected yet. Use checkboxes above.")



# Right column - Results section
with right_col:
    st.markdown('<h3 class="section-header">📊 Calculation Results</h3>', unsafe_allow_html=True)

    with st.container(height=600):
        if st.session_state.get("trigger_calculation", False) and st.session_state.ingredient_list:
            for cell in prompt_cells:
                computed_cache[cell] = st.session_state.ingredient_list.get(cell, {}).get('quantity', 0.0)

            try:
                results = {
                    "Total Quantity": calc_F1(),
                    "Crude Protein (%)": calc_F2(),
                    "ME (Mcal/Kg)": calc_F3(),
                    "Calorie:Protein Ratio": calc_F4(),
                    "Crude Fibre (%)": calc_F5(),
                    "Lysine (%)": calc_F6(),
                    "Methionine (%)": calc_F7(),
                    "Cystine (%)": calc_F8(),
                    "MET+CYS (%)": calc_F9(),
                    "Arginine (%)": calc_F10(),
                    "Calcium (%)": calc_F11(),
                    "Total Phosphorus (%)": calc_F12(),
                    "Available Phosphorus (%)": calc_F13(),
                    "Na+K-Cl (mEq/kg)": calc_F14(),
                    "Na:Cl Ratio": calc_F15(),
                    "Na:K Ratio": calc_F16(),
                    "Chloride (%)": calc_F17(),
                    "Sodium (%)": calc_F18(),
                    "Potassium (%)": calc_F19(),
                    "Cost per kg": calc_F20(),
                    "Cost per Bag": calc_F21(),
                    "Margin": calc_F22(),
                    "Chloride (mg/kg)": calc_F24(),
                    "Sodium (mg/kg)": calc_F25(),
                    "Potassium (mg/kg)": calc_F26(),
                    "Manganese (mg/kg)": calc_F27(),
                    "Zinc (mg/kg)": calc_F28(),
                    "Selenium (mg/kg)": calc_F29(),
                    "Iron (mg/kg)": calc_F30(),
                    "Copper (mg/kg)": calc_F31(),
                    "Cobalt (mg/kg)": calc_F32(),
                    "Iodine (mg/kg)": calc_F33(),
                    "Vitamin A (IU/kg)": calc_F34(),
                    "Vitamin E (IU/kg)": calc_F35(),
                    "Vitamin K (mg/kg)": calc_F36(),
                    "Biotin (mcg/kg)": calc_F37(),
                    "Choline (mg/kg)": calc_F38(),
                    "Folicacid": calc_F39(),
                    "Niacin": calc_F40(),
                    "Panthothenicacid": calc_F41(),
                    "Histidine": calc_H24(),
                    "Leucine": calc_H25(),
                    "Isoleucine": calc_H26(),
                    "P.Alanine": calc_H27(),
                    "Threonine": calc_H28(),
                    "Tryoptophan": calc_H29(),
                    "Tyrosine": calc_H30(),
                    "Valine": calc_H31(),
                    "Serine": calc_H32(),
                    "Linoleicacid": calc_H33(),
                    "AFT": calc_H34(),
                    "B6": calc_H35(),
                    "B2": calc_H36(),
                    "B1": calc_H37(),
                    "B12": calc_H38(),
                    "D3": calc_H39()
                }

                for param, value in results.items():
                    if value == "NA":
                        st.markdown(f'<div class="result-item"><strong>{param}:</strong> NA</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="result-item"><strong>{param}:</strong> {value:.4f}</div>', unsafe_allow_html=True)

                st.session_state.trigger_calculation = False

            except Exception as e:
                st.error(f"Error in calculation: {str(e)}")
                st.write("Please check your inputs and try again.")

        elif not st.session_state.ingredient_list:
                st.warning("⚠️ Please add some ingredients before calculating!")

        else:
                st.info("👆 Add ingredients from the left panel and click 'Calculate' to see results.")
                st.markdown("""
    **Instructions:**
    1. Select ingredients using the checkboxes  
    2. Enter the quantity and cost per kg  
    3. Click 'Calculate' to trigger nutritional analysis  
    4. Use 'Clear All' to reset the formulation  

    **Note:** All calculations are based on the nutritional database from your CSV file.
    """)
