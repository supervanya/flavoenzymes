import pandas as pd
import numpy as np
from numpy import nan

#InFile = "C:\\Users\\emirob\\Desktop\\allhbplus\\0hbplusPISAandBAs5Codes.7.31.19\\ResultsAndAnalysis\\PDBCodesNotSorted.csv" #Use full path if having issues
InFile = "PDBCodesNotSorted.csv"

df = pd.read_csv(InFile)
df = df.fillna('0')
#df['bin'] = df['bin'].astype(int) #might have to use this before running the program the first time but comment out if restarting
df['bin'] = df['bin'].astype(str)
df['ReductionHalf'] = df['ReductionHalf'].astype(str)
df['OxidativeHalf'] = df['OxidativeHalf'].astype(str)
#pd.set_option("display.max_colwidth", 10000)

print(df)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#print(df)
print("**************************************************")
print("***   Hi Bruce, ready to sort some enzymes?   ***")
print("**************************************************")
#(df.at[i,'bin'] == np.nan)

for i in df.index:

    if(df.loc[i,'bin'] == '0'):
        istring = str(i)
        print("Index Number: "+ istring)
        totalindex = str(len(df.index))
        print("Total Index: "+totalindex)
        binlist = df['bin'].tolist()
        left = str(binlist.count('0'))
        print("Left to sort: "+left)
        #df.at[i,'bin'] = df.at[i,'bin'].astype(str)
        print("Type 'exit' to exit.")
        print("**************************************")

        print("This is the enzyme:")
        pdbcode2 = df.at[i,'pdbcode']
        print(pdbcode2)
        namestring = df.at[i, 'title']
        namestring.replace("  ","")
        print(namestring)
        print("Reduction Half Reactions Key:")
        print("etrans = e-Transfer, thiol = Thiol Oxidation, htrans = H-Transfer, idk = I don't know")
        RedAns = input("Reduction Half Reaction? (etrans, thiol, htrans, other, or idk)")

        if RedAns == 'exit':
            print("***")
            print("Exited loop at:")
            print(i)
            print(df.at[i, 'pdbcode'])
            print("***")
            break

        elif RedAns == 'etrans':
            print("***")
            print("Reduction Half = "+ RedAns)
            print("***")
            df.at[i,'ReductionHalf'] = 'eTransfer'
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(i)
                print(df.at[i, 'pdbcode'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'HTransfer'
                if df.at[i,'ReductionHalf'] == 'eTransfer':
                    df.at[i,'bin'] = 'a'
                df.to_csv(InFile,index=False)
            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'DisulfideReduction'
                if df.at[i,'ReductionHalf'] == 'eTransfer':
                    df.at[i,'bin'] = 'b'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'eTransfer'
                if df.at[i,'ReductionHalf'] == 'eTransfer':
                    df.at[i,'bin'] = 'c'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Oxidase'
                if df.at[i,'ReductionHalf'] == 'eTransfer':
                    df.at[i,'bin'] = 'd'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Monooxygenase'
                if df.at[i,'ReductionHalf'] == 'eTransfer':
                    df.at[i,'bin'] = 'e'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'NewMonooxygenase'
                if df.at[i,'ReductionHalf'] == 'eTransfer':
                    df.at[i,'bin'] = 'f'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'idk'
                if df.at[i,'ReductionHalf'] == 'eTransfer':
                    df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'other'
                if df.at[i,'ReductionHalf'] == 'eTransfer':
                    df.at[i,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(i)
                print(df.at[i, 'pdbcode'])
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
            df.at[i,'ReductionHalf'] = 'ThiolOxidation'
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(i)
                print(df.at[i, 'pdbcode'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'HTransfer'
                if df.at[i,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[i,'bin'] = 'g'
                df.to_csv(InFile,index=False)
            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'DisulfideReduction'
                if df.at[i,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[i,'bin'] = 'h'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'eTransfer'
                if df.at[i,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[i,'bin'] = 'i'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Oxidase'
                if df.at[i,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[i,'bin'] = 'j'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Monooxygenase'
                if df.at[i,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[i,'bin'] = 'k'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'NewMonooxygenase'
                if df.at[i,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[i,'bin'] = 'l'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'idk'
                if df.at[i,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'other'
                if df.at[i,'ReductionHalf'] == 'ThiolOxidation':
                    df.at[i,'bin'] = 'other'
                OxOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
                df.at[i,'OxOther'] = OxOtherDescript
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(i)
                print(df.at[i, 'pdbcode'])
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
            df.at[i,'ReductionHalf'] = 'HTransfer'
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(i)
                print(df.at[i, 'pdbcode'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'HTransfer'
                if df.at[i,'ReductionHalf'] == 'HTransfer':
                    df.at[i,'bin'] = 'm'
                df.to_csv(InFile,index=False)
            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'DisulfideReduction'
                if df.at[i,'ReductionHalf'] == 'HTransfer':
                    df.at[i,'bin'] = 'n'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'eTransfer'
                if df.at[i,'ReductionHalf'] == 'HTransfer':
                    df.at[i,'bin'] = 'o'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Oxidase'
                if df.at[i,'ReductionHalf'] == 'HTransfer':
                    df.at[i,'bin'] = 'p'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Monooxygenase'
                if df.at[i,'ReductionHalf'] == 'HTransfer':
                    df.at[i,'bin'] = 'q'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'NewMonooxygenase'
                if df.at[i,'ReductionHalf'] == 'HTransfer':
                    df.at[i,'bin'] = 'r'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'idk'
                if df.at[i,'ReductionHalf'] == 'HTransfer':
                    df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'other'
                if df.at[i,'ReductionHalf'] == 'HTransfer':
                    df.at[i,'bin'] = 'other'
                OxOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
                df.at[i,'OxOther'] = OxOtherDescript
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(i)
                print(df.at[i, 'pdbcode'])
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
            df.at[i,'ReductionHalf'] = 'idk'
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(i)
                print(df.at[i, 'pdbcode'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'HTransfer'
                df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)

            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'DisulfideReduction'
                df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'eTransfer'
                df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Oxidase'
                df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Monooxygenase'
                df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'NewMonooxygenase'
                df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'idk'
                df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'other'
                df.at[i,'bin'] = 'idk'
                OxOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
                df.at[i,'OxOther'] = OxOtherDescript
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(i)
                print(df.at[i, 'pdbcode'])
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
            df.at[i,'ReductionHalf'] = 'other'
            RedOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
            df.at[i,'RedOther'] = RedOtherDescript
            df.to_csv(InFile,index=False)
            print("Oxidative Half Reactions Key:")
            print("etrans = e-Transfer, disulfide = Disulfide Reduction, htrans = H-Transfer, oxidase = Oxidase")
            print("mono = Monooxygenase, newmono = NewMonooxygenase, idk = I don't know")
            OxAns = input("Oxidative Half Reaction? (etrans, disulfide, htrans, oxidase, mono, newmono, other, or idk)")
            if OxAns == 'exit':
                print("***")
                print("Exited loop at:")
                print(i)
                print(df.at[i, 'pdbcode'])
                print("***")
                break

            elif OxAns == 'htrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'HTransfer'
                df.at[i,'bin'] = 'other'
                df.to_csv(InFile,index=False)

            elif OxAns == 'disulfide':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'DisulfideReduction'
                df.at[i,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'etrans':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'eTransfer'
                df.at[i,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'oxidase':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Oxidase'
                df.at[i,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'mono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'Monooxygenase'
                df.at[i,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'newmono':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'NewMonooxygenase'
                df.at[i,'bin'] = 'other'
                df.to_csv(InFile,index=False)
            elif OxAns == 'idk':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'idk'
                df.at[i,'bin'] = 'idk'
                df.to_csv(InFile,index=False)
            elif OxAns == 'other':
                print("***")
                print("Oxidative Half = "+ OxAns)
                print("***")
                df.at[i,'OxidativeHalf'] = 'other'
                df.at[i,'bin'] = 'other'
                OxOtherDescript = input("Briefly describe or type 'no' and hit ENTER:")
                df.at[i,'OxOther'] = OxOtherDescript
                df.to_csv(InFile,index=False)
            else:
                print("***")
                print("Index Number:")
                print(i)
                print(df.at[i, 'pdbcode'])
                print("Not a valid selection.")
                print("You wrote:"+ OxAns)
                print("Please type: etrans, disulfide, htrans, oxidase, mono, newmono, idk, other, or exit.")
                print("Note: You must type this word exactly with no spaces, then hit ENTER/RETURN")
                print("***")
                break

        else:
            print("***")
            print("Index Number:")
            print(i)
            print(df.at[i, 'pdbcode'])
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
