![stock image](https://github.com/RyansStacks/Emergency-Department-Tableau-Dashboard/blob/main/img/stock.png)

# Aegis Healthcare Enterprise Dashboards

## Background
A client has requested that an operational dashboard be created from data from 2022 to present. The dashboard will be used to monitor key metrics in the busy Emergency Department that the client wants to monitor. All the requirements and necessary metrics have been provided by the client and may be found in the dictionary created in response:

[Project Data Dictionary](https://github.com/RyansStacks/Emergency-Department-Tableau-Dashboard/blob/main/metadata/Aegis%20Healthcare%20Enterprise%20Dashboards%20Dictionary.xlsx)

The dashboard shold answer key business problems specific to the Emergency Department:
1. Are specific populations vulnerable?
2. Are wait times associated with any phenomena?
3. Are there any referrals to other medical care from the Emergency Department with significant numbers?
4. Is there any association between patient severity measured by the 'APACHE II Scoring metric' to other attributes?

A follow-up will be performed by a data analyst to build models for each of the questions above if phenomena are noted in the Tableau dashboard. The dashboard will also serve to monitor events on-going to provide swift response by leadership.

## Data

### Data Source

Data for the project due to privacy issues involving healthcare data has been completely fabricated using Python with some post manipulaiton to inject bias to create trends in the Tableau visualizations. The process of both creating the data as well as emulating trending has been a heuristic experience as one truly starts to know the data when creating it.

The following Python script may be used to create the tables needed for the project. Note, one may easily upload into SQL using a GUI based platform such as SSMS that allows automatic table/column creation with .csv files.

#### The following Python file may be used to create data:
[Python Raw Data Script](https://github.com/RyansStacks/Emergency-Department-Tableau-Dashboard/blob/main/src/Data.py )

#### ER Diagram
The ER Diagram below shows all columns within each of the tables used in the creation of the dashboard. Linkage between Primary - Foreign Keys are given by arrows. Again, the tables may be easily uploaded to SQL Server using the GUI or scripting with SQL Server easily connected to Tableau via Tableau's SQL Server driver (simply login to SQL Server in Tableau).

![ER Diagram](https://github.com/RyansStacks/Emergency-Department-Tableau-Dashboard/blob/main/img/ED%20Data%20Model.png)


#### Using Python Pandas to Create Data

D:\Projects\Aegis Healthcare Enterprise Dashboards\src\data.py

## Tableau Dashboard

All the .csv files are combined using Tableau relationships (very similar to SQL joins) with ED Visits serving as the Parent Table:

<img src= https://github.com/RyansStacks/Emergency-Department-Tableau-Dashboard/blob/main/img/Tableau%20Data%20Model.png width="1000"/>


The final product is a Dashboard that staff and leadership may use to confirm trends. Below, we discuss some findings from the Tableau excerpt.



![Tableau Dashboard](https://github.com/RyansStacks/Emergency-Department-Tableau-Dashboard/blob/main/img/ED%20Operations.png)


### Dashboard Summary

##### 1. Average Wait Time Correlate with Poorer Patient Surveys

##### 2. APACHE II (patient severity) Typically Corresponds to Homelessness and Older Populations

##### 3. Addiction Medicine Referrals from ED are Signficantly Higher Compared to Other Hospitals (Benchmarks)

##### 4. Wait Times are Very High on Weekends and in Summer

##### 5. The Emergency Department Serves a Typical Demographics Minus a More Older Population with Median Age of 44

A link to the Dashboard on Tableau Public may be found:

![Tableau Public - See Dashboard](https://public.tableau.com/app/profile/ryan.breen8189/viz/AegisHealthcareEnterpriseEDDashboard/EDOperations?publish=yes)
