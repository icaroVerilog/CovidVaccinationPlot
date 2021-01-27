import pandas as pd
import numpy as NP
import seaborn as sns
import matplotlib.pyplot as plt

Dataset = pd.read_csv("country_vaccinations.csv")

def PlotLine(dataframe):
    
    # Plotando os graficos
    plt.style.use('seaborn-darkgrid')
    
    for column in dataframe.drop("indexColumn", axis = 1):
        plt.plot(dataframe["indexColumn"], dataframe[column], marker='', linewidth=1, alpha=0.9, label=column)
 
    plt.legend(loc=2, ncol=2)
    plt.title("Vacinação diária covid-19", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Dias")
    plt.ylabel("Total vacinado")
    plt.show()

def PlotBar(dataframe):
    
    
    heights = []
    
    barName = ["Sputnik V", "Pfizer/BioNTech", "Pfizer/BioNTech, Sinopharm",
               "Sinovac", "Moderna, Pfizer/BioNTech", "CNBG, Sinovac",
               "Oxford/AstraZeneca, Pfizer/BioNTech", "Covaxin, Covishield", 
               "Sinopharm"]
    
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    F = 0
    G = 0
    H = 0
    I = 0
    
    for index in range(len(dataframe)):
        if dataframe[0][index] == "Sputnik V":
            A = A + 1
        if dataframe[0][index] == "Pfizer/BioNTech":
            B = B + 1
        if dataframe[0][index] == "Pfizer/BioNTech, Sinopharm":
            C = C + 1
        if dataframe[0][index] == "Sinovac":
            D = D + 1
        if dataframe[0][index] == "Moderna, Pfizer/BioNTech":
            E = E + 1
        if dataframe[0][index] == "CNBG, Sinovac":
            F = F + 1
        if dataframe[0][index] == "Oxford/AstraZeneca, Pfizer/BioNTech":
            G = G + 1
        if dataframe[0][index] == "Covaxin, Covishield":
            H = H + 1
        if dataframe[0][index] == "Sinopharm":
            I = I + 1

    heights.append(A)
    heights.append(B)
    heights.append(C)
    heights.append(D)
    heights.append(E)
    heights.append(F)
    heights.append(G)
    heights.append(H)
    heights.append(I)
    
    y_pos = NP.arange(len(barName))
    plt.style.use('seaborn-darkgrid')
    plt.bar(y_pos, heights)
    
    # Rotacionando os nomes das barras para melhor visualização
    plt.xticks(y_pos, barName, rotation = 90, color = "orange")
    plt.yticks(color='orange')
    plt.subplots_adjust(bottom = 0.4, top = 0.99)
    plt.show()
        

def RegionDataframe(dataframe, countryRegion):
    
    if countryRegion == "america":
        countriesNames = ["Argentina", "Brazil", "Canada", "Chile", "Costa Rica", "Mexico", "United States"]
    
    elif countryRegion == "west-europe":
        countriesNames = ["Austria", "Belgium", "Denmark", "Finland", "France", "Germany", "Gibraltar", "Iceland", "Ireland", "Italy", "Luxembourg", "Malta", "Netherlands", "Norway", "Portugal", "Spain", "Sweden", "Switzerland", "United Kingdom"]

    elif countryRegion == "east-europe":
        countriesNames = ["Bulgaria", "Croatia", "Czechia", "Estonia", "Greece", "Hungary", "Latvia", "Lithuania", "Poland", "Romania", "Serbia", "Slovakia", "Slovenia"]
        
    elif countryRegion == "middle-east":
        countriesNames = ["Bahrain", "Cyprus", "Israel", "Kuwait", "Oman", "Saudi Arabia", "United Arab Emirates"]
        
    elif countryRegion == "asia":
        countriesNames = ["China", "India"]
    
    newDataframe = pd.DataFrame()
    
    for country in countriesNames:
        #print(country)
        newDataframe[country] = dataframe[country]
        
    # Adicionando coluna indexadora
    
    newColumnValues = []
    
    for index in range(len(newDataframe.index)):
        newColumnValues.append(index + 1)
        
    newDataframe["indexColumn"] = newColumnValues
        
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
    vaccines = []
    
    for index in range(len(data)):
        vaccinatedDaily.append(data[index][1])
        vaccinatedDailyDATE.append(data[index][2])
        vaccines.append(data[index][3])

    dataframe1 = pd.DataFrame(vaccinatedDaily)
    dataframe2 = pd.DataFrame(vaccinatedDailyDATE)
    dataframe3 = pd.DataFrame(vaccines)

    # Transpondo linhas e colunas para melhor manuseio    
    dataframe1 = dataframe1.transpose()
    
    
    
    RenameColumns(dataframe1, countriesList)

    # Separando em regiões
    
    americaDataframe = RegionDataframe(dataframe1, "america")
    eastEuropeDataframe = RegionDataframe(dataframe1, "east-europe")
    westEuropeDataframe = RegionDataframe(dataframe1, "west-europe")
    asiaDataframe = RegionDataframe(dataframe1, "asia")
    middleEastDataframe = RegionDataframe(dataframe1, "middle-east")
    """
    PlotLine(americaDataframe)
    PlotLine(eastEuropeDataframe)
    PlotLine(westEuropeDataframe)
    PlotLine(asiaDataframe)
    PlotLine(middleEastDataframe)
    """
    PlotBar(dataframe3)

    return dataframe1, dataframe2, dataframe3
countriesList = GetCoutriesList(Dataset)

dataByCountry = []

for i in range(len(countriesList)):
    dataByCountry.append(DataCluster(Dataset, countriesList[i]))
    
dataframe1, dataframe2, dataframe3 = PlotPreprocessing(dataByCountry, countriesList)


