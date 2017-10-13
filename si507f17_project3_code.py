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


def get_nps_homepage_and_state_html(state_str):
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
    state_str_lc = state_str.lower()
    state_str_lc_no_spaces = state_str_lc.replace(" ", "_")
    state_data_suffix = "_data.html"
    state_data_html = state_str_lc_no_spaces + state_data_suffix
    try:
        state_data_file = open(state_data_html, "r")
        html = state_data_file.read()
        state_data_file.close()
    except:
        dropdown_class = "dropdown-menu SearchBar-keywordSearch"
        dropdown = nps_gov_soup.find("ul", {"class": dropdown_class})
        for dropdown_li in dropdown.children:
            try:
                state_link = dropdown_li.contents[0]
                state_link_text = state_link.text
                if state_link_text == state_str:
                    state_link_href = state_link.get("href")
                    nps_gov_prefix = "https://www.nps.gov"
                    nps_state = nps_gov_prefix + state_link_href
                    response = requests.get(nps_state)
                    html = response.text
                    nps_state_file = open(state_data_html, "w")
                    nps_state_file.write(html)
                    nps_state_file.close()
            except:
                pass

    print1 = "Not a fruitful function, but your NPS homepage HTML file "
    print2 = "and your NPS state HTML file are ready\n"
    print(print1 + print2)

get_nps_homepage_and_state_html("Arkansas")
get_nps_homepage_and_state_html("California")
get_nps_homepage_and_state_html("Michigan")

# PART 2


class NationalSite(object):
    def __init__(self, site_soup):
        self.name = site_soup.find("h3").contents[0].text
        self.location = site_soup.find("h4").text
        if site_soup.find("h2").text:
            self.type = site_soup.find("h2").text
        else:
            self.type = None
        if site_soup.find("p").text:
            self.description = site_soup.find("p").text.strip()
        else:
            self.description = ""
        all_links = site_soup.find_all("a")
        for link in all_links:
            if "basicinfo" in link.get("href"):
                    basic_info_link = link.get("href")
        self.basic_info_link = basic_info_link

    def __str__(self):
        return self.name + " | " + self.location

    def __contains__(self, input_str):
        return input_str in self.name

    def get_mailing_address(self):
        site_name_lower = self.name.lower()
        site_name_lower_underscore = site_name_lower.replace(" ", "_")
        basic_info_html_suffix = "_basic_info.html"
        html_name = site_name_lower_underscore + basic_info_html_suffix
        try:
            site_basic_info_file = open(html_name, "r")
            html = site_basic_info_file.read()
            site_basic_info_file.close()
        except:
            response = requests.get(self.basic_info_link)
            html = response.text
            site_basic_info_file = open(html_name, "w")
            site_basic_info_file.write(html)
            site_basic_info_file.close()
        info_soup = BeautifulSoup(html, "html.parser")
        try:
            address = info_soup.find("div", {"itemprop": "address"})
            address_str = ""
            address_lst = []
            address_children = address.contents
            for address_child in address_children:
                try:
                    to_add = address_child.text.strip()
                    if to_add != "":
                        address_lst.append(to_add)
                except:
                    pass
            for address_element in address_lst[:-1]:
                address_str = address_str + address_element + " / "
            address_str = address_str + address_lst[-1]
            return address_str
        except:
            return ""

# PART 3


def create_state_nationalsites_list(state_str):
    state_str_lc = state_str.lower()
    state_str_lc_no_spaces = state_str_lc.replace(" ", "_")
    state_data_suffix = "_data.html"
    state_data_html = state_str_lc_no_spaces + state_data_suffix
    state_data_file = open(state_data_html, "r")
    html = state_data_file.read()
    state_data_file.close()

    state_sites_list = []
    state_soup = BeautifulSoup(html, "html.parser")
    state_sites_ul = state_soup.find("ul", {"id": "list_parks"})
    for state_site_li in state_sites_ul.children:
        try:
            site_object = NationalSite(state_site_li)
            state_sites_list.append(site_object)
        except:
            pass
    return state_sites_list

arkansas_natl_sites = create_state_nationalsites_list("Arkansas")
california_natl_sites = create_state_nationalsites_list("California")
michigan_natl_sites = create_state_nationalsites_list("Michigan")

# PART 4

# Remember the hints / things you learned from Project 2 about
# writing CSV files from lists of objects!

# Note that running this step for ALL your data make take a minute or few
# to run -- so it's a good idea to test any methods/functions you write
# with just a little bit of data, so running the program will take less time!

# Also remember that IF you have None values that may occur,
# you might run into some problems and have to debug for where you need
# to put in some None value / error handling!
