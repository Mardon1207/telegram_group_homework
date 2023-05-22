from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.

    """
    l=0
    for i in data['messages']:
        if i["type"]=="message":
            l+=1
    return l
file_path='data/result.json'
data=read_data(file_path)
print(find_number_of_messages(data))