import pandas as pd
import json

"""
Program Flow:
1. Prints entree (ENZYME) from the csv
2. Q1. Prompts the user for the classification (options: exit | naf | ......real classifications..... )
    a. If answer is valid classification -> write to the CSV
        i. Ask Q2
    b. If answer is 'other              -> prompt for description -> write to the CSV
        i. Ask Q2
    c. If answer is 'exit'              -> exit the program
    d. If answer is 'naf'               -> write to the CSV


Ask Q2 (function):
1. prompt for classification:
    a. If answer is valid classification:
        i. Assign Bin
    b. If answer is 'other:
        i. prompt for description ->  Assign Bin -> write to the CSV
"""

class NotFlavoEnzymeError(ValueError):
    pass

FILE_NAME = 'flavoenzymes_to_sort.csv'
DF = pd.read_csv(FILE_NAME)
DF['bin'] = DF['bin'].astype(str)
NUMBER_ENZYMES_LEFT = len(DF[DF.bin == '0'])
TERMINAL_WIDTH = 130

# question specific parameters 
other_answers = ['naf', 'idk', 'other']

Ox_answers_col_name = 'OxidativeHalf'
Ox_answers  = ['htrans', 'disulfide', 'etrans', 'oxidase', 'mono', 'newmono', 'h', 'd', 'e', 'o', 'm', 'n'] + other_answers
Ox_answers_prompt = "==> OxidativeHalf\nEnter one of: htrans(h), disulfide(d), etrans(e), oxidase(o), mono(m), newmono(n), not-a-flavin(naf), other or idk\nFor example, you can enter 'newmono' or just 'n'"

Red_answers_col_name = 'ReductionHalf'
Red_answers = ['etrans', 'thiol', 'htrans', 'e', 't', 'h'] + other_answers
Red_answers_prompt = "==> ReductionHalf\nEnter one of: etrans(e), thiol(t), htrans(h), not-a-flavin(naf), other or idk.\nFor example, you can enter 'etrans' or just 'e'"


# mappings
answer_map = {
    'htrans':    'HTrans',
    'disulfide': 'DisulfideRed',
    'etrans':    'eTrans',
    'oxidase':   'Oxidase',
    'mono':      'Monoox',
    'newmono':   'NewMonoox',
    'e':         'eTrans',
    't':         'ThiolOx',
    'h':         'HTrans',
    'd':         'DisulfideRed',
    'o':         'Oxidase',
    'm':         'Monoox',
    'n':         'NewMonoox',
    'thiol':     'ThiolOx',
    'idk':       'idk',
    'other':     'other',
    'naf':       'naf'
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
    printMessage('💾 Saved progress to CSV 💾',sep="=")

def writeToDF(answer,index,column):
    printMessage(f"Written '{answer}' for '{column}'")
    DF.loc[index,column] = answer

def writeNAF(index):
    printMessage("Reported as a naf(Not a Flavoenzyme)")
    writeToDF('naf',index,'bin')

def printGreeting():
    print("*"*TERMINAL_WIDTH)
    printMessage("Hi Bruce, ready to sort some enzymes?",'*')
    print("*"*TERMINAL_WIDTH)

    printMessage(f'It looks like there are {NUMBER_ENZYMES_LEFT} enzymes left')
    print('\n')

def printMessage(message, sep=False):
    if sep:
        print(f" {message} ".center(TERMINAL_WIDTH, sep))
    else:
        print(f"> {message} <".center(TERMINAL_WIDTH, ' '))

def printEnd():
    print('\n'*30)

def askPrompt(index,prompt):
    '''
    prompts the user for answer
    returns the answer
    '''    
    return input(prompt + "\n > ").lower()

def handleInvalidInput(answer,index,possible_answers,prompt,column):
    print(f'⚠️ You have entered "{answer}". That is not a valid input. Try again?')
    input("PRESS ENTER/RETURN TO CONTINUE...")
    handleQuestion(index,possible_answers,prompt,column)

def handleBinning(index):
    ox = DF.at[index, Ox_answers_col_name]
    red = DF.at[index, Red_answers_col_name]
    bin = DF.at[index, 'bin']

    if 'naf' in [ox,red,bin]:
        writeNAF(index)
        raise NotFlavoEnzymeError('Not a flavoenzyme encountered')
    elif 'idk' in [ox,red]:
        writeToDF('idk',index,'bin')
    elif 'other' in [ox,red]:
        writeToDF('other',index,'bin')
    else:
        bin = bin_answer_map[f"{red}, {ox}"]
        writeToDF(bin,index,'bin')

def printCompoundInfo(compoundJsonString):
    try:
        # parsing might error, hence the try/except
        compound_list = json.loads(compoundJsonString)
    except:
        print('- None listed for this one')
    else:
        [print(f" • {s}") for s in compound_list]

def printEnzymeInfo(index):
    print(f'Row #: {index + 1}')
    name = DF.at[index,'SYSNAME']
    substrates = (DF.at[index,'SUBSTRATE'])
    products = (DF.at[index,'PRODUCT'])
    ec = DF.at[index,'ec']

    print("This is the enzyme:")
    print(f"Name: {name}")
    print(f'Kegg link: https://www.genome.jp/dbget-bin/www_bget?ec:{ec}')
    print(f'Brenda link: https://www.brenda-enzymes.info/enzyme.php?ecno={ec}')
    
    print(f"Substrates:")
    printCompoundInfo(substrates)
    print(f"Products:")
    printCompoundInfo(products)

def quit():
    if NUMBER_ENZYMES_LEFT == 0:
        print('You are done! no more remaining enzymes')
    else:
        print(f'{NUMBER_ENZYMES_LEFT} enzymes left to sort, have a good day!')
    exit()


def handleQuestion(index,possible_answers,prompt,column):
    answer = askPrompt(index, prompt)
    if (answer == 'exit'):
        quit()
    elif (answer == 'naf'):
        raise NotFlavoEnzymeError('Not a flavin')
    elif (answer in possible_answers) or (answer in ['other','idk']):
        answer = answer_map[answer]
        writeToDF(answer,index,column)
    else:
        handleInvalidInput(answer,index,possible_answers,prompt,column)

def handleQ1(index):
    handleQuestion(index, possible_answers=Ox_answers, prompt=Ox_answers_prompt, column=Ox_answers_col_name)    

def handleQ2(index):
    handleQuestion(index, possible_answers=Red_answers, prompt=Red_answers_prompt, column=Red_answers_col_name)

def askQuestions(index):
    handleQ1(index)
    handleQ2(index)
    
def main():
    unsortedEnzymes = getUnsortedEnzymesIndex()
    if len(unsortedEnzymes) > 0:
        printGreeting() 
        for index in unsortedEnzymes:
            printEnzymeInfo(index)
            try:
                askQuestions(index)
            except NotFlavoEnzymeError:
                writeNAF(index)
            else:
                handleBinning(index)
            finally:
                saveProgressToCSV()
                printEnd()
    else:
        quit() # this will say there is no remaining enzymes

if __name__ == "__main__":
    main()