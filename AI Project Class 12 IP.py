#Types of AI
import pandas as pd
d1={"Branches of AI":["Machine Learning","Deep Learning","Natural Language Processing","Robotics","Expert Systems","Fuzzy logic"],
    "Used In":["Image Recognition","Computer Vision","Speech Recognition","Manufacturing","Predicting Results","Controls Machines"]}
df=pd.DataFrame(d1,index=["X Ray","Object Detection","Language Translator","Logistics Robotics","User Interface","Micro-Controlers"])
print("The index in the above DataFrame depicts Application of various Branches of AI")
print(df)
#CSV File
d1={"Year":[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019],"Number of AI Publications":[1385,1401,1534,1942,1466,1560,4125,6063,10905,9887],
    "Number of AI Journal Publications":[294,462,516,536,681,632,722,961,1375,1553],
    "Patents In AI":[2,5,16,11,15,30,60,92,135,377],"Number of Startups Developing AI Systems":[25,35,40,45,50,70,80,120,180,200]}
df1=pd.DataFrame(d1)
print(df1)

df1.to_csv("D:\\Artificial Intelligence.csv")


AI=pd.read_csv("D:\\Artificial Intelligence.csv")
#Menu Driven Program
print("Menu Driven Program to display graph \n",
      "1. For plotting Line Graph \n",
      "2. For plotting Bar Graph")


ch=int(input("Enter your choice"))
if ch==1:
    import matplotlib.pyplot as plt
    CS=input("Do you want to plot Multiline Graph of All Data inside CSV File with predefined axis and labels Answer in 'Yes' or 'No'")
    if CS=="No":
        print("Enter the type of line graph you want as solid,dashed,dotted,dash-dot")
        A=input("Enter the type of Line Graph")
        B=float(input("Enter the width of line in points i.e float value"))
        C=input("Enter the name of column on x axis whose graph you want")
        D=input("Enter the name of column on y axis whose graph you want")
        I=input("Enter the color of line")
        J=input("Enter the marker to be used")
        K=float(input("Enter the size of marker in float value"))
        L=input("Enter the color of marker")
        M="Increase in",D,"over past years"

        x=AI[C]
        y=AI[D]
        plt.plot(x,y,color=I,linewidth=B,linestyle=A,marker=J,markersize=K,markeredgecolor=L)
        plt.xlabel(C)
        plt.ylabel(D)
        plt.title(M)
        plt.grid(True)
        plt.show()
    elif CS=="Yes":
        C=input("Enter color for first line in line chart")
        Y=input("Enter the type of line graph you want as solid,dashed,dotted,dash-dot")
        K=float(input("Enter the line width in points i.e float value"))
        L=input("Enter the marker you want to be used")
        M=float(input("Enter the size of marker in points i.e float value"))
        P=input("Enter the color of marker")
        print("Plotting The Graph please wait...")
        print("Your Multiline Graph is ready")

        x=AI["Year"]
        y=AI["Number of AI Publications"]
        plt.plot(x,y,color=C,linewidth=K,linestyle=Y,marker=L,markersize=M,markeredgecolor=P)
        x2=AI["Year"]
        y2=AI["Number of AI Journal Publications"]
        D=input("Enter color for second line in line chart")
        plt.plot(x2,y2,color=D,linewidth=K,linestyle=Y,marker=L,markersize=M,markeredgecolor=P)
        x3=AI["Year"]
        y3=AI["Patents In AI"]
        F=input("Enter color for third line in line chart")
        plt.plot(x3,y3,color=F,linewidth=K,linestyle=Y,marker=L,markersize=M,markeredgecolor=P)
        x4=AI["Year"]
        y4=AI["Number of Startups Developing AI Systems"]
        G=input("Enter color for fourth line in line chart") 
        plt.plot(x4,y4,color=G,linewidth=K,linestyle=Y,marker=L,markersize=M,markeredgecolor=P)
        plt.xlabel("Years")
        plt.ylabel("AI Publications, AI Journal Pubications, Patents In AI, Startups Developing Systems")
        plt.title("Increase in AI Publications, AI Journal Pubications, Patents In AI, Startups Developing Systems")
        plt.legend()
        plt.grid(True)
        plt.show()

        
elif ch==2:
    import matplotlib.pyplot as plt
    print("Select \n",
          "1. For Vertical Bar Graph \n",
          "2. For Horizontal Bar Graph \n",
          "3. For Multiple Bar Plot"),
    ch1=int(input("Enter your choice: "))
    if ch1==1:
        A=input("Enter the name of column on x axis whose graph you want: ")
        B=input("Enter the name of column on y axis whose graph you want: ")
        C=float(input("Enter the width of graph in points i.e float value: "))
        D=input("Enter the color for bars")
        M="Increase in",B,"over past 10 years"

        x=AI[A]
        y=AI[B]
        plt.bar(x,y,width=C,color=D)
        plt.xlabel(A)
        plt.ylabel(B)
        plt.title(M)
        plt.show()
        
    elif ch1==2:
        A=input("Enter the name of column on x axis whose graph you want: ")
        B=input("Enter the name of column on y axis whose graph you want: ")
        C=input("Enter the color for bars: ")
        M="Increase in",B,"over past 10 years"

        x=AI[A]
        y=AI[B]
        plt.barh(x,y,align="center",color=C)
        plt.xlabel(A)
        plt.ylabel(B)
        plt.title(M)
        plt.show()
    elif ch1==3:
        print("You have entered a mode to create a multiple bar plot with predefined axis and labels")
        CS=int(input("Enter 1. For Vertical Multiple Bar Plot \n 2. For Horizontal Bar Plot"))
        if CS==1:
            x=AI["Year"]
            y=AI["Number of AI Publications"]
            C=input("Enter color for First Bar in line chart")
            plt.bar(x,y,width=2.0,color=C)
            x2=AI["Year"]
            y2=AI["Number of AI Journal Publications"]
            D=input("Enter color for Second Bar in line chart")
            plt.bar(x2,y2,width=2.0,color=D)
            x3=AI["Year"]
            y3=AI["Patents In AI"]
            F=input("Enter color for Third Bar in line chart")
            plt.bar(x3,y3,width=2.0,color=F)
            x4=AI["Year"]
            y4=AI["Number of Startups Developing AI Systems"]
            G=input("Enter color for Fourth Bar in line chart") 
            plt.bar(x4,y4,width=2.0,color=G)
            plt.xlabel("Years")
            plt.ylabel("AI Publications, AI Journal Pubications, Patents In AI, Startups Developing Systems")
            plt.title("Increase in AI Publications, AI Journal Pubications, Patents In AI, Startups Developing Systems")
            plt.show()

        elif CS==2:
            x=AI["Year"]
            y=AI["Number of AI Publications"]
            C=input("Enter color for First Bar in line chart")
            plt.barh(x,y,align="center",color=C)
            x2=AI["Year"]
            y2=AI["Number of AI Journal Publications"]
            D=input("Enter color for Second Bar in line chart")
            plt.barh(x2,y2,align="center",color=D)
            x3=AI["Year"]
            y3=AI["Patents In AI"]
            F=input("Enter color for Third Bar in line chart")
            plt.barh(x3,y3,align="center",color=F)
            x4=AI["Year"]
            y4=AI["Number of Startups Developing AI Systems"]
            G=input("Enter color for Fourth Bar in line chart") 
            plt.barh(x4,y4,align="center",color=G)
            plt.xlabel("Years")
            plt.ylabel("AI Publications, AI Journal Pubications, Patents In AI, Startups Developing Systems")
            plt.title("Increase in AI Publications, AI Journal Pubications, Patents In AI, Startups Developing Systems")
            plt.show()




                                                                                                                                             
                      #In list there are values seperated by comma
#
def len():
    L1=[]
    x=int(input("Enter the number of words you want to enter \n Don\'t enter more than five. Five is the limit."))
    for i in range(1,x+1):
        print("You have entered the mode to input data")
        y=input("Enter the word")
        L1.append(y)
    print("Retrieving inputted values please wait")
    print(L1)
    print(len(L1>[L1[0]>L1[1]>L1[2]]))
    
    #print(len>L1)
    #for i in x:
    for z in range(0,3):
        P[z]=len(L1[z])
        print(len>len(P[z]))
        
