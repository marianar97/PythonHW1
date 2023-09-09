
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
column_space = f"{'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20} {'-'*15: <20} "
file_output.write(column_heads)
file_output.write(column_space)


exchanges = set()
for line in file_read:

    fields = line.split()

    if fields[0].strip() == "B" and fields[1][0:5] == "NYMLO" or fields[1][0:5] == "NYMCL" :
        print(line)
        exchanges.add(fields[1][0:5])

print(exchanges)

