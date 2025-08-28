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
prompt_cells = {f"B{i}" for i in range(2, 32)}  # B1 to B31
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
        font-size: 0.5rem !important;
        padding: 0.25rem 0.4rem !important;
        height: auto !important;
        min-height: 28px !important;
        white-space: nowrap !important;
    }
</style>
""", unsafe_allow_html=True)

# Main title with centered container
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🌾 Suryacore Feed Formulator</h1>', unsafe_allow_html=True)

# Create centered layout with reduced margins
col_spacer1, left_col, right_col, col_spacer2 = st.columns([0.5, 1, 1, 0.5], gap="medium")

# Left column - Input section
with left_col:
    st.markdown('<h3 class="section-header">📋 Add Ingredients</h3>', unsafe_allow_html=True)
    
    # Ingredient labels dictionary
    labels = {
        "B2": "Maize",
        "B3": "Jowar", 
        "B4": "B.Rice",
        "B5": "Wheat",
        "B6": "Bajra",
        "B7": "Ragi",
        "B8": "R.Polish",
        "B9": "DORB",
        "B10": "SFOC",
        "B11": "DOGN",
        "B12": "SOYA",
        "B13": "Fish Meal",
        "B14": "RSM",
        "B15": "LSP",
        "B16": "SG",
        "B17": "Mustard Meal",
        "B18": "DCP",
        "B19": "MOLASES",
        "B20": "MEAT AND BONE Meal",
        "B21": "Oil",
        "B22": "MGM",
        "B23": "Methionine",
        "B24": "Lysine",
        "B25": "Betaine",
        "B26": "Cocktail Enzyme",
        "B27": "Phytase",
        "B28": "SodaBicarb",
        "B29": "Salt",
        "B30": "TM MIX",
        "B31": "Rice DDGS"
    }
    
    # Dropdown for ingredient selection
    available_ingredients = [labels[cell] for cell in sorted(prompt_cells)]
    selected_ingredient = st.selectbox(
        "Select Ingredient:", 
        options=["Select an ingredient..."] + available_ingredients,
        key="ingredient_selector"
    )
    
    if selected_ingredient != "Select an ingredient...":
        # Find the corresponding cell
        selected_cell = None
        for cell, label in labels.items():
            if label == selected_ingredient:
                selected_cell = cell
                break
        
        if selected_cell:
            # Quantity input with smaller size
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.write(f"**{selected_ingredient}**")
            with col2:
                quantity = st.number_input(
                    "Quantity", 
                    min_value=0.0,
                    step=0.1,
                    format="%.2f",
                    key=f"qty_{selected_cell}",
                    label_visibility="collapsed"
                )
            with col3:
                if st.button("Add", key=f"add_{selected_cell}", type="primary"):
                    if quantity > 0:
                        st.session_state.ingredient_list[selected_cell] = {
                            'name': selected_ingredient,
                            'quantity': quantity
                        }
                        st.success(f"Added {selected_ingredient}")
                        st.rerun()
    
    # Display current ingredient list with editable quantities
    st.markdown("### Current Ingredients:")
    if st.session_state.ingredient_list:
        with st.container(height=300):
            # Track changes to ingredient quantities
            updated_ingredients = {}
            
            for i, (cell, data) in enumerate(st.session_state.ingredient_list.items()):
                col1, col2, col3, col4 = st.columns([3, 2, 1, 0.5])
                
                with col1:
                    st.markdown(f'**{data["name"]}**')
                
                with col2:
                    # Editable quantity field for each ingredient
                    new_quantity = st.number_input(
                        "Edit Qty",
                        min_value=0.0,
                        value=data["quantity"],
                        step=0.1,
                        format="%.2f",
                        key=f"edit_qty_{cell}_{i}",
                        label_visibility="collapsed"
                    )
                    updated_ingredients[cell] = new_quantity
                
                with col3:
                    # Update button for individual ingredient
                    if st.button("ADD", key=f"update_{cell}_{i}", type="secondary"):
                        if new_quantity > 0:
                            st.session_state.ingredient_list[cell]['quantity'] = new_quantity
                            st.success(f"Updated {data['name']}")
                            st.rerun()
                        elif new_quantity == 0:
                            st.warning(f"Quantity cannot be 0. Use remove button to delete ingredient.")
                
                with col4:
                    # Remove button
                    if st.button("❌", key=f"remove_{cell}_{i}", help="Remove ingredient"):
                        del st.session_state.ingredient_list[cell]
                        st.rerun()
        
        # Bulk update and clear buttons
        col_update, col_clear = st.columns([1, 1])
        with col_update:
            if st.button("Update All", type="primary"):
                changes_made = False
                for cell, new_qty in updated_ingredients.items():
                    if cell in st.session_state.ingredient_list and new_qty > 0:
                        if st.session_state.ingredient_list[cell]['quantity'] != new_qty:
                            st.session_state.ingredient_list[cell]['quantity'] = new_qty
                            changes_made = True
                        elif new_qty == 0:
                            st.warning(f"Skipped {st.session_state.ingredient_list[cell]['name']} - quantity cannot be 0")
                
                if changes_made:
                    st.success("All quantities updated!")
                    st.rerun()
                else:
                    st.info("No changes detected")
        
        with col_clear:
            if st.button("Clear All", type="secondary"):
                st.session_state.ingredient_list = {}
                st.rerun()
    else:
        st.info("No ingredients added yet. Select ingredients from the dropdown above.")

# Right column - Results section
with right_col:
    st.markdown('<h3 class="section-header">📊 Calculation Results</h3>', unsafe_allow_html=True)
    
    # Calculate button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        calculate_button = st.button("🔍 Calculate", type="primary", use_container_width=True)
    
    # Create scrollable container for results
    with st.container(height=600):
        if calculate_button and st.session_state.ingredient_list:
            # Update computed_cache with ingredient list values
            for cell in prompt_cells:
                if cell in st.session_state.ingredient_list:
                    computed_cache[cell] = st.session_state.ingredient_list[cell]['quantity']
                else:
                    computed_cache[cell] = 0.0
            
            try:
                # Calculate all results
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
                    "Choline (mg/kg)": calc_F38()
                }
                
                # Display results with better formatting
                significant_results = {k: v for k, v in results.items() if abs(v) > 0.0001}
                
                if significant_results:
                    for param, value in significant_results.items():
                        st.markdown(f'''
                        <div class="result-item">
                            <strong>{param}:</strong> {value:.4f}
                        </div>
                        ''', unsafe_allow_html=True)
                else:
                    st.warning("No significant results to display. Please add ingredients with quantities.")
                        
            except Exception as e:
                st.error(f"Error in calculation: {str(e)}")
                st.write("Please check your inputs and try again.")
        
        elif calculate_button and not st.session_state.ingredient_list:
            st.warning("⚠️ Please add some ingredients before calculating!")
        
        else:
            st.info("👆 Add ingredients from the left panel and click 'Calculate' to see results.")
            st.markdown("""
            **Instructions:**
            1. Select an ingredient from the dropdown
            2. Enter the quantity 
            3. Click 'Add' to add it to your formulation
            4. Edit quantities directly in the ingredient list
            5. Click 'Update' for individual changes or 'Update All' for bulk changes
            6. Click 'Calculate' to see nutritional analysis
            
            **Note:** All calculations are based on the nutritional database from your CSV file.
            """)

# Footer
st.markdown("---")
st.markdown("*Suryacore Feed Formulator - Professional Feed Formulation Tool*")
st.markdown('</div>', unsafe_allow_html=True)  # Close main-containerimport csv
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
prompt_cells = {f"B{i}" for i in range(2, 32)}  # B1 to B31
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
</style>
""", unsafe_allow_html=True)

# Main title with centered container
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🌾 Suryacore Feed Formulator</h1>', unsafe_allow_html=True)

# Create centered layout with reduced margins
col_spacer1, left_col, right_col, col_spacer2 = st.columns([0.5, 1, 1, 0.5], gap="medium")

# Left column - Input section
with left_col:
    st.markdown('<h3 class="section-header">📋 Add Ingredients</h3>', unsafe_allow_html=True)
    
    # Ingredient labels dictionary
    labels = {
        "B2": "Maize",
        "B3": "Jowar", 
        "B4": "B.Rice",
        "B5": "Wheat",
        "B6": "Bajra",
        "B7": "Ragi",
        "B8": "R.Polish",
        "B9": "DORB",
        "B10": "SFOC",
        "B11": "DOGN",
        "B12": "SOYA",
        "B13": "Fish Meal",
        "B14": "RSM",
        "B15": "LSP",
        "B16": "SG",
        "B17": "Mustard Meal",
        "B18": "DCP",
        "B19": "MOLASES",
        "B20": "MEAT AND BONE Meal",
        "B21": "Oil",
        "B22": "MGM",
        "B23": "Methionine",
        "B24": "Lysine",
        "B25": "Betaine",
        "B26": "Cocktail Enzyme",
        "B27": "Phytase",
        "B28": "SodaBicarb",
        "B29": "Salt",
        "B30": "TM MIX",
        "B31": "Rice DDGS"
    }
    
    # Dropdown for ingredient selection
    available_ingredients = [labels[cell] for cell in sorted(prompt_cells)]
    selected_ingredient = st.selectbox(
        "Select Ingredient:", 
        options=["Select an ingredient..."] + available_ingredients,
        key="ingredient_selector"
    )
    
    if selected_ingredient != "Select an ingredient...":
        # Find the corresponding cell
        selected_cell = None
        for cell, label in labels.items():
            if label == selected_ingredient:
                selected_cell = cell
                break
        
        if selected_cell:
            # Quantity input with smaller size
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.write(f"**{selected_ingredient}**")
            with col2:
                quantity = st.number_input(
                    "Quantity", 
                    min_value=0.0,
                    step=0.1,
                    format="%.2f",
                    key=f"qty_{selected_cell}",
                    label_visibility="collapsed"
                )
            with col3:
                if st.button("Add", key=f"add_{selected_cell}", type="primary"):
                    if quantity > 0:
                        st.session_state.ingredient_list[selected_cell] = {
                            'name': selected_ingredient,
                            'quantity': quantity
                        }
                        st.success(f"Added {selected_ingredient}")
                        st.rerun()
    
    # Display current ingredient list with editable quantities
    st.markdown("### Current Ingredients:")
    if st.session_state.ingredient_list:
        with st.container(height=300):
            # Track changes to ingredient quantities
            updated_ingredients = {}
            
            for i, (cell, data) in enumerate(st.session_state.ingredient_list.items()):
                col1, col2, col3, col4 = st.columns([3, 2, 1, 0.5])
                
                with col1:
                    st.markdown(f'**{data["name"]}**')
                
                with col2:
                    # Editable quantity field for each ingredient
                    new_quantity = st.number_input(
                        "Edit Qty",
                        min_value=0.0,
                        value=data["quantity"],
                        step=0.1,
                        format="%.2f",
                        key=f"edit_qty_{cell}_{i}",
                        label_visibility="collapsed"
                    )
                    updated_ingredients[cell] = new_quantity
                
                with col3:
                    # Update button for individual ingredient
                    if st.button("Update", key=f"update_{cell}_{i}", type="secondary"):
                        if new_quantity > 0:
                            st.session_state.ingredient_list[cell]['quantity'] = new_quantity
                            st.success(f"Updated {data['name']}")
                            st.rerun()
                        elif new_quantity == 0:
                            st.warning(f"Quantity cannot be 0. Use remove button to delete ingredient.")
                
                with col4:
                    # Remove button
                    if st.button("❌", key=f"remove_{cell}_{i}", help="Remove ingredient"):
                        del st.session_state.ingredient_list[cell]
                        st.rerun()
        
        # Bulk update and clear buttons
        col_update, col_clear = st.columns([1, 1])
        with col_update:
            if st.button("Update All", type="primary"):
                changes_made = False
                for cell, new_qty in updated_ingredients.items():
                    if cell in st.session_state.ingredient_list and new_qty > 0:
                        if st.session_state.ingredient_list[cell]['quantity'] != new_qty:
                            st.session_state.ingredient_list[cell]['quantity'] = new_qty
                            changes_made = True
                        elif new_qty == 0:
                            st.warning(f"Skipped {st.session_state.ingredient_list[cell]['name']} - quantity cannot be 0")
                
                if changes_made:
                    st.success("All quantities updated!")
                    st.rerun()
                else:
                    st.info("No changes detected")
        
        with col_clear:
            if st.button("Clear All", type="secondary"):
                st.session_state.ingredient_list = {}
                st.rerun()
    else:
        st.info("No ingredients added yet. Select ingredients from the dropdown above.")

# Right column - Results section
with right_col:
    st.markdown('<h3 class="section-header">📊 Calculation Results</h3>', unsafe_allow_html=True)
    
    # Calculate button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        calculate_button = st.button("🔍 Calculate", type="primary", use_container_width=True)
    
    # Create scrollable container for results
    with st.container(height=600):
        if calculate_button and st.session_state.ingredient_list:
            # Update computed_cache with ingredient list values
            for cell in prompt_cells:
                if cell in st.session_state.ingredient_list:
                    computed_cache[cell] = st.session_state.ingredient_list[cell]['quantity']
                else:
                    computed_cache[cell] = 0.0
            
            try:
                # Calculate all results
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
                    # "Cost per kg": calc_F20(),
                    # "Cost per Bag": calc_F21(),
                    # "Margin": calc_F22(),
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
                    "Choline (mg/kg)": calc_F38()
                }
                
                # Display results with better formatting
                significant_results = {k: v for k, v in results.items() if abs(v) > 0.0001}
                
                if significant_results:
                    for param, value in significant_results.items():
                        st.markdown(f'''
                        <div class="result-item">
                            <strong>{param}:</strong> {value:.4f}
                        </div>
                        ''', unsafe_allow_html=True)
                else:
                    st.warning("No significant results to display. Please add ingredients with quantities.")
                        
            except Exception as e:
                st.error(f"Error in calculation: {str(e)}")
                st.write("Please check your inputs and try again.")
        
        elif calculate_button and not st.session_state.ingredient_list:
            st.warning("⚠️ Please add some ingredients before calculating!")
        
        else:
            st.info("👆 Add ingredients from the left panel and click 'Calculate' to see results.")
            st.markdown("""
            **Instructions:**
            1. Select an ingredient from the dropdown
            2. Enter the quantity 
            3. Click 'Add' to add it to your formulation
            4. Edit quantities directly in the ingredient list
            5. Click 'Update' for individual changes or 'Update All' for bulk changes
            6. Click 'Calculate' to see nutritional analysis
            
            **Note:** All calculations are based on the nutritional database from your CSV file.
            """)

# Footer
st.markdown("---")
st.markdown("*Suryacore Feed Formulator - Professional Feed Formulation Tool*")
st.markdown('</div>', unsafe_allow_html=True)  # Close main-container
