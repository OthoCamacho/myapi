from flask import Flask, jsonify, request
from pymongo import MongoClient

#import requests
#from requests.auth import HTTPDigestAuth
#from ipify import get_ip

app = Flask(__name__)

# Obtiene la dirección IP actual de PythonAnywhere utilizando ipify
#ip_address = get_ip()

# Credenciales de MongoDB Atlas (actualízalas con tus propias credenciales)
#atlas_group_id = "65ef6357bf977b393906cc5a"
#atlas_api_key_public = "NmEgS95bdbDW2b9AaBvsh28vhTdu2gvGmUc6i3fm"
#atlas_api_key_private = "Aib1vQfkLAo6wKI8aegAPd3jffRZWzivGUWEPrNHIghsSu54qSLeaTiXM9HQCo5d"

# MongoDB Connection
try:
    client = MongoClient('mongodb+srv://othocamacho:304179394@cluster0.e1y9uge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['master-data']
    coll = db['Montly_Electricity_2023']
    print("Conexión a MongoDB Atlas establecida con éxito")
except Exception as e:
    print(f"Error al conectar con MongoDB Atlas: {str(e)}")

#The Mogos's '_id' is a not JSON serializable. For that reason I need a helper function to handle the conversion and call it from each endpoint where is needed.

def convert_object_ids(data):
    for entry in data:
        entry['_id'] = str(entry['_id'])

# Helper function to convert MongoDB documents to dictionary
def mongo_to_dict(data):
    return [entry for entry in data]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#General Infomation
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#Endpoint to provide information about the API
@app.route('/', methods=['GET'])  #BASE URL for our API
def root():
    return "Welcome to 2023 Montly Eletricity Statitics. In this API you can consult montly electricity production and trade data for all OECD member countries."


#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#All data
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#Endpoint to fetch data from MongoDB
@app.route('/api/data', methods=['GET'])
def get_mongo_data():
    #Retrive data from MongoDB collection
    data = list(coll.find({})) #Fecht all documents from the collection

    #Convert ObjectId to string for JSON serialization
    convert_object_ids(data)
    
    #Return the datas as JSON
    return jsonify(data)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#List of countries
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#Endpoint displaying a list of countries which monthly electricity data is available for consultation
@app.route('/api/countries', methods=['GET'])
def get_countries_list():
    # Retrieve a list of unique countries from the MongoDB collection
    unique_countries = coll.distinct('Country')
    
    # Return the list of unique countries as JSON
    return jsonify(unique_countries)

#"Argentina",
    "Australia",
    "Austria",
    "Belgium",
    "Brazil",
    "Bulgaria",
    "Canada",
    "Chile",
    "Colombia",
    "Costa Rica",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "IEA Total",
    "Iceland",
    "India",
    "Ireland",
    "Italy",
    "Japan",
    "Korea",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Mexico",
    "Netherlands",
    "New Zealand",
    "North Macedonia",
    "Norway",
    "OECD Americas",
    "OECD Asia Oceania",
    "OECD Europe",
    "OECD Total",
    "People's Republic of China",
    "Peru",
    "Poland",
    "Portugal",
    "Republic of Turkiye",
    "Serbia",
    "Slovak Republic",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "United Kingdom",
    "United States"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# List of elements in the Balance column
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Endpoint displaying a list of elements for consultation in the column 'Balance'
@app.route('/api/balances', methods=['GET'])
def get_balances():
    # Retrieve a list of unique of elements from the 'Balance' collumn in the MongoDB collection for consultation
    unique_balance_elements = coll.distinct('Balance')
    
    # Return the list of unique countries as JSON
    return jsonify(unique_balance_elements)

#   "Distribution Losses",
    "Final Consumption (Calculated)",
    "Net Electricity Production",
    "Remarks",
    "Total Exports",
    "Total Imports",
    "Used for pumped storage"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# List of elements in the Product column
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Endpoint displaying a list of elements for consultation in the column 'Product'
@app.route('/api/products', methods=['GET'])
def get_products():
    # Retrieve a list of unique of elements from the 'Product' collumn in the MongoDB collection for consultation
    unique_product_elements = coll.distinct('Product')
    
    # Return the list of unique products as JSON
    return jsonify(unique_product_elements)

#"Coal, Peat and Manufactured Gases",
    "Combustible Renewables",
    "Data is estimated for this month",
    "Electricity",
    "Geothermal",
    "Hydro",
    "Natural Gas",
    "Not Specified",
    "Nuclear",
    "Oil and Petroleum Products",
    "Other Combustible Non-Renewables",
    "Other Renewables",
    "Solar",
    "Total Combustible Fuels",
    "Total Renewables (Hydro, Geo, Solar, Wind, Other)",
    "Wind"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# List of elements in the 'Time' product
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/api/dates', methods=['GET'])
def get_dates():
    # Retrieve a list of unique elements from the 'Time' column in the MongoDB collection for consultation
    unique_dates = coll.distinct('Time')

    # Parse the dates into datetime objects
    parsed_dates = [datetime.strptime(date, '%b-%y') for date in unique_dates]

    # Order the unique dates by year and month
    parsed_dates.sort()

    # Convert the sorted datetime objects back to the original format
    sorted_dates = [date.strftime('%b-%y') for date in parsed_dates]

    # Return the list of unique dates ordered by year and month as JSON
    return jsonify(sorted_dates)

 #"Jan-10",
    "Feb-10",
    "Mar-10",
    "Apr-10",
    "May-10",
    "Jun-10",
    "Jul-10",
    "Aug-10",
    "Sep-10",
    "Oct-10",
    "Nov-10",
    "Dec-10",
    "Jan-11",
    "Feb-11",
    "Mar-11",
    "Apr-11",
    "May-11",
    "Jun-11",
    "Jul-11",
    "Aug-11",
    "Sep-11",
    "Oct-11",
    "Nov-11",
    "Dec-11",
    "Jan-12",
    "Feb-12",
    "Mar-12",
    "Apr-12",
    "May-12",
    "Jun-12",
    "Jul-12",
    "Aug-12",
    "Sep-12",
    "Oct-12",
    "Nov-12",
    "Dec-12",
    "Jan-13",
    "Feb-13",
    "Mar-13",
    "Apr-13",
    "May-13",
    "Jun-13",
    "Jul-13",
    "Aug-13",
    "Sep-13",
    "Oct-13",
    "Nov-13",
    "Dec-13",
    "Jan-14",
    "Feb-14",
    "Mar-14",
    "Apr-14",
    "May-14",
    "Jun-14",
    "Jul-14",
    "Aug-14",
    "Sep-14",
    "Oct-14",
    "Nov-14",
    "Dec-14",
    "Jan-15",
    "Feb-15",
    "Mar-15",
    "Apr-15",
    "May-15",
    "Jun-15",
    "Jul-15",
    "Aug-15",
    "Sep-15",
    "Oct-15",
    "Nov-15",
    "Dec-15",
    "Jan-16",
    "Feb-16",
    "Mar-16",
    "Apr-16",
    "May-16",
    "Jun-16",
    "Jul-16",
    "Aug-16",
    "Sep-16",
    "Oct-16",
    "Nov-16",
    "Dec-16",
    "Jan-17",
    "Feb-17",
    "Mar-17",
    "Apr-17",
    "May-17",
    "Jun-17",
    "Jul-17",
    "Aug-17",
    "Sep-17",
    "Oct-17",
    "Nov-17",
    "Dec-17",
    "Jan-18",
    "Feb-18",
    "Mar-18",
    "Apr-18",
    "May-18",
    "Jun-18",
    "Jul-18",
    "Aug-18",
    "Sep-18",
    "Oct-18",
    "Nov-18",
    "Dec-18",
    "Jan-19",
    "Feb-19",
    "Mar-19",
    "Apr-19",
    "May-19",
    "Jun-19",
    "Jul-19",
    "Aug-19",
    "Sep-19",
    "Oct-19",
    "Nov-19",
    "Dec-19",
    "Jan-20",
    "Feb-20",
    "Mar-20",
    "Apr-20",
    "May-20",
    "Jun-20",
    "Jul-20",
    "Aug-20",
    "Sep-20",
    "Oct-20",
    "Nov-20",
    "Dec-20",
    "Jan-21",
    "Feb-21",
    "Mar-21",
    "Apr-21",
    "May-21",
    "Jun-21",
    "Jul-21",
    "Aug-21",
    "Sep-21",
    "Oct-21",
    "Nov-21",
    "Dec-21",
    "Jan-22",
    "Feb-22",
    "Mar-22",
    "Apr-22",
    "May-22",
    "Jun-22",
    "Jul-22",
    "Aug-22",
    "Sep-22",
    "Oct-22",
    "Nov-22",
    "Dec-22",
    "Jan-23",
    "Feb-23",
    "Mar-23",
    "Apr-23",
    "May-23",
    "Jun-23",
    "Jul-23",
    "Aug-23",
    "Sep-23",
    "Oct-23",
    "Nov-23",
    "Dec-23"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Electricity data for a specific country
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Endpoint to fetch monthly electricity data for a specific country
@app.route('/api/data/country', methods=['GET'])
def get_country_data():
    # Retrieve the country name from the query parameters
    country = request.args.get('country')
    
    # If country is not provided, return an error message
    if not country:
        return jsonify({'error': 'Country name not provided'}), 400

    # Retrieve data from MongoDB collection for the specified country
    data = list(coll.find({'Country': country}))

    # Convert ObjectId to string for JSON serialization
    convert_object_ids(data)

    # Sort the data by year
    data.sort(key=lambda x: datetime.strptime(x['Time'], '%b-%y'))

    return jsonify(data)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Intruction for the electricity data for a specifil country usun query parameters (Balance, Product, mont)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Define allowed products based on balance
allowed_products = {
    "Net Electricity Production": ["Electricity", "Total Combustible Fuels", "Coal Peat and Manufactured Gases", "Oil and Petroleum Products", "Natural Gas", 
                                    "Combustible Renewables", "Other Combustible Non-Renewables", "Hydro", "Wind", "Solar", "Geothermal", "Other Renewables", 
                                    "Total Renewables (Hydro, Geo, Solar, Wind, Other)", "Not specified", "Nuclear"],
    "Used for pumped storage": ["Electricity"],
    "Distribution Losses": ["Electricity"],
    "Total Exports": ["Electricity"],
    "Total Imports": ["Electricity"],
    "Final Consumption (Calculated)": ["Electricity"],
    "Remarks": ["Data is estimated for this month"]
}

# Define the list of balances
balances = list(allowed_products.keys())

# Define the list of countries
countries = [
    "Argentina",
    "Australia",
    "Austria",
    "Belgium",
    "Brazil",
    "Bulgaria",
    "Canada",
    "Chile",
    "Colombia",
    "Costa Rica",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "IEA Total",
    "Iceland",
    "India",
    "Ireland",
    "Italy",
    "Japan",
    "Korea",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Mexico",
    "Netherlands",
    "New Zealand",
    "North Macedonia",
    "Norway",
    "OECD Americas",
    "OECD Asia Oceania",
    "OECD Europe",
    "OECD Total",
    "People's Republic of China",
    "Peru",
    "Poland",
    "Portugal",
    "Republic of Turkiye",
    "Serbia",
    "Slovak Republic",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "United Kingdom",
    "United States"
]

# Define the list of months
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# Define the list of years
years = [
    "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"
]


@app.route('/api/electricity_data_instructions', methods=['GET'])
def electricity_data_instructions():
    instructions = (
        "Syntax: Key: country (value: check list of countries); Key: balance (Value: check list of balances); Key: Product (Value: check list of products); "
        "Key: month (Value: check list months). Key: year "
        "Note: Product options are limited based on the selected balance. See documentation for more details."
    )
    return jsonify({'instructions': instructions, 'countries': countries, 'balances': balances, 'allowed_products': allowed_products, 'months': months, 'year': years})


#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Electricity data for a specific country using specific parameters for Balance and Product, such as 'Net electricity production' and 'Electricity'
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/api/electricity_data', methods=['GET'])
def electricity_data():
    try:
        # Get query parameters from the request URL
        country = request.args.get('country')
        balance = request.args.get('balance')
        product = request.args.get('product')
        month = request.args.get('month')
        year = request.args.get('year')

        # Construct the query based on the provided parameters
        query = {}

        if country:
            query['Country'] = country
        if balance:
            query['Balance'] = balance
        if product:
            query['Product'] = product
        if month:
            # Construct a regex pattern to match any day in January of the specified year
            month_abbr = month[:3].capitalize()
            query['Time'] = {'$regex': rf'{month_abbr}-\d{{2}}', '$options': 'i'}  # Corregir la secuencia de escape
        if year:
            if 'Time' not in query:
                query['Time'] = {}
            year_pattern = year[-2:]  # Extract the last two digits of the year
            query['Time']['$regex'] = f'{query["Time"].get("$regex", "")}-{year_pattern}'

        # Filter the data based on the query
        data = list(coll.find(query))

        # Convert ObjectId to string for JSON serialization
        convert_object_ids(data)

        # Convert MongoDB documents to dictionary
        data_dict = [entry for entry in data]

        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


#-----------------------------------------------------------------------------------------------
#List of Endpoints for individual cointries, OECD zones and International Energy Agency (IEA) 
#-----------------------------------------------------------------------------------------------



# Endpoint to fetch montly electricity data for Argentina
@app.route('/api/data/country/argentina', methods=['GET'])
def get_argentina_data():
    #Retrieve data from MongoDB collection for Argentina
    data =list(coll.find({'Country': 'Argentina'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Australia
@app.route('/api/data/country/australia', methods=['GET'])
def get_australia_data():
    #Retrieve data from MongoDB collection for Australia
    data =list(coll.find({'Country': 'Australia'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Austria
@app.route('/api/data/country/austria', methods=['GET'])
def get_austria_data():
    #Retrieve data from MongoDB collection for Austria
    data =list(coll.find({'Country': 'Austria'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Belgium
@app.route('/api/data/country/belgium', methods=['GET'])
def get_belgium_data():
    #Retrieve data from MongoDB collection for Belgium
    data =list(coll.find({'Country': 'Belgium'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Brazil
@app.route('/api/data/country/brazil', methods=['GET'])
def get_brazil_data():
    #Retrieve data from MongoDB collection for Brazil
    data =list(coll.find({'Country': 'Brazil'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Bulgaria
@app.route('/api/data/country/bulgaria', methods=['GET'])
def get_bulgaria_data():
    #Retrieve data from MongoDB collection for Bulgaria
    data =list(coll.find({'Country': 'Bulgaria'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Canada
@app.route('/api/data/country/canada', methods=['GET'])
def get_canada_data():
    #Retrieve data from MongoDB collection for Canada
    data =list(coll.find({'Country': 'Canada'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Chile
@app.route('/api/data/country/chile', methods=['GET'])
def get_chile_data():
    #Retrieve data from MongoDB collection for chile
    data =list(coll.find({'Country': 'Chile'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Colombia
@app.route('/api/data/country/colombia', methods=['GET'])
def get_colombia_data():
    #Retrieve data from MongoDB collection for Colombia
    data =list(coll.find({'Country': 'Colombia'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Costa Rica
@app.route('/api/data/country/costarica', methods=['GET'])
def get_costarica_data():
    #Retrieve data from MongoDB collection for Costa Rica
    data =list(coll.find({'Country': 'Costa Rica'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Croatia
@app.route('/api/data/country/croatia', methods=['GET'])
def get_croatia_data():
    #Retrieve data from MongoDB collection for Croatia
    data =list(coll.find({'Country': 'Croatia'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Cyprus
@app.route('/api/data/country/cyprus', methods=['GET'])
def get_cyprus_data():
    #Retrieve data from MongoDB collection for Cyprus
    data =list(coll.find({'Country': 'Cyprus'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Czech Republic
@app.route('/api/data/country/czechrepublic', methods=['GET'])
def get_czechrepublic_data():
    #Retrieve data from MongoDB collection for Czech Republic
    data =list(coll.find({'Country': 'Czech Republic'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Denmark
@app.route('/api/data/country/denmark', methods=['GET'])
def get_denmark_data():
    #Retrieve data from MongoDB collection for Denmark
    data =list(coll.find({'Country': 'Denmark'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Estonia
@app.route('/api/data/country/estonia', methods=['GET'])
def get_estonia_data():
    #Retrieve data from MongoDB collection for Denmark
    data =list(coll.find({'Country': 'Estonia'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Finland
@app.route('/api/data/country/finland', methods=['GET'])
def get_finland_data():
    #Retrieve data from MongoDB collection for Finland
    data =list(coll.find({'Country': 'Finland'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for France
@app.route('/api/data/country/france', methods=['GET'])
def get_france_data():
    #Retrieve data from MongoDB collection for France
    data =list(coll.find({'Country': 'France'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Germany
@app.route('/api/data/country/germany', methods=['GET'])
def get_germany_data():
    #Retrieve data from MongoDB collection for Germany
    data =list(coll.find({'Country': 'Germany'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Greece
@app.route('/api/data/country/greece', methods=['GET'])
def get_greece_data():
    #Retrieve data from MongoDB collection for Greece
    data =list(coll.find({'Country': 'Greece'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Hungary
@app.route('/api/data/country/hungary', methods=['GET'])
def get_hungary_data():
    #Retrieve data from MongoDB collection for Hungary
    data =list(coll.find({'Country': 'Hungary'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for IEA Total
@app.route('/api/data/country/ieatotal', methods=['GET'])
def get_ieatotal_data():
    #Retrieve data from MongoDB collection for IEA Total
    data =list(coll.find({'Country': 'IEA Total'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Iceland
@app.route('/api/data/country/iceland', methods=['GET'])
def get_iceland_data():
    #Retrieve data from MongoDB collection for Iceland
    data =list(coll.find({'Country': 'Iceland'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for India
@app.route('/api/data/country/india', methods=['GET'])
def get_india_data():
    #Retrieve data from MongoDB collection for India
    data =list(coll.find({'Country': 'India'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Ireland
@app.route('/api/data/country/ireland', methods=['GET'])
def get_ireland_data():
    #Retrieve data from MongoDB collection for Ireland
    data =list(coll.find({'Country': 'Ireland'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Italy
@app.route('/api/data/country/italy', methods=['GET'])
def get_italy_data():
    #Retrieve data from MongoDB collection for Italy
    data =list(coll.find({'Country': 'Italy'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Japan
@app.route('/api/data/country/japan', methods=['GET'])
def get_japan_data():
    #Retrieve data from MongoDB collection for Japan
    data =list(coll.find({'Country': 'Japan'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Korea
@app.route('/api/data/country/korea', methods=['GET'])
def get_korea_data():
    #Retrieve data from MongoDB collection for Korea
    data =list(coll.find({'Country': 'Korea'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Latvia
@app.route('/api/data/country/latvia', methods=['GET'])
def get_latvia_data():
    #Retrieve data from MongoDB collection for Latvia
    data =list(coll.find({'Country': 'Latvia'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Lithuania
@app.route('/api/data/country/lithuania', methods=['GET'])
def get_lithuania_data():
    #Retrieve data from MongoDB collection for Lithuania
    data =list(coll.find({'Country': 'Lithuania'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Luxembourg
@app.route('/api/data/country/luxembourg', methods=['GET'])
def get_luxembourg_data():
    #Retrieve data from MongoDB collection for Luxembourg
    data =list(coll.find({'Country': 'Luxembourg'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Malta
@app.route('/api/data/country/malta', methods=['GET'])
def get_malta_data():
    #Retrieve data from MongoDB collection for Malta
    data =list(coll.find({'Country': 'Malta'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Mexico
@app.route('/api/data/country/mexico', methods=['GET'])
def get_mexico_data():
    #Retrieve data from MongoDB collection for Mexico
    data =list(coll.find({'Country': 'Mexico'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Netherlands
@app.route('/api/data/country/netherlands', methods=['GET'])
def get_netherlands_data():
    #Retrieve data from MongoDB collection for Netherlands
    data =list(coll.find({'Country': 'Netherlands'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for New Zealand
@app.route('/api/data/country/newzealand', methods=['GET'])
def get_newzealand_data():
    #Retrieve data from MongoDB collection for New Zealand
    data =list(coll.find({'Country': 'New Zealand'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for North Macedonia
@app.route('/api/data/country/northmacedonia', methods=['GET'])
def get_northmacedonia_data():
    #Retrieve data from MongoDB collection for North Macedonia
    data =list(coll.find({'Country': 'North Macedonia'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Norway
@app.route('/api/data/country/norway', methods=['GET'])
def get_norway_data():
    #Retrieve data from MongoDB collection for Norway
    data =list(coll.find({'Country': 'Norway'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for OECD Americas
@app.route('/api/data/country/oecdamericas', methods=['GET'])
def get_oecdamericas_data():
    #Retrieve data from MongoDB collection for OECD Americas
    data =list(coll.find({'Country': 'OECD Americas'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for OECD Asia Oceania
@app.route('/api/data/country/oecdasiaoceania', methods=['GET'])
def get_oecdasiaoceania_data():
    #Retrieve data from MongoDB collection for OECD Asia Oceania
    data =list(coll.find({'Country': 'OECD Asia Oceania'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for OECD Europe
@app.route('/api/data/country/oecdeurope', methods=['GET'])
def get_oecdeurope_data():
    #Retrieve data from MongoDB collection for OECD Europe
    data =list(coll.find({'Country': 'OECD Europe'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for OECD Total
@app.route('/api/data/country/oecdtotal', methods=['GET'])
def get_oecdtotal_data():
    #Retrieve data from MongoDB collection for OECD Total
    data =list(coll.find({'Country': 'OECD Total'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch monthly electricity data for People's Republic of China
@app.route('/api/data/country/peoplesrepublicofchina', methods=['GET'])
def get_peoplesrepublicofchina_data():
    # Retrieve data from MongoDB collection for People's Republic of China
    data = list(coll.find({'Country': "People's Republic of China"}))

    # Convert ObjectId to string for JSON serialization
    convert_object_ids(data)

    # Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Peru
@app.route('/api/data/country/peru', methods=['GET'])
def get_peru_data():
    #Retrieve data from MongoDB collection for Peru
    data =list(coll.find({'Country': 'Peru'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Poland
@app.route('/api/data/country/poland', methods=['GET'])
def get_poland_data():
    #Retrieve data from MongoDB collection for Poland
    data =list(coll.find({'Country': 'Poland'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Portugal
@app.route('/api/data/country/portugal', methods=['GET'])
def get_portugal_data():
    #Retrieve data from MongoDB collection for Portugal
    data =list(coll.find({'Country': 'Portugal'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Republic of Turkiye
@app.route('/api/data/country/republicofturkiye', methods=['GET'])
def get_republicofturkiye_data():
    #Retrieve data from MongoDB collection for OECD Total
    data =list(coll.find({'Country': 'Republic of Turkiye'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Serbia
@app.route('/api/data/country/serbia', methods=['GET'])
def get_serbia_data():
    #Retrieve data from MongoDB collection for Serbia
    data =list(coll.find({'Country': 'Serbia'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Slovak Republic
@app.route('/api/data/country/slovakrepublic', methods=['GET'])
def get_slovakrepublic_data():
    #Retrieve data from MongoDB collection for Slovak Republic
    data =list(coll.find({'Country': 'Slovak Republic'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Slovenia
@app.route('/api/data/country/slovenia', methods=['GET'])
def get_slovenia_data():
    #Retrieve data from MongoDB collection for slovenia
    data =list(coll.find({'Country': 'Slovenia'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Spain
@app.route('/api/data/country/spain', methods=['GET'])
def get_spain_data():
    #Retrieve data from MongoDB collection for Spain
    data =list(coll.find({'Country': 'Spain'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Sweden
@app.route('/api/data/country/sweden', methods=['GET'])
def get_sweden_data():
    #Retrieve data from MongoDB collection for Sweden
    data =list(coll.find({'Country': 'Sweden'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for Switzerland
@app.route('/api/data/country/switzerland', methods=['GET'])
def get_switzerland_data():
    #Retrieve data from MongoDB collection for Switzerland
    data =list(coll.find({'Country': 'Switzerland'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for United Kingdom
@app.route('/api/data/country/unitedkingdom', methods=['GET'])
def get_unitedkingdom_data():
    #Retrieve data from MongoDB collection for United Kingdom
    data =list(coll.find({'Country': 'United Kingdom'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)

# Endpoint to fetch montly electricity data for United States
@app.route('/api/data/country/unitedstates', methods=['GET'])
def get_unitedstates_data():
    #Retrieve data from MongoDB collection for United States
    data =list(coll.find({'Country': 'United States'}))

    # Call the convert_object_ids function to convert ObjectIds to strings
    convert_object_ids(data)

    #Convert MongoDB documents to dictionary
    data_dict = [entry for entry in data]

    return jsonify(data_dict)


#Run the Flask application
app.run(debug=True, host='localhost', port=5000)
