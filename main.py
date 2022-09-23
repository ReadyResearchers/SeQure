# Tool to grade web applications based on code
# and potential for vulnerabilities

from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from urllib.parse import urljoin
import os

def get_all_forms(url):
    """Given a url, it returns all forms from the HTML content"""
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Extracts all possible useful info about an HTML form"""
    details = {}
    # get the form action (target url)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc)
    method = form .attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    # construct the full url
    target_url = urljoin(url, form_details["action"])
    # get the inputs
    inputs = form_details["inputs"]
    data = {} 
    for input in inputs:
        # replace all text and search values with 'value'
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            # if input name and value are not None, 
            # then add them to the data of form submission
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        # GET request
        return requests.get(target_url, params=data)

def scan_xss(url):
    """
    Given a `url`, it prints all XSS vulnerable forms and 
    returns True if any is vulnerable, False otherwise
    """
    # get all the forms from the URL
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('hi')</scripT>" # script 1
    js_script2 = "<scr><script><ipt>alert('hello')</scripT>" # script 2
    # returning value
    is_vulnerable = False
    # iterate over all forms
    for form in forms: # for loop for script 1
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = print(f"[+] {True}. One or more scripts passed.\n")
            # won't break because we want to print other available vulnerable forms
            
    for form in forms: # for loop for script 2
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script2).content.decode()
        if js_script2 in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = print(f"[+] {True}. One or more scripts passed.")
    return is_vulnerable

# this is the sql scan function
def scan_sql(url):
    is_vulnerable = False
    # test on url
    for c in "\"'":
        #add quote/double quote character to the URL
        new_url = f"{url}{c}"
        print("[!] Trying", new_url)
        # make the HTTP request
        res = s.get(new_url)
        if is_vulnerable(res):
            # SQL Injection vulnerability on the URL itself, 
            # no need to proceed for extracting forms and submitting them
            print("[+] SQL Injection vulnerabilty detected, link: ", new_url)
            return
    # test on HTML forms
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        for c in "\"'":
            #the data body we want to submit
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["value"] or input_tag["type"] == "hidden":
                    # any input form that has some value or hidden,
                    # just use it in the form body
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    # all others except submit, use some junk data with special character
                    data[input_tag["name"]] = f"test{c}"
            # join the url with the action (form request URL)
            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["method"] == "get":
                res = s.get(url, params=data)
            # test whether the resulting page is vulnerable
            if is_vulnerable(res):
                print("[+] SQL Injection vulnerability detected, link: ", url)
                print("[+] Form: ")
                pprint(form_details)
                break

# this is the main function
if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    print("[+] Welcome to SeQure!\n")
    url = "https://xss-game.appspot.com/level1/frame"
    url2 = "https://lex.chompe.rs/?page_id=2"
    
    print(scan_xss(url))
    print("\n-------------------------------------------------")
    print(scan_xss(url2))
    
# Below are the links I am testing: 
# https://lex.chompe.rs/?page_id=2
# https://xss-game.appspot.com/level1/frame
