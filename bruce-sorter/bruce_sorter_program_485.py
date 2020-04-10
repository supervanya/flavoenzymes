
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




Red_answers = ['etrans', 'thiol', 'htrans']
Ox_answers  = ['htrans', 'disulfide', 'etrans', 'oxidase', 'mono', 'newmono']
emily_map = {'a':'eTrans, HTrans','b':'eTrans, DisulfideRed','c':'eTrans, eTrans','d':'eTrans, Oxidase','e':'eTrans, Monoox','f':'eTrans, NewMonoox','g':'ThiolOx, HTrans','h':'ThiolOx, DisulfideRed','i':'ThiolOx, eTrans','j':'ThiolOx, Oxidase','k':'ThiolOx, Monoox','l':'ThiolOx, NewMonoox','m':'HTrans, HTrans','n':'HTrans, DisulfideRed','o':'HTrans, eTrans','p':'HTrans, Oxidase','q':'HTrans, Monoox','r':'HTrans, NewMonoox'}


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

FILENAME = 'Flavoenzyme_Classification.csv'
NUMBER_ENZYMES_LEFT = 0
def readUnsortedEnzymes():
    df = pd.read_csv(InFile)
    return df[df.bin != 0]
def printGreeting():
    print(f'Welcome to the BruceSorter!\nIt looks like there are {NUMBER_ENZYMES_LEFT} enzymes left to sort')
def sortEnzymeEntry(entry,index):
    answer = promptUser()
    if (answer == 'exit'):
        exit()
    elif (answer == 'NAF'):
        writeNAFtoCSV()
    elif answer in Q1_possibilities:
        askQ2()
    else:
        handleInvalidAnswer()
def printDone():
    print('You are done! no more remaining enzymes')
def askQ2():
    return False

def main():
    unsortedEnzymes = readUnsortedEnzymes()

    if unsortedEnzymes:
        printGreeting() # this will print the remaining enzymes
        for enzyme in unsortedEnzymes:
            sortEnzymeEntry()
    else:
        printDone() # this will say there is no remaining enzymes

if __name__ == "__main__":
    main()