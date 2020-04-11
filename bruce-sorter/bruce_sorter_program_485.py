import pandas as pd
import json

"""
Program Flow:
1. Prints entree (ENZYME) from the csv
2. Q1. Prompts the user for the classification (options: exit | NAF | ......real classifications..... )
    a. If answer is valid classification -> write to the CSV
        i. Ask Q2
    b. If answer is 'other              -> prompt for description -> write to the CSV
        i. Ask Q2
    c. If answer is 'exit'              -> exit the program
    d. If answer is 'NAF'               -> write to the CSV


Ask Q2 (function):
1. prompt for classification:
    a. If answer is valid classification:
        i. Assign Bin
    b. If answer is 'other:
        i. prompt for description ->  Assign Bin -> write to the CSV
"""

FILE_NAME = 'flavoenzymes_to_sort.csv'
DF = pd.read_csv(FILE_NAME)
DF['bin'] = DF['bin'].astype(str)
NUMBER_ENZYMES_LEFT = len(DF[DF.bin == '0'])

# question specific parameters 
Ox_answers_col_name = 'OxidativeHalf'
Ox_answers  = ['htrans', 'disulfide', 'etrans', 'oxidase', 'mono', 'newmono', 'h', 'd', 'e', 'o', 'm', 'n']
Ox_answers_prompt = "Enter one of: htrans(h), disulfide(d), etrans(e), oxidase(o), mono(m), newmono(n)\nFor example, you can enter 'newmono' or just 'n'"

Red_answers_col_name = 'ReductionHalf'
Red_answers = ['etrans', 'thiol', 'htrans', 'e', 't', 'h']
Red_answers_prompt = "Enter one of: etrans(e), thiol(t), htrans(h). For example, you can enter 'etrans' or just 'e'"


# mappings
answer_map = {
    'htrans':    'HTrans',
    'disulfide': 'DisulfideRed',
    'etrans':    'eTrans',
    'oxidase':   'Oxidase',
    'mono':      'Monoox',
    'newmono':   'NewMonoox',
    'e': 'eTrans',
    't': 'ThiolOx',
    'h': 'HTrans',
    'd': 'DisulfideRed',
    'o': 'Oxidase',
    'm': 'Monoox',
    'n': 'NewMonoox',
    'thiol': 'ThiolOx'
    }

bin_answer_map = {
    'eTrans, HTrans': 'a',
    'eTrans, DisulfideRed': 'b',
    'eTrans, eTrans': 'c',
    'eTrans, Oxidase': 'd',
    'eTrans, Monoox': 'e',
    'eTrans, NewMonoox': 'f',
    'ThiolOx, HTrans': 'g',
    'ThiolOx, DisulfideRed': 'h',
    'ThiolOx, eTrans': 'i',
    'ThiolOx, Oxidase': 'j',
    'ThiolOx, Monoox': 'k',
    'ThiolOx, NewMonoox': 'l',
    'HTrans, HTrans': 'm',
    'HTrans, DisulfideRed': 'n',
    'HTrans, eTrans': 'o',
    'HTrans, Oxidase': 'p',
    'HTrans, Monoox': 'q',
    'HTrans, NewMonoox': 'r'
}

def getUnsortedEnzymesIndex():
    return DF[DF.bin == '0'].index

def saveProgressToCSV():
    DF.to_csv(FILE_NAME,index=False)

def writeToCSV(answer,index,column):
    DF.loc[index,column] = answer
    saveProgressToCSV()

def writeNAFtoCSV(index):
    print("Reported as a 'Not a Flavoenzyme'")
    writeToCSV('NAF',index,'bin')

def printGreeting():
    print("**************************************************")
    print("***   Hi Bruce, ready to sort some enzymes?    ***")
    print("**************************************************")
    print(f'\nIt looks like there are {NUMBER_ENZYMES_LEFT} enzymes left\n\n')

def askPrompt(index,prompt):
    '''
    prompts the user for answer
    returns the answer
    '''    
    return input(prompt + "\n > ")

def handleInvalidInput(answer,index,possible_answers,prompt,column):
    print(f'⚠️ You have entered "{answer}". That is not a valid input. Try again?')
    input("PRESS ENTER/RETURN TO CONTINUE...")
    handleQuestion(index,possible_answers,prompt,column)

def handleQuestion(index,possible_answers,prompt,column):
    answer = askPrompt(index, prompt)
    if (answer == 'exit'):
        quit()
    elif (answer == 'NAF'):
        writeNAFtoCSV(index)
    elif (answer in possible_answers) or (answer in ['other','idk']):
        answer = answer_map[answer]
        writeToCSV(answer,index,column)
    else:
        handleInvalidInput(answer,index,possible_answers,prompt,column)

def handleQ1(index):
    handleQuestion(index, possible_answers=Ox_answers, prompt=Ox_answers_prompt, column=Ox_answers_col_name)    

def handleQ2(index):
    handleQuestion(index, possible_answers=Red_answers, prompt=Red_answers_prompt, column=Red_answers_col_name)

def handleBinning(index):
    ox = DF.at[index, Ox_answers_col_name]
    red = DF.at[index, Red_answers_col_name]
    bin = DF.at[index, 'bin']

    if 'NAF' in [ox,red,bin]:
        writeNAFtoCSV(index)
    elif 'idk' in [ox,red]:
        writeToCSV('idk',index,'bin')
    elif 'other' in [ox,red]:
        writeToCSV('other',index,'bin')
    else:
        bin = bin_answer_map[f"{red}, {ox}"]
        writeToCSV(bin,index,'bin')

def printEnzymeInfo(index):
    print(f'Row #: {index + 1}')
    name = DF.at[index,'SYSNAME']
    substrates = json.loads(DF.at[index,'SUBSTRATE'])
    products = json.loads(DF.at[index,'PRODUCT'])
    ec = DF.at[index,'ec']

    print("This is the enzyme:")
    print(f'Kegg link: https://www.genome.jp/dbget-bin/www_bget?ec:{ec}')
    print(f'Brenda link: https://www.brenda-enzymes.info/enzyme.php?ecno={ec}')
    
    print(f"Name: {name}")
    
    print(f"Substrates:")
    [print(f" • {s}") for s in substrates]
    
    print(f"Products:")
    [print(f" • {p}") for p in products]

def quit():
    if NUMBER_ENZYMES_LEFT == 0:
        print('You are done! no more remaining enzymes')
    else:
        print(f'{NUMBER_ENZYMES_LEFT} enzymes left to sort, have a good day!')
    exit()

def askQuestions(index):
    handleQ1(index)
    handleQ2(index)

def main():
    unsortedEnzymes = getUnsortedEnzymesIndex()
    if len(unsortedEnzymes) > 0:
        printGreeting() 
        for index in unsortedEnzymes:
            try:
                printEnzymeInfo(index)
            except:
                writeNAFtoCSV(index)
            else:
                askQuestions(index)
                handleBinning(index)

    else:
        quit() # this will say there is no remaining enzymes

if __name__ == "__main__":
    main()