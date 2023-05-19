import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    #open file
    f=open('data/result.json',encoding='utf8')
    r=json.load(f)
    return r
file_path=''
print(read_data(file_path))