import tkinter as tk                    
from tkinter import ttk, messagebox
import webbrowser
import time

class BMI_app:
    def __init__(self, master):
        
        self.master = master
        # giving title to the main window
        self.master.title("BMI_Calculator")
        self.master.geometry("500x500") 
        tabControl = ttk.Notebook(self.master)
        # creating 2 different unit system in 2 tabs
        self.unit_SI = ttk.Frame(tabControl)
        self.unit_Eng = ttk.Frame(tabControl)
        self.more_info = ttk.Frame(tabControl)

        tabControl.add(self.unit_SI, text = "Select SI Unit")
        tabControl.add(self.unit_Eng, text = "Select English Unit")
        tabControl.add(self.more_info, text = "More about BMI")

        tabControl.pack(expand = 1, fill ="both")
        
        #################
        # SI Unit Layout
        #################
        inp_SI_Frame = ttk.Frame(self.unit_SI)
        inp_SI_Frame.pack(anchor = "w")
        ttk.Label(inp_SI_Frame, text = "Type in your info").grid(row = 0, column = 0, padx = 5, pady = 10)
        # input weight section
        ttk.Label(inp_SI_Frame, text = "Weight").grid(row = 1, column = 0, padx = 5, pady = 5)
        self.weight1 = ttk.Entry(inp_SI_Frame, width = 10)
        self.weight1.grid(row = 1, column = 1, padx = 5, pady = 5)
        ttk.Label(inp_SI_Frame, text = "kg").grid(row = 1, column = 2, padx = 5, pady = 5)
        # input height section
        ttk.Label(inp_SI_Frame, text = "Height").grid(row = 2, column = 0, padx = 5, pady = 5)
        self.height1 = ttk.Entry(inp_SI_Frame, width = 10)
        self.height1.grid(row = 2, column = 1, padx = 5, pady = 5)
        ttk.Label(inp_SI_Frame, text = "cm").grid(row = 2, column = 2, padx = 5, pady = 5)
        # clear input button
        ttk.Button(inp_SI_Frame, text = "untype", command = self.clear_SI).grid(row = 3, column = 0, padx = 5, pady = 5)
        # get BMI result button
        ttk.Button(inp_SI_Frame, text = "Get my BMI", command = self.get_BMI_SI).grid(row = 4, column = 0, padx = 10, pady = 5)
        
        #################
        # English Unit Layout
        #################
        inp_Eng_Frame = ttk.Frame(self.unit_Eng)
        inp_Eng_Frame.pack(anchor = "w")
        ttk.Label(inp_Eng_Frame, text = "Type in your info").grid(row = 0, column = 0, padx = 5, pady = 10)
        # input weight section
        ttk.Label(inp_Eng_Frame, text = "Weight").grid(row = 1, column = 0, padx = 5, pady = 5)
        self.weight2 = ttk.Entry(inp_Eng_Frame, width = 10)
        self.weight2.grid(row = 1, column = 1, padx = 5, pady = 5)
        ttk.Label(inp_Eng_Frame, text = "lb").grid(row = 1, column = 2, padx = 5, pady = 5)
        # input height section
        ttk.Label(inp_Eng_Frame, text = "Height").grid(row = 2, column = 0, padx = 5, pady = 5)
        self.height2_1 = ttk.Entry(inp_Eng_Frame, width = 10)
        self.height2_1.grid(row = 2, column = 1, padx = 5, pady = 5)
        ttk.Label(inp_Eng_Frame, text = "ft").grid(row = 2, column = 2, padx = 5, pady = 5)
        self.height2_2 = ttk.Entry(inp_Eng_Frame, width = 10)
        self.height2_2.grid(row = 2, column = 3, padx = 5, pady = 5)
        ttk.Label(inp_Eng_Frame, text = "in").grid(row = 2, column = 4, padx = 5, pady = 5)
        # clear input button
        ttk.Button(inp_Eng_Frame, text = "untype", command = self.clear_Eng).grid(row = 3, column = 0, padx = 5, pady = 5)
        # get BMI result button
        ttk.Button(inp_Eng_Frame, text = "Get my BMI", command = self.get_BMI_Eng).grid(row = 4, column = 0, padx = 10, pady = 5)
        
        ##########
        # more about BMI
        ##########
        ttk.Label(self.more_info, text = "What is BMI", font = 'Helvetica 10 bold').pack(pady = (5,5), anchor = "w")
        ttk.Label(self.more_info, text = "Body mass index (BMI) is a person’s weight in kilograms divided by the square of height in meters. BMI is an inexpensive and easy screening method for weight category—underweight, healthy weight, overweight, and obesity.", wraplengt=450).pack(anchor = "w")
        
        ttk.Label(self.more_info, text = "Child and Teen BMI", font = 'Helvetica 10 bold').pack(pady = (10, 5), anchor = "w")
        ttk.Label(self.more_info, text = "For children and teens, BMI is age- and sex-specific and is often referred to as BMI-for-age.", wraplengt=450).pack(anchor = "w")

        link_1 = ttk.Label(self.more_info, text = "Child and Teen BMI Calculator", font= 'Helvetica 10 underline bold')
        link_1.pack(pady = (10,5), anchor = "w")
        link_1.bind("<Button-1>", lambda e: self.callback("https://www.cdc.gov/healthyweight/bmi/calculator.html"))


    def clear_SI(self):
        ##########
        # clear weight and height input in SI unit tab
        ##########
        self.weight1.delete(0, "end")
        self.height1.delete(0, "end")

    def clear_Eng(self):
        ##########
        # clear weight and height input in English unit tab
        ##########
        self.weight2.delete(0, "end")
        self.height2_1.delete(0, "end")  
        self.height2_2.delete(0, "end") 
    
    def get_BMI_SI(self):
        ##########
        # 1. check if input is valid
        # 2. calculate BMI and show BMI
        # 3. offer option to compare to CDC standard
        ##########
        self.start = time.time()
        try:
            float(self.weight1.get()) or float(self.height1.get())  # valid input
            w_kg = float(self.weight1.get())           # convert string to number
            h_cm = float(self.height1.get()) / 100     # convert string to number
            self.BMI = round(self.BMI_calc(w_kg, h_cm, 1), 2)    # BMI with 2 decimal
            # ttk.Label(self.unit_SI, text = f"Your BMI is {self.BMI}").pack(pady = 10, anchor = "w")
            # compare to CDC standard
            self.compare_BMI(self.unit_SI)

        except ValueError:
            self.clear_SI()
            messagebox.showwarning(title = "Invalid Input", message = "Please check your input. Weight and Height have to be numbers.")

       
    def get_BMI_Eng(self):
        ##########
        # 1. check if input is valid
        # 2. calculate BMI and show BMI
        # 3. offer option to compare to CDC
        self.start = time.time()
        try:
            float(self.weight2.get()) or float(self.height2_1.get()) or float(self.height2_2.get())
            w_lb = float(self.weight2.get())
            h_in = float(self.height2_1.get()) * 12 + float(self.height2_2.get())
            self.BMI = round(self.BMI_calc(w_lb, h_in, 2), 2)
            # compare to CDC standard session
            self.compare_BMI(self.unit_Eng)
        except ValueError:
            self.clear_Eng()
            messagebox.showwarning(title = "Invalid Input", message = "Please check your input. Weight and Height have to be numbers.")

    def compare_BMI(self, tab):
        ########
        # new frame ask for BMI comparison with CDC
        ########
        #compFrame = ttk.Frame(tab)
        self.compFrame = tk.Toplevel(self.master)
        self.compFrame.geometry("500x500")
        ttk.Label(self.compFrame, text = f"Your BMI is {self.BMI}").pack(pady = 5, anchor = "w")
        self.end = time.time()
        time_lapsed = (self.end - self.start) * 1000
        ttk.Label(self.compFrame, text = f"App response time is {time_lapsed} in ms").pack(pady = (20, 0), anchor = "w")
        # compare to CDC standard
        ttk.Label(self.compFrame, text = "Compare your BMI with CDC standard to see if your weight is healthy").pack(pady = (20, 0), anchor = "w")
        ttk.Label(self.compFrame, text = "Note: A new window will open.").pack(anchor = "w")
        ttk.Button(self.compFrame, text = "Weight Status", command = self.show_BMI_std).pack(pady = 5, anchor = "w")

    def show_BMI_std(self):
        ########
        # compare BMI with CDC standard
        ########
        newWindow = tk.Toplevel(self.compFrame)
        newWindow.geometry("500x500") 
        w_status = "NA"
        # compare BMI with CDC standard
        if self.BMI < 18.5:
            w_status = "Underweight"
        elif (self.BMI >= 18.5) & (self.BMI <= 24.9):
            w_status = "Healthy Weight"
        elif (self.BMI > 24.9) & (self.BMI <= 29.9):
            w_status = "Overweight"
        elif self.BMI > 29.9:
            w_status = "Obese"
        
        # show weight status results
        ttk.Label(newWindow, text = f"Your BMI is {self.BMI}. According to CDC standard, your weight status is {w_status}").pack(pady = 20, anchor='w')
        ttk.Label(newWindow, text = "CDC standard").pack(pady = 5, anchor = "center")
        
        # show CDC standard in new frame
        table = ttk.Frame(newWindow)
        table.pack()
        lst = [("BMI", "Weight Status"),("Below 18.5", "Underweight"),("18.5 - 24.9", "Healthy Weight"), ("25.0 - 29.9", "Overweight"), ("30.0 and Above", "Obesity")]
        for i in range(5):
            for j in range(2):
                cell = tk.Entry(table)
                cell.grid(row = i + 3, column = j)
                cell.insert("end", lst[i][j])

        # links to related resources
        resource = ttk.Frame(newWindow)
        resource.pack()
        ttk.Label(resource, text = "Want to know how to keep healthy weight? Check following resources.",).pack(pady = (30, 0), anchor = "w")
        ttk.Label(resource, text = "! Warning: Following link will navigate to external webpage!", font = 'Helvetica 10 bold', foreground = "#FF0000").pack(pady = (0, 10), anchor = "w")
        link1 = ttk.Label(resource, text = "Losing Weight", font= ('Helvetica 10 underline'))
        link1.pack(pady = (0,5), anchor = "w")
        link1.bind("<Button-1>", lambda e: self.callback("https://www.cdc.gov/healthyweight/losing_weight/index.html"))
        link2 = ttk.Label(resource, text = "Healthy Eating for a Healthy Weight", font= ('Helvetica 10 underline'))
        link2.pack(pady = (0,5), anchor = "w")
        link2.bind("<Button-1>", lambda e: self.callback("https://www.cdc.gov/healthyweight/healthy_eating/index.html"))
        link3 = ttk.Label(resource, text = "Physical Activity for a Healthy Weight", font= ('Helvetica 10 underline'))
        link3.pack(pady = (0,5), anchor = "w")
        link3.bind("<Button-1>", lambda e: self.callback("https://www.cdc.gov/healthyweight/physical_activity/index.html"))
        return None
    
    def callback(self, url):
        webbrowser.open_new_tab(url)

    def BMI_calc(self, w, h, unit_opt):
        if unit_opt == 1:
            return w / (h**2)
        elif unit_opt == 2:
            return w / (h**2) * 703
        return None

    def tab_layout(self, tab, w_unit, h_unit):
        # input section  
        ttk.Label(tab, text = "Type in your info").grid(row = 0, column = 0, padx = 5, pady = 10)
        # input weight
        ttk.Label(tab, text = "Weight").grid(row = 1, column = 0, padx = 5, pady = 5)
        self.weight = ttk.Entry(tab, width = 10)
        self.weight.grid(row = 1, column = 1, padx = 5, pady = 5)
        ttk.Label(tab, text = w_unit).grid(row = 1, column = 2, padx = 5, pady = 5)
        ttk.Button(tab, text = "untype", command = self.clear_text).grid(row = 1, column = 3, padx = 5, pady = 5)
        # input height
        ttk.Label(tab, text = "Height").grid(row = 2, column = 0, padx = 5, pady = 5)
        height = ttk.Entry(tab, width = 10)
        height.grid(row = 2, column = 1, padx = 5, pady = 5)
        ttk.Label(tab, text = h_unit).grid(row = 2, column = 2, padx = 5, pady = 5)
        if h_unit == "ft":
            height2 = ttk.Entry(tab, width = 10)
            height2.grid(row = 2, column = 3, padx = 5, pady = 5)
            ttk.Label(tab, text = "in").grid(row = 2, column = 4, padx = 5, pady = 5)
        ttk.Button(tab, text = "Get my BMI").grid(row = 3, column = 0, padx = 10, pady = 5)

        self.x = ttk.Entry(tab, width = 10)
        self.x.grid(row = 5, column = 1, padx = 5, pady = 5)

root = tk.Tk()

BMI_app(root)
root.mainloop()