
file_read = open('cme.20210709.c.pa2', 'r')
file_output = open("CL_expirations_and_settlements.txt", "w")


# Writing table column names
col1 = "Futures Code"
col2 = "Contract Month"
col3 = "Contract Type"
col4 = "Futures Exp Date"
col5 = "Options Code"
col6 = "Options Exp Date"

column_heads = f"{col1: <20} {col2: <20} {col3: <20} {col4: <20} {col5: <20} {col6: <20}\n"
column_space = f"{'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20}\n"
file_output.write(column_heads)
file_output.write(column_space)



exchanges = set()
for line in file_read:

    fields = line.split()
    record_type = fields[0].strip()

    if record_type == "B" and len(fields[1]) == 5 and fields[1] == "NYMCL":
        commodity_code = fields[1][-2:]
        contract_month = fields[2][3:]
        contract_month = contract_month[0:4] + "-" + contract_month[4:]
        product_type_code = fields[2][0:3]
        fut_exp_date = fields[3][-10:-2]
        fut_exp_date = fut_exp_date[:4] + "-" + fut_exp_date[4:6] + "-" + fut_exp_date[6:]
        exchanges.add(commodity_code)
        options_code = ''
        options_expirations_date = ''
        formatted_row = f"{commodity_code: <20} {contract_month: <20} {product_type_code.capitalize() : <20} {fut_exp_date: <20} {options_code: <20} {options_expirations_date: <20}\n"
        file_output.write(formatted_row)

    if record_type == "B" and len(fields[1]) == 5 and fields[1] == "NYMLO":
        commodity_code = fields[4][-2:] #CL
        contract_month = fields[2][3:]
        contract_month = contract_month[0:4] + "-" + contract_month[4:]
        product_type_code = "Opt"
        fut_exp_date = ''
        options_expirations_date = fields[4][-10:-2]
        options_code = 'LO'


        formatted_row = f"{commodity_code: <20} {contract_month: <20} {product_type_code.capitalize() : <20} {fut_exp_date: <20} {options_code: <20} {options_expirations_date: <20}\n"
        file_output.write(formatted_row)




    # if record_type == "81":
    #     print(line)
    #     break

# print(exchanges)