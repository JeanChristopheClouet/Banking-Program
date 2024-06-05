import csv
import tkinter

class Account():
    '''A Class meant to facilitate personal money management.'''

    def __init__(self, name, initial_deposit=0) -> None:
        
        
        self.name = name # name of the object
        self.filename=f"{str(name)}.csv" # file containing the transactions
        

    def return_balance(self)->int:
        '''
        Returns balance by adding up every withdrawal and deposit amount from the file.
        '''

        # balance value held in memory
        balance = 0
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file,quoting=csv.QUOTE_NONNUMERIC)
                for line in reader:
                    # pass if empty list
                    if any(line)==False:pass
                    else:
                        balance+=float(line[0])
        except:pass

        return int(balance)


    def withdraw(self, a, p):
        '''
        Writes negative amount and product to file.
        '''
        with open(self.filename, 'a', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow((-a, p))        
    

    def deposit(self, a, p):
        '''
        Writes amount and product to file.
        '''
        with open(self.filename, 'a', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow((a, p))        


    def gui(self):
        '''
        Setup a GUI for navigating through the account comfortably.
        '''

        # functions
        def show_balance():
            '''
            Displays user balance on the GUI window by calling self.balance() in the process.
            '''
            balance_str = str(self.return_balance())
            balance_widget=tkinter.Label(window, text=balance_str)
            balance_widget.grid(column=1, row=1, sticky='ew', padx=50)
        

        def withdraw1(): # TODO replace by _withdraw
            '''
            Calls self.withdraw on the variables bound to the entry boxes next to the withdraw label
            except it is raised when clicking the 'ok' button widget'''
            
            # initializing variables

            amount = float(withdraw_amount_var.get())

            # code below doesn't work
            try:
                amount = float(withdraw_amount_var.get())
            except:
                pass
                # add pop up text for a few seconds that goes like 'invalid value for whatever'

            product = withdraw_product_var.get()

            # code below doesn't work
            try:
                product = withdraw_product_var.get()
            except:
                error_message = tkinter.Label(window, text='Please enter valid input')
                error_message.grid(row=3, column=4)
                pass
                # add pop up text for a few seconds that goes like 'invalid value for whatever'
            
            # writing values to file
            try:
                self.withdraw(amount, product)  
            except: 
                error_message = tkinter.Label(window, text='Please enter valid input')
                error_message.grid(row=3, column=4)

                pass

            withdraw_amount_var.set('')
            withdraw_product_var.set('')


        def deposit1(): # TODO replace by _withdraw
            '''
            Calls self.deposit on the variables bound to the entry boxes next to deposit label
            except it is raised when clicking the 'ok' button widget
            '''
            
            # initializing variables
            amount = float(deposit_amount_var.get())

            # code below doesn't work
            try: 
                amount = float(deposit_amount_var.get())
            except:
                error_message = tkinter.Label(window, text='Please enter valid input')
                error_message.grid(row=5, column=4)
                
                # add pop up text for a few seconds that goes like 'invalid value for whatever'
            
            product = deposit_product_var.get()
            
            # code below doesn't work
            try:
                product = deposit_product_var.get()
            except:
                error_message = tkinter.Label(window, text='Please enter valid input')
                error_message.grid(row=5, column=4)
                
                # add pop up text for a few seconds that goes like 'invalid value for whatever'
         

            # writing values to file
            try:
                self.deposit(amount, product)
            except:
                pass

            # setting the deposit variable empty once 
            deposit_amount_var.set('')
            deposit_product_var.set("")


        # setting up the window
        window = tkinter.Tk() 
        window.geometry('700x455')
        window.title('Acccount')


        # configuring rows and columns
        # window.columnconfigure(1, weight=1)
        # window.columnconfigure(2, weight=1)
        # window.rowconfigure(2, weight=1)
        # window.rowconfigure(3, weight=1)
        # window.rowconfigure(4, weight=1)
        

        #----------------- GUI window initialization ----------------------
        # Welcome
        welcome = tkinter.Label(window, text=f"Welcome {self.name}")
        welcome.grid(column=1, row=0, sticky='nsew')

        view_balance = tkinter.Button(window, text='View Balance', command=show_balance, relief='groove')
        view_balance.grid(column=0, row=1, sticky='ew', padx=50)




        # ---------------------- withdraw related widgets ----------------------

        # withdraw text
        withdraw = tkinter.Label(window, text='Withdraw')
        withdraw.grid(column=0, row=3, sticky='nsew')

        # product :
        withdraw_product_label = tkinter.Label(window, text='product:')
        withdraw_product_label.grid(column=1, row=2)

        # amount :
        withdraw_amount_label = tkinter.Label(window, text='amount:')
        withdraw_amount_label.grid(column=2, row=2)


        # binding the entry boxes with the variables

        withdraw_product_var = tkinter.StringVar()
        withdraw_product_en = tkinter.Entry(window, textvariable=withdraw_product_var)
        withdraw_product_en.grid(column=1, row=3)

        withdraw_amount_var = tkinter.StringVar()
        withdraw_amount_en = tkinter.Entry(window, textvariable=withdraw_amount_var)
        withdraw_amount_en.grid(column=2, row=3)

        withdraw_ok = tkinter.Button(window, text='OK', command=withdraw1, relief='groove')
        withdraw_ok.grid(column=3, row=3, sticky='ew', padx=50)




        # ---------------------- deposit related widgets ----------------------

        deposit=tkinter.Label(window, text='Deposit')
        deposit.grid(column=0, row=5, sticky='nsew')

        # product :
        deposit_product_label = tkinter.Label(window, text='product:')
        deposit_product_label.grid(column=1, row=4)
        
        # amount :
        deposit_amount_label = tkinter.Label(window, text='amount:')
        deposit_amount_label.grid(column=2, row=4)


        # binding the entry boxes with the variables

        deposit_product_var = tkinter.StringVar()
        deposit_product_en = tkinter.Entry(window, textvariable=deposit_product_var)
        deposit_product_en.grid(column=1, row=5)

        deposit_amount_var = tkinter.StringVar()
        deposit_amount_en = tkinter.Entry(window, textvariable=deposit_amount_var)
        deposit_amount_en.grid(column=2, row=5)

        deposit_ok = tkinter.Button(window, text='OK', command=deposit1, relief='groove')
        deposit_ok.grid(column=3, row=5, sticky='ew', padx=50)

        window.mainloop()



test = Account('Bob', 150)
test.deposit(20, 'grandma gift')
test.withdraw(50, 'video games')
test.gui()

 
# 09.12.2022 - > set up tkinter.Tk() object and make it pop up
# 09.13.2022 - > give it a name and add a label inside
# 09.14.2022 -> use grid() geometry manager to move 'welcome' in the middle of the window
# 09.15.2022 -> add labels and configure rows
# 09.16.2022 -> add buttons and bind its pressing to a function to show balance
#            -> fix the problem of 'welcome' moving to the right when balance pops
# 09.17.2022 -> set up the entries and labels that specify what to type, change button relief
# 09.18.2022 -> add ok buttons, figure out how to retrieve a string passed to an entry widget by the user
# 09.19.2022 -> bind ok buttons with functions meant to append a tuple to transactions and to modify balance
# 09.20.2022 -> remove 0 from entry boxes and set the default value inside to ''.
# 09.23.2022 -> transactions are stored to a file on the hard drive! Entry boxes turn blank after pressing the respective ok buttons.
# 09.27.2022 -> implement create_balance() which computes balance based on values from the file storing transactions.
# 09.28.2022 -> write documentation for all classes and functions (except __init__). 
# 10.01.2022 -> document functions and optimise withdraw1 & deposit1 code.
# 10.02.2022 -> handle the scenario where invalid values are entered by the user.
# 10.04.2022 -> display error message if invalid input is entered.
# ------------------------------------------------------------------------------------
# link for grid() documentation
#https://www.pythontutorial.net/tkinter/tkinter-grid/