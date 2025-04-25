# %%
# =============================================================================
# this is exmaple of assignment
# =============================================================================


a = 1
a

b = 2


c = 3


# %%
# =============================================================================
# data concatenation
# =============================================================================
import pandas as pd

df1 = pd.read_csv('https://bcdanl.github.io/data/concat_1.csv')
df2 = pd.read_csv('https://bcdanl.github.io/data/concat_2.csv')
df3 = pd.read_csv('https://bcdanl.github.io/data/concat_3.csv')


# this is comment




# %%
# =============================================================================
# pd.read_html()
# =============================================================================
import pandas as pd
url = "https://www.nps.gov/orgs/1207/national-park-visitation-sets-new-record-as-economic-engines.htm"

tables = pd.read_html(url)
len(tables)

tables[0]

tables[1]



df1 = tables[0]
df2 = tables[1]

df1.iloc[0]
df1.iloc[0,]

df1.columns = df1.iloc[0]

df1[1:]
df1.iloc[1:]


df1 = df1[1:]
df1.info()

df1 = df1.reset_index()


tables = pd.read_html(url)

df1_dropTrue = df1.reset_index(drop=True)
df1_dropTrue


# %%
# =============================================================================
# complete code
# =============================================================================
import pandas as pd
url = "https://www.nps.gov/orgs/1207/national-park-visitation-sets-new-record-as-economic-engines.htm"

tables = pd.read_html(url)
len(tables)
df_0 = tables[0]
df_0.columns = df_0.iloc[0]  # Set the first row as column names
df_0 = df_0[1:].reset_index(drop = True)  # Remove the first row & reset index


