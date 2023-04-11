

class ROI_calculator():
    def __init__(self, monthly_Icome,Total_Investments ,monthly_Expenses):
        self.monthly_Icome = monthly_Icome
        self.Total_Investments = Total_Investments
        self.monthly_Expenses = monthly_Expenses
                  
    def ROI(self):
        yearly_Income=self.monthly_Icome*12
        yearly_Expenses=self.monthly_Expenses *12
        yearly_net_income=yearly_Income-yearly_Expenses
        
        roi_= yearly_net_income/self.Total_Investments
        #return roi_
        print("your ROI is ",roi_*100,"%")
    

my_roi = ROI_calculator(2000, 40000,1600)
my_roi.ROI()