from api import JsonData

def main():
    json_data = JsonData(in_file='nested.json', response_key='mathematicians')
    normalized_df = json_data.normalize_array()
    json_data.write_dataframe(normalized_df)   
 
if __name__=="__main__":
    main()

