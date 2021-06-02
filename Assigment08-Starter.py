# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# DFerenczy,5.31.2021,Modified code to complete assignment 8
# DFerenczy,5.31.2021,Added Product class code
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'ProductPriceList.txt'
lstWorkingList = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DFerenczy,6.1.2021,Modified code to complete assignment 8
    """

    # --Fields--
    # strProductName = ''
    # floatProductPrice = 0.00

    # -- Constructor --
    def __init__(self, product_name='', product_price=0.00):
        # -- Attributes --
        self.ProductName = product_name
        self.ProductPrice = product_price

    # -- Properties --
    @property  # DON'T USE NAME for this directive!
    def product_name(self):  # (getter or accessor)
        return str(self.product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property  # DON'T USE NAME for this directive!
    def product_price(self):  # (getter or accessor)
        return str(self.product_price).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric():
            self.__product_price = value
        else:
            raise Exception("Please enter a valid price")

    # -- Methods --

    def __str__(self):
        return '{self.ProductName}, ${self.ProductPrice}'.format(self=self)

# --End of class--

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DFerenczy,6.1.2021,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into objects that are stored in a list

        :param file_name: (string) with name of file:
        :param list_of_objects: (list) you want filled with file data:
        :return: (list) of objects
        """
        global lstWorkingList
        lstWorkingList = []
        file = open(file_name, "r")
        for line in file:
            name, cost = line.split(",")
            obj = Product(name, cost)
            lstWorkingList.append(obj)
        file.close()
        return lstWorkingList

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Write data from a list of objects to a file

        :param list_of_product_objects: (list) list you want to write from
        :param file_name: (string) with name of file:
        :return: (list) of dictionary rows
        """
        txt_file = open(file_name, "w")
        for row in list_of_product_objects:
            item_name = row.ProductName.strip()
            item_cost = row.ProductPrice.strip()
            txt_row = f'{item_name},{item_cost}\n'
            txt_file.write(txt_row)
        txt_file.close()
        print("Save Successful!")
        return list_of_product_objects


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring

    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Data
        2) Add a New Product
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Items Are: *******")
        for item in list_of_rows:
            print(str(item.__str__()).strip())
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_cost():
        """ Gets a priority and task input from the user

        :return: string
        """
        global lstWorkingList
        ProductName = input("Enter a Product to Add: ")
        ProductCost = input("Enter the Cost of the Product: ")
        lstWorkingList.append(Product(ProductName, ProductCost))
        return lstWorkingList

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
lstWorkingList = FileProcessor.read_data_from_file(strFileName)

while True:
    IO.print_menu_Tasks()  # Show user a menu of options
    strChoice = IO.input_menu_choice()  # Get user's menu option choice

    if strChoice == '1':
        IO.print_current_Tasks_in_list(lstWorkingList)  # Show user current data in the list of product objects
        IO.input_press_to_continue()

    if strChoice == '2':
        IO.input_new_product_and_cost()  # Let user add data to the list of product objects
        IO.input_press_to_continue()

    if strChoice == '3':
        FileProcessor.save_data_to_file(strFileName, lstWorkingList)  # let user save current data to file and exit
        # program
        IO.input_press_to_continue()

    if strChoice == '4':
        print("Goodbye!")
        break

    else:
        print("Please enter a valid number between 1 and 4")

# Main Body of Script  ---------------------------------------------------- #
