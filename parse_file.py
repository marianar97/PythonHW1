
file_read = open('cme.20210709.c.pa2', 'r')
file_output = open("CL_expirations_and_settlements.txt", "w")


# Defining table1 column names
col1 = "Futures Code"
col2 = "Contract Month"
col3 = "Contract Type"
col4 = "Futures Exp Date"
col5 = "Options Code"
col6 = "Options Exp Date"

# Defining table2 column names
t2_col1 = "Futures Code"
t2_col2 = "Contract Month"
t2_col3 = "Contract Type"
t2_col4 = "Strike Price"
t2_col5 = "Settlement Price"


column_heads = f"{col1: <20} {col2: <20} {col3: <20} {col4: <20} {col5: <20} {col6: <20}\n"
column_space = f"{'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20}\n"
file_output.write(column_heads)
file_output.write(column_space)

records = set()
types = set()
record_81 = False
i = 0
for line in file_read:
    # print(line)
    # break

    fields = line.split()

    record_type = fields[0].strip()

    if record_type == "B" and len(fields[1]) == 5 and fields[1] == "NYMCL":
        commodity_code = fields[1][-2:]
        product_type_code = fields[2][0:3]
        fut_exp_date = fields[3][-10:-2]
        fut_exp_date = fut_exp_date[:4] + "-" + fut_exp_date[4:6] + "-" + fut_exp_date[6:]
        options_code = ''
        options_expirations_date = ''


    if record_type == "B" and len(fields[1]) == 5 and fields[1] == "NYMLO":
        commodity_code = fields[4][-2:] #CL
        # product_type_code = "Opt"
        fut_exp_date = ''
        options_expirations_date = fields[4][-10:-2]
        options_code = 'LO'


    if record_type == "B" and len(fields[1]) == 5 and (fields[1] == "NYMLO" or fields[1] == "NYMCL"):
        contract_month = fields[2][3:]
        contract_month = contract_month[0:4] + "-" + contract_month[4:]
        formatted_row = f"{commodity_code: <20} {contract_month: <20} {product_type_code.capitalize() : <20} {fut_exp_date: <20} {options_code: <20} {options_expirations_date: <20}\n"
        file_output.write(formatted_row)


    if record_type[0:5] == "81NYM" and not record_81:
        record_81 = True
        c4 = f"{t2_col1: <20} {t2_col2: <20} {t2_col3: <20} {t2_col4: <20} {t2_col5: <20}\n"
        c5 = f"{'-' * 15: <20} {'-' * 15: <20} {'-' * 15: <20} {'-' * 15: <20} {'-' * 15: <20} \n"
        file_output.write(c4)
        file_output.write(c5)

    if record_type[0:7] == "81NYMCL" and fields[1] =="CL":
        types.add(record_type)
        commodity_code = fields[1]
        contract_month = fields[3]
        contract_month = contract_month[0:4] + "-" + contract_month[4:]
        product_type_code = fields[2].capitalize()
        setl_price = int(fields[4].split('+')[-1][0:-1]) / 100
        strike_price = ''


        formatted_row = f"{commodity_code: <20} {contract_month: <20} {product_type_code.capitalize() : <20} {strike_price: <20} {setl_price: <20}\n"
        file_output.write(formatted_row)




# print(types)