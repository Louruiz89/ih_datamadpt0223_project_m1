import pandas as pd
import argparse

df = pd.read_csv('data/final_result.csv')

'''
def show_all(csv):
    return df[:10]
    
def embasy(one):
    return input('Select an Embassy or a Consulship to get the nearest BiciMAD Station: ')
'''


def argument_parser():
    parser = argparse.ArgumentParser(description= 'Application to know the closest BiciMAD Station to embassies' )
    help_message ='You have two options. Option 1: "Example" show 10 rows of the CSV file. Option 2: "Check a Place" find the nearest BiciMAD Station' 
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args



print('Welcome to the BiciMAD Station nearest to each Embassy and Consulship')



def find_address():
    place = input("Select an Embassy or a Consulship to get the nearest BiciMAD Station: ")
    result = df.loc[df['Place of interest'] == place, 'BiciMAD station'].iloc[0]
    print(result)

# Call the function to start the search
find_address()


# In[7]:


if __name__ == '__main__':
    if argument_parser().function == 'Example':
        result = print(df[:10])
    elif argument_parser().function == 'Check a Place':
        result = find_address()
    else:
        result = 'FATAL ERROR...sorry the APP is not able to do that, bye'
    print(f'The result is => {result}')

