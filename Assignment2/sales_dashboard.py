import pandas as pd
import time
import gdown
import sys

required_fields = ['sales_region', 'employee_name', 'produce_name', 'customer_name',
                   'quantity', 'unit_price', 'order_date', 'order_type', 'customer_state',
                   'customer_type', 'product_category']

df = None

def load_sales_data():
    # Load and validate the sales dataset, exit on failure. Ensures required columns exist before continuing.
    # Defensive programming: Check internet access and data validity before proceeding
    global df
    file_id = "1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
    url = f"https://drive.google.com/uc?id={file_id}"
    output_file = "sales_data.csv"

    print("Loading sales data, please wait...")
    start_time = time.time()
    try:
        gdown.download(url, output_file, quiet=False)
        assert output_file.endswith('.csv'), "Downloaded file is not a CSV"
        df = pd.read_csv(output_file)
    except Exception as e:
        print("Failed to load sales data.")
        print(f"Error: {e}")
        sys.exit(1)

    df.fillna(0, inplace=True)
    end_time = time.time()
    load_time = end_time - start_time

    print("Sales data loaded successfully.")
    print(f"Load time: {load_time:.2f} seconds")
    print(f"Number of rows: {len(df)}")
    print(f"Available columns: {list(df.columns)}")

    missing_fields = [field for field in required_fields if field not in df.columns]
    if missing_fields:
        print("Warning: Missing fields:", missing_fields)
    else:
        print("All required fields are present.")

def export_to_excel(df_result):
    # Optionally export any pivot table result to an Excel file with basic filename validation.
    export = input("Would you like to export the results to an Excel file? (y/n): ").strip().lower()
    if export == 'y':
        filename = input("Enter filename (without extension): ").strip()
        if filename and all(c not in filename for c in r'<>:"/\|?*'):
            df_result.to_excel(f"{filename}.xlsx")
            print(f"Results exported to {filename}.xlsx")
        else:
            print("No filename provided. Export cancelled.")

def fill_with_mean(df_result):
    # Replace missing (NaN) numeric values with the column mean to preserve valid averages.
    return df_result.fillna(df_result.mean(numeric_only=True))

def show_first_n_rows():
    print(f"\nThere are {len(df)} rows available.")
    choice = input("Enter rows to display:\n- Enter a number 1 to {0}\n- To see all rows, enter 'all'\n- To skip preview, press Enter\nYour choice: ".format(len(df))).strip().lower()
    if choice == 'all':
        print(df)
    elif choice.isdigit():
        n = int(choice)
        if 1 <= n <= len(df):
            print(df.head(n))
        else:
            print("Invalid number. Must be between 1 and", len(df))
    elif choice == '':
        print("Skipped preview.")
    else:
        print("Invalid input.")

def total_sales_by_region_and_order_type():
    df['total_price'] = df['quantity'] * df['unit_price']
    result = df.pivot_table(index='sales_region', columns='order_type', values='total_price', aggfunc='sum')
    result = fill_with_mean(result)
    print(result)
    export_to_excel(result)
    return result

def average_sales_by_region_state_type():
    df['total_price'] = df['quantity'] * df['unit_price']
    result = df.pivot_table(index=['sales_region', 'customer_state'], columns='order_type', values='total_price', aggfunc='mean')
    result = fill_with_mean(result)
    print(result)
    export_to_excel(result)
    return result

def sales_by_customer_and_order_by_state():
    df['total_price'] = df['quantity'] * df['unit_price']
    result = df.pivot_table(index='customer_state', columns=['customer_type', 'order_type'], values='total_price', aggfunc='sum')
    result = fill_with_mean(result)
    print(result)
    export_to_excel(result)
    return result

def total_quantity_price_by_region_product():
    df['total_price'] = df['quantity'] * df['unit_price']
    result = df.pivot_table(index='sales_region', columns='produce_name', values=['quantity', 'total_price'], aggfunc='sum')
    result = fill_with_mean(result)
    print(result)
    export_to_excel(result)
    return result

def total_quantity_price_by_customer_type():
    df['total_price'] = df['quantity'] * df['unit_price']
    result = df.pivot_table(index='customer_type', values=['quantity', 'total_price'], aggfunc='sum')
    result = fill_with_mean(result)
    print(result)
    export_to_excel(result)
    return result

def max_min_sales_by_category():
    df['total_price'] = df['quantity'] * df['unit_price']
    result = df.pivot_table(index='product_category', values='total_price', aggfunc=['max', 'min'])
    result = fill_with_mean(result)
    print(result)
    export_to_excel(result)
    return result

def unique_employees_by_region():
    result = df.pivot_table(index='sales_region', values='employee_name', aggfunc=pd.Series.nunique)
    result = fill_with_mean(result)
    print(result)
    export_to_excel(result)
    return result

def create_custom_pivot():
    # Custom Pivot Table Generator: users can define rows, columns, values, and aggregation logic interactively.
    #Used AI here to figure out how to create the custom pivot tables. Tweaked where needed. 
    df['total_price'] = df['quantity'] * df['unit_price']
    row_options = {"1": "employee_name", "2": "sales_region", "3": "product_category"}
    col_options = {"1": "order_type", "2": "customer_type"}
    val_options = {"1": "quantity", "2": "total_price"}
    agg_options = {"1": "sum", "2": "mean", "3": "count"}

    print("\nSelect rows:")
    for k, v in row_options.items():
        print(f"{k}. {v}")
    row_input = input("Enter the number(s) of your choice(s), separated by commas: ").split(',')
    rows = [row_options.get(i.strip()) for i in row_input if i.strip() in row_options]

    print("\nSelect columns (optional):")
    for k, v in col_options.items():
        print(f"{k}. {v}")
    col_input = input("Enter the number(s) of your choice(s), separated by commas (enter for no grouping): ").split(',')
    columns = [col_options.get(i.strip()) for i in col_input if i.strip() in col_options]

    print("\nSelect values:")
    for k, v in val_options.items():
        print(f"{k}. {v}")
    val_input = input("Enter the number(s) of your choice(s), separated by commas: ").split(',')
    values = [val_options.get(i.strip()) for i in val_input if i.strip() in val_options]

    print("\nSelect aggregation function:")
    for k, v in agg_options.items():
        print(f"{k}. {v}")
    agg_input = input("Enter the number of your choice: ").strip()
    if agg_input not in agg_options:
        print("Invalid aggregation choice. Defaulting to 'sum'.")
        agg_input = '1'
    aggfunc = agg_options.get(agg_input)

    try:
        pivot = df.pivot_table(index=rows, columns=columns if columns else None, values=values, aggfunc=aggfunc)
        pivot = fill_with_mean(pivot)
        print(pivot)
        export_to_excel(pivot)
        return pivot
    except Exception as e:
        print(f"Error creating pivot table: {e}")
        return None

def compare_two_analytics():
    # Let the user compare two separate analytics outputs side-by-side for analysis and insight.
    print("Select the first report to compare:")
    r1 = select_analytics()
    print("Select the second report to compare:")
    r2 = select_analytics()

    print("\n--- Comparison ---")
    print("\nFirst Result:")
    print(r1)
    print("\nSecond Result:")
    print(r2)

def select_analytics():
    # Validates menu input to prevent index errors and enhances usability
    options = list(menu_items.items())[:-2]  # Exclude custom pivot and exit
    for i, (label, _) in enumerate(options, 1):
        print(f"{i}. {label.split('. ', 1)[1]}")
    choice = int(input("Enter your choice: "))
    if 1 <= choice <= len(options):
        return list(menu_items.values())[choice - 1]()
    else:
        print("Invalid choice.")
        return None

def exit_program():
    print("Exiting dashboard. Goodbye!")
    exit()

menu_items = {
    "1. Show the first n rows of sales data": show_first_n_rows,
    "2. Total sales by region and order_type": total_sales_by_region_and_order_type,
    "3. Average sales by region with average sales by state and sale type": average_sales_by_region_state_type,
    "4. Sales by customer type and order type by state.": sales_by_customer_and_order_by_state,
    "5. Total sales quantity and price by region and product": total_quantity_price_by_region_product,
    "6. Total sales quantity and price by customer type": total_quantity_price_by_customer_type,
    "7. Max and min sales price of sales by category": max_min_sales_by_category,
    "8. Number of unique employees by region": unique_employees_by_region,
    "9. Create a custom pivot table": create_custom_pivot,
    "10. Compare two analytics side by side": compare_two_analytics,
    "11. Exit": exit_program
}

def display_menu():
    print("\n--- Sales Data Dashboard ---")
    for i, item in enumerate(menu_items.keys(), start=1):
        print(f"{i}. {item.split('. ', 1)[1]}")

def run_dashboard():
    # Runs the interactive dashboard loop, continually presenting the user with actionable options.
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-11): "))
            if 1 <= choice <= len(menu_items):
                list(menu_items.values())[choice - 1]()
            else:
                print("Invalid option. Please choose a number from the menu.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    load_sales_data()
    run_dashboard()