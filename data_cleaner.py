def data_cleaner():
    import pandas as pd
    data = pd.read_csv("PFcsv.csv")
    import datetime
    classification = {}

    classification["Grocery"] = ["singhshindu", "grofers", "swiggyinstamart", "grocery", "licious", "zepto", "lemarche"]
    classification["Outside Food"] = ["kesharwani", "guddukumar", "swiggyupi","eatsure","zomato", "outsidefood", "thirdwave", "swiggystores"]
    classification["Fuel/Car Maintainence/Challans"] = ["tejenrajbanshi","petrol","fuel"]
    classification["Purchases/Personal/Outings"] = ["bookmyshow", "cinepolis","pvr","youtube","googleplay","spotify","steamgames", "netflix","hotstar", "personal", "alochol"]
    classification["Investments"] = ["zerodha","indianclearingcorp"]
    classification["Credit Card"] = ["creditcard", "cred"]
    classification["House"] = ["maid","cook","gas","electricity","waterpurifier","waterfilter", "house", "deviduttjoshi"]
    classification["Paytm Wallet Expense"] = ["add money to wallet"]

    print(len(data["Narration"]))


    i = len(data["Review Status"][data["Review Status"]==True])

    while i<len(data["Narration"]):
        narration = data["Narration"][i]
        narration = "".join("".join(str(narration).lower().split("-")).split(" "))
        data["Review Status"][i] = True
        gate = False

        if "deviduttjoshi" in narration:
            #print("hiii", narration, "AMT:",data['Withdrawal Amt.'][i])
            if data['Withdrawal Amt.'][i] == 40000:
                #print("hiii", narration)
                data.loc[i, 'Withdrawal Amt.'] = 13500
                #print("hiii NEWWWWWW", narration, "AMT:",data['Withdrawal Amt.'][i])
            else:
                data.loc[i, 'Withdrawal Amt.'] /= 3
                #print("hiii NEWWWWWW", narration, "AMT:",data['Withdrawal Amt.'][i])

        for m,n in classification.items():
            if str(data["Expense Classification"][i])  == "nan":
                if gate == False:
                    for m,n in classification.items():
                        #if gate == False:
                            for dict_element in n:
                                if dict_element in narration:
                                    data["Expense Classification"][i] = m
                                    #print(dict_element, "-----------", narration)
                                    #gate = True
                                    #print("HI  ", m)
                                    # if gate==True:
                                    #     break
                            
                                
        i+=1

    #data.to_csv("Cleaned_CSV.csv")
    #data['Date'].apply(lambda x: (datetime.datetime(x)))
    def date_cleaner(date_):
        if type(date_) == str:
            return datetime.datetime(int('20'+date_.split("/")[2]), int(date_.split("/")[1]), int(date_.split("/")[0]))
        else:
            return ""



    data['Date'] = data['Date'].apply(date_cleaner)
    #data['Date'] = pd.to_datetime(data["Date"])
    data['Date'][2]

    # def null_finder(date_):
    #     if type(date_) == pd.Timestamp:
    #         return date_
    #     else:
    #         return '11-11-1900'


    #data['Date'] = data['Date'].apply(null_finder)


    #data['Date'] = pd.to_datetime(data["Date"]).dt.strftime("%Y-%m-%d")

    #data['Date'].apply()
    data= data.drop(['Value Dt', 'Date_Value', 'Chq./Ref.No.', 'Review Status', 'Closing Balance'], axis=1)
    for val in ['Withdrawal Amt.', 'Deposit Amt.']:
        data[f'{val}'].apply(lambda x: float(x))

    print("TYPE:: ", type(data['Date'][0]))
    data.to_csv("Cleaned_CSV.csv", index=False)