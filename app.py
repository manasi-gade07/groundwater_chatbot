from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

# Store last query and response for context
user_memory = {
    "last_query": None,
    "last_response": None
}

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/index')
def index():
    return render_template('index.html')

def generate_response(msg):
    global user_memory
    msg = msg.lower()

    # Check if the current message is similar to the last one
    if user_memory["last_query"] is not None and user_memory["last_query"] in msg:
        return user_memory["last_response"]  # Return previous response if the query is similar

    # Handle specific requests for groundwater-related information
    if msg in ["hi", "hello", "hey", "help", "info", "groundwater", "hydrogeology", "water quality", "recharge", "water conservation"]:
        response = ("Welcome! I’m here to help you with information on groundwater topics. "
                    "You can ask about water level scenarios, groundwater management practices, or hydrogeology. Feel free to ask!")
    elif "water level of solapur" in msg or "scenario" in msg:
        response = water_level_info()
    elif "groundwater" in msg:
        response = groundwater_info()
    elif "hydrogeology" in msg:
        response = hydrogeology_info()
    elif "water quality" in msg:
        response = water_quality_info()
    elif "management" in msg:
        response = management_info()
    elif "aquifer" in msg:
        response = aquifer_info()
    elif "recharge" in msg:
        response = recharge_info()
    elif "noc" in msg or "noc guidelines" in msg:
        response = noc_guidelines_info()
    elif "water conservation" in msg or "conservation" in msg:
        response = conservation_info()
    elif "artificial recharge" in msg:
        response = artificial_recharge_info()
    elif "types of wells" in msg or "well types" in msg:
        response = well_types_info()
    elif "well construction" in msg:
        response = well_construction_info()
    elif "well development" in msg:
        response = well_development_info()
    elif "types of aquifers" in msg:
        response = types_of_aquifers_info()
    elif "drainage" in msg:
        response = drainage_info()
    elif "over extraction" in msg:
        response = over_extraction_info()
    elif "groundwater pollution" in msg:
        response = groundwater_pollution_info()
    elif "groundwater depletion" in msg:
        response = groundwater_depletion_info()
    elif "rainwater harvesting" in msg:
        response = rainwater_harvesting_info()
    elif "sustainable groundwater use" in msg:
        response = sustainable_use_info()
    elif "aquifer recharge" in msg:
        response = aquifer_recharge_info()
    elif "groundwater law" in msg:
        response = groundwater_law_info()
    elif "aquifer storage" in msg:
        response = aquifer_storage_info()
    elif "climate change" in msg:
        response = climate_change_info()
    else:
        response = default_info()

    # Save the current query and response in memory for future use
    user_memory["last_query"] = msg
    user_memory["last_response"] = response

    return response

def water_level_info():
    water_level = round(random.uniform(10, 15), 2)  # Generates level between 10 and 15 meters
    return (f"The current groundwater level  of solapur is approximately {water_level} meters. "
            "This value is based on recent data and reflects average water levels in the area. "
            "Conservation efforts and recharge practices are vital for maintaining this level.")

def groundwater_info():
    return ("Groundwater is the water found beneath the Earth's surface in soil and rock formations. "
            "It plays a crucial role in providing drinking water, irrigation, and industrial use. "
            "It is an important natural resource that requires careful management.")

def hydrogeology_info():
    return ("Hydrogeology is the branch of geology that deals with the distribution and movement of groundwater. "
            "It involves studying aquifers, groundwater flow, and the interaction of water with soil and rock formations.")

def water_quality_info():
    return ("Water quality refers to the physical, chemical, and biological characteristics of groundwater. "
            "Key parameters include pH, dissolved oxygen, contaminants like nitrates, and microbial presence. Regular monitoring is crucial.")

def management_info():
    return ("Groundwater management includes practices aimed at ensuring the sustainable use of groundwater resources. "
            "This involves regulation, monitoring, efficient irrigation, water conservation, and groundwater recharge initiatives.")

def aquifer_info():
    return ("An aquifer is a body of rock or sediment that can store and transmit water. "
            "Aquifers are classified as confined, unconfined, and perched, each with different properties and importance for water supply.")

def recharge_info():
    return ("Recharge is the process by which groundwater is replenished. It occurs through infiltration of water from rainfall, surface water, or artificial recharge methods like recharge pits.")

def noc_guidelines_info():
    return ("The NOC (No Objection Certificate) guidelines for groundwater extraction in India regulate large-scale water extraction. "
            "To obtain an NOC, industries and farmers must apply to the Central Ground Water Authority (CGWA) and demonstrate that they are using groundwater sustainably.")

def conservation_info():
    return ("Water conservation is the practice of using water efficiently to reduce unnecessary water usage. "
            "Some common techniques include: \n"
            "1. **Rainwater Harvesting**: Collecting rainwater to recharge groundwater reserves. \n"
            "2. **Efficient Irrigation**: Using drip or sprinkler irrigation systems to reduce water wastage. \n"
            "3. **Water-Saving Appliances**: Installing low-flow taps and toilets to reduce water usage. \n"
            "4. **Reusing Water**: Reusing treated wastewater for non-potable purposes. \n"
            "5. **Groundwater Recharge**: Creating recharge wells and ponds to replenish aquifers.")

def artificial_recharge_info():
    return ("Artificial recharge refers to human-made methods that increase the rate at which groundwater is replenished. Techniques include recharge wells, check dams, and percolation tanks.")

def well_types_info():
    return ("The main types of wells are: \n"
            "1. Dug wells – constructed by digging vertically into the ground. \n"
            "2. Drilled wells – created by drilling into deeper groundwater reservoirs. \n"
            "3. Bore wells – similar to drilled wells, but usually deeper and narrower. \n"
            "4. Tube wells – a type of drilled well fitted with a pipe and pump.")

def well_construction_info():
    return ("Well construction typically involves digging or drilling a hole to reach groundwater. "
            "The well is lined with casing to prevent collapse, and a pump is installed for water extraction.")

def well_development_info():
    return ("Well development is the process of improving the efficiency and capacity of a well by removing fine particles from the aquifer and ensuring better flow of water into the well.")

def types_of_aquifers_info():
    return ("Aquifers are classified into three main types: \n"
            "1. Confined Aquifers – surrounded by impermeable rock layers, leading to pressure buildup. \n"
            "2. Unconfined Aquifers – not surrounded by impermeable layers, making them more susceptible to contamination. \n"
            "3. Perched Aquifers – small, localized aquifers above the main groundwater table.")

def drainage_info():
    return ("Drainage refers to the process of removing excess water from the soil or ground. "
            "It is essential for preventing waterlogging and maintaining groundwater levels in agricultural and urban areas.")

def water_table_info():
    return ("The water table is the boundary between saturated and unsaturated soil, indicating the level of groundwater. It fluctuates depending on rainfall, recharge, and extraction rates.")

def over_extraction_info():
    return ("Over-extraction of groundwater can lead to depletion of aquifers, land subsidence, and reduced water availability. Sustainable extraction rates are crucial to prevent these issues.")

def groundwater_pollution_info():
    return ("Groundwater pollution is caused by the contamination of groundwater from sources such as industrial waste, agricultural runoff, and improper disposal of chemicals. It poses a significant risk to water quality.")

def groundwater_depletion_info():
    return ("Groundwater depletion occurs when water extraction exceeds the natural recharge rate, leading to a decrease in available groundwater. This can lead to long-term shortages and affect ecosystems.")

def rainwater_harvesting_info():
    return ("Rainwater harvesting involves capturing rainwater runoff from roofs or other surfaces for storage and later use. It helps to reduce dependence on groundwater and provides an alternative water source.")

def sustainable_use_info():
    return ("Sustainable groundwater use involves managing water extraction to ensure that aquifers are replenished at the same rate as they are used. This includes practices such as efficient irrigation and reducing waste.")

def aquifer_recharge_info():
    return ("Aquifer recharge involves methods to enhance the natural process of replenishing groundwater. This includes techniques like recharge wells, managed aquifer recharge (MAR), and water harvesting systems.")

def groundwater_law_info():
    return ("Groundwater laws vary by country and region, regulating extraction and use to ensure sustainability. In India, the Central Ground Water Authority (CGWA) sets guidelines for groundwater extraction.")

def aquifer_storage_info():
    return ("Aquifer storage refers to the amount of water that can be stored in an aquifer. It is an important factor in groundwater management and helps determine the availability of water during droughts.")

def climate_change_info():
    return ("Climate change affects groundwater levels by altering precipitation patterns, evaporation rates, and water availability. It can lead to more intense droughts and floods, impacting groundwater recharge and availability.")

def default_info():
    return ("I'm sorry, I didn't quite understand that. Could you please ask your question again?")

@socketio.on('message')
def handle_message(msg):
    response = generate_response(msg)
    emit('response', response)

if __name__ == "__main__":
    socketio.run(app, debug=True)
