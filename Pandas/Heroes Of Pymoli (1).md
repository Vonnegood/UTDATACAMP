
# Heroes of Pymoli


```python
import pandas as pd
import os

filepath=os.path.join("HeroesOfPymoli","purchase_data.json")
Original = pd.read_json(filepath)
Original.head()
#Original.count() Just checked that there weren't null values
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count


```python
players = len(Original["SN"].unique())

Summary = pd.DataFrame({"Total Player": [players]} )
Summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Player</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)

#### Number of Unique Items


```python
unique_items = len(Original["Item ID"].unique())
avg_price= round(Original["Price"].mean(),2)
purchases = Original["Item Name"].count()
total_rev = Original["Price"].sum()

Summary = pd.DataFrame({"Number of Unique Items": [unique_items], 
                        "Average Price": [avg_price],
                        "Number of Purchases": [purchases],
                        "Total Revenue": [total_rev]})

Summary["Average Price"] =Summary["Average Price"].map("${:,.2f}".format)
Summary["Total Revenue"] = Summary["Total Revenue"].map("${:,.2f}".format)

Summary = Summary[["Number of Unique Items","Average Price","Number of Purchases","Total Revenue"]]
Summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# create a table with totals for unique players
unique = Original.drop_duplicates(subset="SN")
```

## Gender Demographics


```python
genders = pd.DataFrame()
genders["Total Count"] = unique.groupby("Gender")["Price"].count()
genders["Percentage of Players"] = round(genders["Total Count"] / genders["Total Count"].sum() * 100,2)

genders = genders[["Percentage of Players","Total Count"]]
genders = genders.sort_values(by="Total Count", ascending=False)
genders
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
# # I did this and it works, but the previous input is much more concise.

# gender_counts = []
# gender_percent = []
# genders = Original["Gender"].unique()

# for gender in genders:
#     gender_df = Original[Original["Gender"]== gender]
#     gender_counts.append(len(gender_df["SN"].unique()))
#     gender_percent.append(round(len(gender_df["SN"].unique()) / players * 100,2))

# print(gender_counts)
# print(gender_percent)

# gender_demo_df = pd.DataFrame({"Genders": genders, "Percentage of Players": gender_percent, "Total Count": gender_counts})
# gender_demo_df
```

## Purchasing Analysis (Gender)

### Male


```python
gender_purchase = pd.DataFrame()
gender_purchase["Purchase Count"] = Original.groupby("Gender")["Price"].count()
gender_purchase["Average Purchase Price"] = Original.groupby("Gender")["Price"].mean()
gender_purchase["Total Purchase Value"] = Original.groupby("Gender")["Price"].sum()
gender_purchase["Normalized Totals"] = gender_purchase["Total Purchase Value"] / unique.groupby("Gender")["Price"].count()

gender_purchase["Average Purchase Price"] = gender_purchase["Average Purchase Price"].map("${:,.2f}".format)
gender_purchase["Total Purchase Value"] = gender_purchase["Total Purchase Value"].map("${:,.2f}".format)
gender_purchase["Normalized Totals"] = gender_purchase["Normalized Totals"].map("${:,.2f}".format)

gender_purchase
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics


```python
bins = [0,9,14,19,24,29,34,39,999]
labels = ["<10","10-14","15-19","20-24","25-29","30-34","35-29","40+"]
Original["Age Group"] = pd.cut(Original["Age"], bins, labels= labels)
unique = Original.drop_duplicates(subset="SN")

age_groups = pd.DataFrame()
age_groups["Total Count"] = unique.groupby("Age Group")["Age"].count()
age_groups["Percentage of Players"] = round(100 * age_groups["Total Count"] / age_groups["Total Count"].sum(),2)

age_groups = age_groups[["Percentage of Players","Total Count"]]
age_groups
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.32</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.01</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.20</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.18</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.20</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-29</th>
      <td>4.71</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.92</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Age)


```python
age_purchase = pd.DataFrame()
age_purchase["Purchase Count"] = Original.groupby("Age Group")["Price"].count()
age_purchase["Average Purchase Price"] = Original.groupby("Age Group")["Price"].mean()
age_purchase["Total Purchase Value"] = Original.groupby("Age Group")["Price"].sum()
age_purchase["Normalized Totals"] = age_purchase["Total Purchase Value"] / unique.groupby("Age Group")["Price"].count()

age_purchase["Average Purchase Price"] = age_purchase["Average Purchase Price"].map("${:,.2f}".format)
age_purchase["Total Purchase Value"] = age_purchase["Total Purchase Value"].map("${:,.2f}".format)
age_purchase["Normalized Totals"] = age_purchase["Normalized Totals"].map("${:,.2f}".format)

age_purchase
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$4.20</td>
    </tr>
    <tr>
      <th>35-29</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$4.42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$4.89</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders


```python
spenders = pd.DataFrame()
spenders["Purchase Count"] = Original.groupby("SN")["Price"].count()
spenders["Average Purchase Price"] = Original.groupby("SN")["Price"].mean()
spenders["Total Purchase Value"] = Original.groupby("SN")["Price"].sum()
sorted_spenders = spenders.sort_values(by="Total Purchase Value", ascending=False)

sorted_spenders["Average Purchase Price"] = sorted_spenders["Average Purchase Price"].map("${:,.2f}".format)
sorted_spenders["Total Purchase Value"] = sorted_spenders["Total Purchase Value"].map("${:,.2f}".format)

sorted_spenders.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <th>Male</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <th>Male</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <th>Female</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <th>Male</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <th>Male</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Items


```python
items = pd.DataFrame()
items["Purchase Count"] = Original.groupby(["Item ID","Item Name"])["Price"].count()
items["Total Purchase Value"] = Original.groupby(["Item ID","Item Name"])["Price"].sum()
items["Item Price"] = items["Total Purchase Value"] / items["Purchase Count"]

pop_items = items.sort_values(by="Purchase Count",ascending=False)

pop_items["Total Purchase Value"] = pop_items["Total Purchase Value"].map("${:,.2f}".format)
pop_items["Item Price"] = pop_items["Item Price"].map("${:,.2f}".format)

pop_items = items.sort_values(by="Purchase Count",ascending=False)
pop_items = pop_items[["Purchase Count","Item Price", "Total Purchase Value"]]
pop_items.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>



## Most Profitable Items


```python
profit_items = items.sort_values(by="Total Purchase Value",ascending=False)

profit_items["Total Purchase Value"] = profit_items["Total Purchase Value"].map("${:,.2f}".format)
profit_items["Item Price"] = profit_items["Item Price"].map("${:,.2f}".format)

profit_items = profit_items[["Purchase Count","Item Price","Total Purchase Value"]]
profit_items.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Just some fun to see what brought the Other / non-disclosed avg purchase price up
Other = Original[Original["Gender"] =="Other / Non-Disclosed"]
Other_items = Other.groupby(["Item ID","Item Name"])["Price"].agg({"Total Revenue": sum})
Other_items.sort_values(by="Total Revenue", ascending=False)
```

    C:\Users\Chris\AppData\Local\conda\conda\envs\PythonData\lib\site-packages\ipykernel\__main__.py:3: FutureWarning: using a dict on a Series for aggregation
    is deprecated and will be removed in a future version
      app.launch_new_instance()
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Total Revenue</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>48</th>
      <th>Rage, Legacy of the Lone Victor</th>
      <td>4.32</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>4.25</td>
    </tr>
    <tr>
      <th>128</th>
      <th>Blazeguard, Reach of Eternity</th>
      <td>4.00</td>
    </tr>
    <tr>
      <th>61</th>
      <th>Ragnarok</th>
      <td>3.97</td>
    </tr>
    <tr>
      <th>29</th>
      <th>Chaos, Ender of the End</th>
      <td>3.79</td>
    </tr>
    <tr>
      <th>155</th>
      <th>War-Forged Gold Deflector</th>
      <td>3.73</td>
    </tr>
    <tr>
      <th>141</th>
      <th>Persuasion</th>
      <td>3.27</td>
    </tr>
    <tr>
      <th>183</th>
      <th>Dragon's Greatsword</th>
      <td>2.36</td>
    </tr>
    <tr>
      <th>157</th>
      <th>Spada, Etcher of Hatred</th>
      <td>2.21</td>
    </tr>
    <tr>
      <th>65</th>
      <th>Conqueror Adamantite Mace</th>
      <td>1.96</td>
    </tr>
    <tr>
      <th>179</th>
      <th>Wolf, Promise of the Moonwalker</th>
      <td>1.88</td>
    </tr>
  </tbody>
</table>
</div>


