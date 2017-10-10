from bs4 import BeautifulSoup
import unittest
import requests

# Instr note: the outline comments will stay as suggestions,
# otherwise it's too difficult.
# Of course, it could be structured in an easier/neater way,
# and if a student decides to commit to that, that is OK.

# NOTE OF ADVICE:
# When you go to make your GitHub milestones, think pretty seriously
# about all the different parts and their requirements,
# and what you need to understand.
# Make sure you've asked your questions about Part 2 as much as you need to
# before Fall Break!


# PART 0

try:
    gallery_file = open("gallery.html", "r")
    html = gallery_file.read()
    gallery_file.close()
except:
    newman_taylor_gallery = "http://newmantaylor.com/gallery.html"
    response = requests.get(newman_taylor_gallery)
    html = response.text
    gallery_file = open("gallery.html", "w")
    gallery_file.write(html)
    gallery_file.close()

gallery_soup = BeautifulSoup(html, "html.parser")
img_alt_text_lst = []
imgs = gallery_soup.find_all("img")
for img in imgs:
    alt = img.get("alt", "No alternative text provided!")
    img_alt_text_lst.append(alt)
for element in img_alt_text_lst:
    print(element)

# PART 1

try:
    nps_gov_file = open("nps_gov_data.html", "r")
    html = nps_gov_file.read()
    nps_gov_file.close()
except:
    nps_gov_home = "https://www.nps.gov/index.htm"
    response = requests.get(nps_gov_home)
    html = response.text
    nps_gov_file = open("nps_gov_data.html", "w")
    nps_gov_file.write(html)
    nps_gov_file.close()

state_list = ["Arkansas", "California", "Michigan"]
for state in state_list:
    state_str_lc = state.lower()
    state_str_lc_no_spaces = state_str_lc.replace(" ", "_")
    state_data_suffix = "_data.html"
    state_data_html = state_str_lc_no_spaces + state_data_suffix
    try:
        state_data_file = open(state_data_html, "r")
        html = state_data_file.read()
        state_data_file.close()
    except:
        try:
            nps_gov_file = open("nps_gov_data.html", "r")
            html = nps_gov_file.read()
            nps_gov_file.close()
        except:
            nps_gov_home = "https://www.nps.gov/index.htm"
            response = requests.get(nps_gov_home)
            html = response.text
            nps_gov_file = open("nps_gov_data.html", "w")
            nps_gov_file.write(html)
            nps_gov_file.close()
        nps_gov_soup = BeautifulSoup(html, "html.parser")
        dropdown_class = "dropdown-menu SearchBar-keywordSearch"
        dropdown = nps_gov_soup.find("ul", {"class": dropdown_class})
        dropdown_states = dropdown.find_all("li")
        for dropdown_state in dropdown_states:
            state_link = dropdown_state.find("a")
            state_link_text = state_link.text
            if state_link_text == state:
                state_link_href = state_link.get("href")
                nps_gov_home = "https://www.nps.gov/index.htm"
                nps_state = nps_gov_home + state_link_href
                response = requests.get(nps_state)
                html = response.text
                nps_state_file = open(state_data_html, "w")
                nps_state_file.write(html)
                nps_state_file.close()

# PART 2

# Before truly embarking on Part 2, we recommend you do two things:

# 1. Create BeautifulSoup objects out of all the data you have access to
#       in variables from Part 1
# 2. Do some investigation on those BeautifulSoup objects.
#       What data do you have about each state? How is it organized in HTML?

# HINT: remember the method .prettify() on a BeautifulSoup object --
# might be useful for your investigation!
# So, of course, might be .find or .find_all, etc...

# HINT: Remember that the data you saved is data that includes ALL
# of the parks/sites/etc in a certain state, but you want the class
# to represent just ONE park/site/monument/lakeshore.

# We have provided, in sample_html_of_park.html an HTML file that represents
# the HTML about 1 park. However, your code should rely upon HTML data about
# Michigan, Arkansas, and Califoria you saved and accessed in Part 1.

# However, to begin your investigation and begin
# to plan your class definition, you may want to open this file
# and create a BeautifulSoup instance of it to do investigation on.

# Remember that there are things you'll have to be careful about listed in
# the instructions -- e.g. if no type of park/site/monument is listed in input,
# one of your instance variables should have a None value...





# Define your class NationalSite here:





# Recommendation: to test the class, at various points, uncomment
# the following code and invoke some of the methods / check out the
# instance variables of the test instance saved in the variable sample_inst:

# f = open("sample_html_of_park.html",'r')
# soup_park_inst = BeautifulSoup(f.read(), 'html.parser')
#   (an example of 1 BeautifulSoup instance to pass into your class)
# sample_inst = NationalSite(soup_park_inst)
# f.close()


# PART 3

# Create lists of NationalSite objects for each state's parks.

# HINT: Get a Python list of all the HTML BeautifulSoup instances
# that represent each park, for each state.




# Code to help you test these out:
# for p in california_natl_sites:
# 	print(p)
# for a in arkansas_natl_sites:
# 	print(a)
# for m in michigan_natl_sites:
# 	print(m)



# PART 4

# Remember the hints / things you learned from Project 2 about
# writing CSV files from lists of objects!

# Note that running this step for ALL your data make take a minute or few
# to run -- so it's a good idea to test any methods/functions you write
# with just a little bit of data, so running the program will take less time!

# Also remember that IF you have None values that may occur,
# you might run into some problems and have to debug for where you need
# to put in some None value / error handling!
