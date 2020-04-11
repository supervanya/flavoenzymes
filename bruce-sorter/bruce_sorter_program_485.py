
""" 
import json
import pandas as pd
import numpy as np
from numpy import nan

InFile='Flavoenzyme_Classification.csv'
df = pd.read_csv(InFile)

df['bin'] = df['bin'].astype(str)
df['ReductionHalf'] = df['ReductionHalf'].astype(str)
df['OxidativeHalf'] = df['OxidativeHalf'].astype(str)

for entry in df.index:
    if(df.loc[entry,'bin'] == '0'):
        istring = str(entry)
       #print("Index Number: "+ istring)
        totalindex = str(len(df.index))
        #print("Total Index: "+totalindex)
        binlist = df['bin'].tolist()
        left = str(binlist.count('0'))

for entry in df.index:
    if(df.loc[entry,'bin'] == '0'):
        istring = str(entry)
        print("Index Number: "+ istring)
        totalindex = str(len(df.index))
        print("Total Index: "+totalindex)
        binlist = df['bin'].tolist()
        left = str(binlist.count('0'))
        print("Left to sort: "+left)
        #df.at[entry,'bin'] = df.at[entry,'bin'].astype(str)
        print("Type 'exit' to exit.")
        print("**************************************")
        sysname = df.at[entry,'SYSNAME']
        print("This is the enzyme: "+ sysname)
        product = df.at[entry, 'PRODUCT']
        substrate = df.at[entry, 'SUBSTRATE']
        print('\n')
        print("Enzyme substrates: " + substrate)
        print('\n')
        print("Enzyme products: " + product)
        print('\n')
        print("Reduction Half Reactions Key:")
        print("etrans = e-Transfer, thiol = Thiol Oxidation, htrans = H-Transfer, idk = I don't know")
        RedAns = input("Reduction Half Reaction? (etrans, thiol, htrans, other, or idk)")

        if RedAns == 'exit':
            print("***")
            print("Exited loop at:")
            print(entry)
            print(df.at[entry, 'SYSNAME'])
            print("***")
            break
        elif RedAns == 'etrans':
            print("***")
            print("Reduction Half = "+ RedAns)
            print("***")
            df.at[entry,'ReductionHalf'] = 'eTransfer'
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'HTransfer'
                if df.at[entry,'ReductionHalf'] == 'eTransfer':
                    df.at[entry,'bin'] = 'a'
                df.to_csv(InFile,index=False)
            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'DisulfideReduction'
                if df.at[entry,'ReductionHalf'] == 'eTransfer':
                    df.at[entry,'bin'] = 'b'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'eTransfer'
                if df.at[entry,'ReductionHalf'] == 'eTransfer':
                    df.at[entry,'bin'] = 'c'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Oxidase'
                if df.at[entry,'ReductionHalf'] == 'eTransfer':
                    df.at[entry,'bin'] = 'd'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Monooxygenase'
                if df.at[entry,'ReductionHalf'] == 'eTransfer':
                    df.at[entry,'bin'] = 'e'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'NewMonooxygenase'
                if df.at[entry,'ReductionHalf'] == 'eTransfer':
                    df.at[entry,'bin'] = 'f'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'idk'
                if df.at[entry,'ReductionHalf'] == 'eTransfer':
                    df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'other'
                if df.at[entry,'ReductionHalf'] == 'eTransfer':
                    df.at[entry,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("Not a valid selection.")
                print("You wrote:"+ OxAns)
                print("Please type: etrans, disulfide, htrans, oxidase, mono, newmono, idk, other, or exit.")
                print("Note: You must type this word exactly with no spaces, then hit ENTER/RETURN")
                print("***")
                break

        elif RedAns == 'thiol':
            print("***")
            print("Reduction Half = "+ RedAns)
            print("***")
            df.at[entry,'ReductionHalf'] = 'ThiolOxidation'
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'HTransfer'
                if df.at[entry,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[entry,'bin'] = 'g'
                df.to_csv(InFile,index=False)
            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'DisulfideReduction'
                if df.at[entry,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[entry,'bin'] = 'h'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'eTransfer'
                if df.at[entry,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[entry,'bin'] = 'i'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Oxidase'
                if df.at[entry,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[entry,'bin'] = 'j'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Monooxygenase'
                if df.at[entry,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[entry,'bin'] = 'k'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'NewMonooxygenase'
                if df.at[entry,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[entry,'bin'] = 'l'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'idk'
                if df.at[entry,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'other'
                if df.at[entry,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[entry,'bin'] = 'other'
                OxOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
                df.at[entry,'OxOther'] = OxOtherDescript
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("Not a valid selection.")
                print("You wrote:"+ OxAns)
                print("Please type: etrans, disulfide, htrans, oxidase, mono, newmono, idk, other, or exit.")
                print("Note: You must type this word exactly with no spaces, then hit ENTER/RETURN")
                print("***")
                break
        elif RedAns == 'htrans':
            print("***")
            print("Reduction Half = "+ RedAns)
            print("***")
            df.at[entry,'ReductionHalf'] = 'HTransfer'
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'HTransfer'
                if df.at[entry,'ReductionHalf'] == 'HTransfer':
                    df.at[entry,'bin'] = 'm'
                df.to_csv(InFile,index=False)
            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'DisulfideReduction'
                if df.at[entry,'ReductionHalf'] == 'HTransfer':
                    df.at[entry,'bin'] = 'n'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'eTransfer'
                if df.at[entry,'ReductionHalf'] == 'HTransfer':
                    df.at[entry,'bin'] = 'o'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Oxidase'
                if df.at[entry,'ReductionHalf'] == 'HTransfer':
                    df.at[entry,'bin'] = 'p'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Monooxygenase'
                if df.at[entry,'ReductionHalf'] == 'HTransfer':
                    df.at[entry,'bin'] = 'q'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'NewMonooxygenase'
                if df.at[entry,'ReductionHalf'] == 'HTransfer':
                    df.at[entry,'bin'] = 'r'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'idk'
                if df.at[entry,'ReductionHalf'] == 'HTransfer':
                    df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'other'
                if df.at[entry,'ReductionHalf'] == 'HTransfer':
                    df.at[entry,'bin'] = 'other'
                OxOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
                df.at[entry,'OxOther'] = OxOtherDescript
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("Not a valid selection.")
                print("You wrote:"+ OxAns)
                print("Please type: etrans, disulfide, htrans, oxidase, mono, newmono, idk, other, or exit.")
                print("Note: You must type this word exactly with no spaces, then hit ENTER/RETURN")
                print("***")
                break

        elif RedAns == 'idk':
            print("***")
            print("Reduction Half = "+ RedAns)
            print("***")
            df.at[entry,'ReductionHalf'] = 'idk'
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'HTransfer'
                df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)

            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'DisulfideReduction'
                df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'eTransfer'
                df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Oxidase'
                df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Monooxygenase'
                df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'NewMonooxygenase'
                df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'idk'
                df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'other'
                df.at[entry,'bin'] = 'idk'
                OxOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
                df.at[entry,'OxOther'] = OxOtherDescript
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("Not a valid selection.")
                print("You wrote:"+ OxAns)
                print("Please type: etrans, disulfide, htrans, oxidase, mono, newmono, idk, other, or exit.")
                print("Note: You must type this word exactly with no spaces, then hit ENTER/RETURN")
                print("***")
                break

        elif RedAns == 'other':
            print("***")
            print("Reduction Half = "+ RedAns)
            print("***")
            df.at[entry,'ReductionHalf'] = 'other'
            RedOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
            df.at[entry,'RedOther'] = RedOtherDescript
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'HTransfer'
                df.at[entry,'bin'] = 'other'
                df.to_csv(InFile,index=False)

            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'DisulfideReduction'
                df.at[entry,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'eTransfer'
                df.at[entry,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Oxidase'
                df.at[entry,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'Monooxygenase'
                df.at[entry,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'NewMonooxygenase'
                df.at[entry,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'idk'
                df.at[entry,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[entry,'OxidativeHalf'] = 'other'
                df.at[entry,'bin'] = 'other'
                OxOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
                df.at[entry,'OxOther'] = OxOtherDescript
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(entry)
                print(df.at[entry, 'SYSNAME'])
                print("Not a valid selection.")
                print("You wrote:"+ OxAns)
                print("Please type: etrans, disulfide, htrans, oxidase, mono, newmono, idk, other, or exit.")
                print("Note: You must type this word exactly with no spaces, then hit ENTER/RETURN")
                print("***")
                break

        else:
            print("***")
            print("Index Number:")
            print(entry)
            print(df.at[entry, 'SYSNAME'])
            print("Not a valid selection.")
            print("You wrote:"+ RedAns)
            print("Please type: etrans, thiol, htrans, idk, other, or exit.")
            print("Note: You must type this word exactly with no spaces and no punction, then hit ENTER/RETURN")
            print("***")
            break
        print("**************************************")
    else:
        #print("No more enzymes left!")
        pass

print("*********   End of Program   *********")
#print(df.head())
#print(df.loc[df['bin']=='c'])
df.to_csv(InFile,index=False)
 """




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


import pandas as pd

FILE_NAME = 'flavoenzymes_to_sort.csv'
DF = pd.read_csv(FILE_NAME)
NUMBER_ENZYMES_LEFT = len(DF[DF.bin == 0])

# question specific parameters 
Red_answers_col_name = 'ReductionHalf'
Red_answers = ['etrans', 'thiol', 'htrans', 'e', 't', 'h']
Red_answers_prompt = "Enter one of: etrans(e), thiol(t), htrans(t). For example, you can enter 'etrans' or just 'e'"

Ox_answers_col_name = 'OxidativeHalf'
Ox_answers  = ['htrans', 'disulfide', 'etrans', 'oxidase', 'mono', 'newmono', 'h', 'd', 'e', 'o', 'm', 'n']
Ox_answers_prompt = "Enter one of: htrans(h), disulfide(d), etrans(e), oxidase(o), mono(m), newmono(n)\nFor example, you can enter 'newmono' or just 'n'"

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

'''

'''
def getUnsortedEnzymesIndex():
    return DF[DF.bin == 0].index

def saveProgressToCSV():
    DF.to_csv(FILE_NAME,index=False)

def writeToCSV(answer,index,column):
    DF.iloc[index][column] = answer
    saveProgressToCSV()

def printGreeting():
    print("**************************************************")
    print("***   Hi Bruce, ready to sort some enzymes?    ***")
    print("**************************************************")
    print(f'It looks like there are {NUMBER_ENZYMES_LEFT} enzymes left to sort')

def askQuestion(index,prompt):
    '''
    prints the enzyme properties to the terminal
    propmpts the user for answer
    returns the answer
    '''
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
    
    return input(prompt + "\n > ")
    
def handleQuestion(index,possible_answers,prompt,column):
    answer = askQuestion(index,prompt)
    if (answer == 'exit'):
        exit()
    elif (answer == 'NAF'):
        writeNAFtoCSV(index)
    elif (answer in Red_answers) or (answer in ['other','idk']):
        writeToCSV(answer,index,column)
    else:
        handleInvalidAnswer()

def handleQ2(index):
    answer = askQ2(index)
    if (answer == 'exit'):
        exit()
    elif (answer == 'NAF'):
        writeNAFtoCSV(index)
    elif (answer in Ox_answers) or (answer in ['other','idk']):
        writeQ1ToCSV(answer,index)
        handleQ2(index)
    else:
        handleInvalidAnswer()

def printDone():
    print('You are done! no more remaining enzymes')

def handleQ1():
    handleQuestion(index, possible_answers=Red_answers, prompt=Red_answers_prompt, column=Red_answers_col_name)
    writeQ1toCSV(index)
    saveToCSV()

def writeQ2toCSV(index):

def handleQ2(index):
    handleQuestion(index, possible_answers=Ox_answers, prompt=Ox_answers_prompt, column=Ox_answers_col_name)
    writeQ2toCSV(index)
    

def main():
    unsortedEnzymes = getUnsortedEnzymesIndex()
    if unsortedEnzymes:
        printGreeting() 
        for index in unsortedEnzymes:
            handleQ1(index)
            handleQ2(index)
            calculateBin(index)
    else:
        printDone() # this will say there is no remaining enzymes

if __name__ == "__main__":
    main()