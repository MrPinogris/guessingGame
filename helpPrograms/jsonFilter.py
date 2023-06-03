import json

def load_block_data():
    with open('C:\\Users\\alexa\\Documents\\selfLearning\\coding\\guessingGame\\dataFiles\\block_data.json') as file:
        block_data = json.load(file)
    return block_data

block_data = load_block_data()
filtered_block_data = {}

for block_name, block_info in block_data.items():
    if "pools" in block_info:
        pools = block_info["pools"]
        for pool in pools:
            if "entries" in pool:
                filtered_block_data[block_name] = block_info
                break

def save_filtered_block_data(filtered_block_data):
    with open('filtered_block_data.json', 'w') as file:
        json.dump(filtered_block_data, file, indent=4)

save_filtered_block_data(filtered_block_data)
