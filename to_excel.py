import pandas as pd
import numpy as np
import openpyxl
import xlsxwriter




def def_init_excel(recon_date, duplicated_cpns, uncleared_cpns):
    pathway = fr'C:\Users\matthewray\OneDrive - Clearwater\Desktop\Python\PayPal - Duplicated Coupon\Output\coupon_check_{recon_date}.xlsx'
    
    try:
        with pd.ExcelWriter(pathway, engine='openpyxl', mode='w') as writer:
            duplicated_cpns.to_excel(writer, sheet_name='Duplicated Coupons', index=False)
            uncleared_cpns.to_excel(writer, sheet_name='Uncleared CPNs', index=False)

            # Adjust column widths
            for sheet_name in writer.sheets:
                worksheet = writer.sheets[sheet_name]
                for column_cells in worksheet.columns:
                    max_length = 0
                    column = column_cells[0].column_letter
                    for cell in column_cells:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(cell.value)
                        except Exception as e:
                            print(f"Non Fatal - Error processing cell {cell}: {e}")
                    adjusted_width = (max_length + 6)
                    worksheet.column_dimensions[column].width = adjusted_width

        print("Python: Executed successfully. Output file created")
    except Exception as e:
        print(f"An error occurred: {e}")
