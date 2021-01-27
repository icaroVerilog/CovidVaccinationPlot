import pandas as pd
import numpy as NP
import seaborn as sns
import matplotlib.pyplot as plt

Dataset = pd.read_csv("country_vaccinations.csv")

def RegionDataframe(dataframe, countryRegion):
    
    if countryRegion == "america":
        countriesNames = ["Argentina", "Brazil", "Canada", "Chile", "Costa Rica", "Mexico", "United States"]
    
    elif countryRegion == "west-europe":
        countriesNames = ["Austria", "Belgium", "Denmark", "Finland", "France", "Germany", "Gibraltar", "Iceland", "Ireland", "Italy", "Luxembourg", "Malta", "Netherlands", "Norway", "Portugal", "Spain", "Sweden", "Switzerland", "United Kingdom"]

    elif countryRegion == "east-europe":
        countriesNames = ["Bulgaria", "Croatia", "Czechia", "Estonia", "Greece", "Hungary", "Latvia", "Lithuania", "Poland", "Romania", "Russia", "Serbia", "Slovakia", "Slovenia"]
        
    elif countryRegion == "middle-east":
        countriesNames = ["Bahrain", "Cyprus", "Israel", "Kwait", "Oman", "Saudi Arabia", "Turkey", "United Arab Emirates"]
        
    elif countryRegion == "asia":
        countriesNames = ["China", "India", "Singapore"]
    
    newDataframe = pd.DataFrame()
    
    for country in countriesNames:
        print(country)
        newDataframe[country] = dataframe[country]
        
    return newDataframe

def RenameColumns(database, names):
    newNames = []
    
    for name in names:
        newNames.append(name)

    database.columns = newNames
    

def GetCoutriesList(database):
    
    
    
    untratedCountries = database.iloc[:, 0].values
    countries = []
    
    for index in untratedCountries:
        if (index not in countries):
            countries.append(index)
            
    return NP.array(countries)
def DataCluster(database, country):
    
    vaccinatedDaily = []
    vaccinatedDailyDATE = []
    
    for i in range(1266):
        if (database["country"][i] == country):
            totalVaccinated = database["people_vaccinated_per_hundred"][i]
            vaccine = database["vaccines"][i]
            
            if (NP.isnan(database["daily_vaccinations"][i]) == False):    
                vaccinatedDaily.append(database["daily_vaccinations"][i])
                vaccinatedDailyDATE.append(database["date"][i])
    
    return totalVaccinated, vaccinatedDaily, vaccinatedDailyDATE, vaccine

def PlotPreprocessing(data, data2):
    
    vaccinatedDaily = []
    vaccinatedDailyDATE = []
    newColumnValue = []
    
    for index in range(len(data)):
        vaccinatedDaily.append(data[index][1])
        vaccinatedDailyDATE.append(data[index][2])
        
    dataframe1 = pd.DataFrame(vaccinatedDaily)
    dataframe2 = pd.DataFrame(vaccinatedDailyDATE)

    # Transpondo linhas e colunas para melhor manuseio    
    dataframe1 = dataframe1.transpose()    
    
    # Adicionando coluna indexadora
    for index2 in range(len(dataframe1.index)):
        newColumnValue.append(index2 + 1)
    
    RenameColumns(dataframe1, countriesList)

    # Separando em regiões
    
    americaDataframe = RegionDataframe(dataframe1, "america")
    eastEuropeDataframe = RegionDataframe(dataframe1, "east-europe")
    westEuropeDataframe = RegionDataframe(dataframe1, "west-europe")
    asiaDataframe = RegionDataframe(dataframe1, "asia")
    middEastDataframe = RegionDataframe(dataframe1, "middle-east")
    

    
    dataframe1["x"] = newColumnValue
    new = dataframe1.iloc[:, 54:58]


    # Plotando os graficos
    plt.style.use('seaborn-darkgrid')
    palette = plt.get_cmap('Set1')
    colorNum = 0
    
    """
    for column in dataframe1.drop("x", axis = 1):
        collorNum = collorNum + 1
        plt.plot(dataframe1['x'], dataframe1[column], marker='', linewidth=1, alpha=0.9, label=column)
    """
    
    for column in new.drop("x", axis = 1):
        colorNum = colorNum + 1
        plt.plot(new['x'], new[column], marker='o', linewidth=1, alpha=0.9, label=column, color = palette(colorNum))
 
    plt.legend(loc=2, ncol=2)
    plt.title("Vacinação diária covid-19", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Dias")
    plt.ylabel("Total vacinado")
    plt.show()

    return dataframe1, dataframe2, new, americaDataframe
countriesList = GetCoutriesList(Dataset)

dataByCountry = []

for i in range(len(countriesList)):
    dataByCountry.append(DataCluster(Dataset, countriesList[i]))
    
aaa, aa, a , america = PlotPreprocessing(dataByCountry, countriesList)


