from flask import Flask, jsonify, render_template, url_for, request, redirect
from time import sleep
from threading import Thread
from flask_cors import CORS
import json
import requests
from webdriver_manager.firefox import GeckoDriverManager
import img2pdf
from langdetect import detect
from PIL import Image
import re
import string
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from textblob import TextBlob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from deep_translator import GoogleTranslator

# No getting front.

# this one now.
import traceback

def hasCss(xpath):
    try:
        driver.find_element_by_css_selector(xpath)
        return True
    except:
        return False
    
    
def hasXpath(xpath):
    try:
       
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

def hasClass(xpath):
    try:
        driver.find_element_by_class_name(xpath)
        return True
    except:
        return False
    
def compute(chosen_word,interval,start,end_year,total_books,keywords,analysis_type,language):

    interval = int(interval)
    start = int(start)
    
    end_year = int(end_year)
    total_books = int(total_books)
    screenshot_max = 5
    Image.MAX_IMAGE_PIXELS = None
    
    
    # Since the start and end dates above will be changed, we will store the start
    # and end dates into another variable so that if the program runs into an error,
    # it can boot back up.
    
    start_date = start
    end_date = end_year
    
    # If there exists more than one keyword, then we are going to increment the number of screenshots we take for a given
    # book, and increase the number of books that we go through, the reason for this being that not all of the 
    # screenshots are going to contain the word we are seeking to understand (some will solely be segments
    # of the book that contain the keyword(s)).
    
    print(f"Entered word is: {chosen_word.capitalize()} \n")
    print(f"Entered start date is: {start} \n")
    print(f"Entered interval is: {interval} \n")
    print(f"Entered end date is: {end_year} \n")
    
  
    
    if (language !=""):
        print(f"Entered language is : {language} \n")
        is_en=False
    
    else:
        language = "en"
        is_en = True
        
        
    if (analysis_type!=""):
        print(f"Entered analysis type is: {analysis_type.capitalize()} \n")   

    if (keywords!=""):
        
        print(f"Entered keyword(s) is/are: {keywords}\n")
        print(f"Entered total books is: {total_books}, but the program will go through {total_books*2} because you entered another keyword \n")
        
        if (total_books<20):
            
            total_books = total_books*2
            
        chosen_word += " "+ keywords
        screenshot_max = 10

    else:
        
        print(f"Entered total_books is: {total_books} \n")
    
    print("If any of these variables are incorrect, please close the pop-browser and re-enter the variables you'd like to change.")   
    
    # This function will change the contrast of the image, to make the background segment of the 
    # image not visible.
    
    def change_contrast(img, level):
        factor = (300 * (level + 450)) / (370 * (259 - level))
        def contrast(c):
            return 128 + factor * (c - 150)
        return img.point(contrast)
    
    # This function will merge all of the taken screenshots for a given interval
    # together into one image.
    
    def merge_images_vertically(imgs):

        widths, heights = zip(*(i.size for i in imgs))
        width_of_new_image = max(widths)  #take minimum width
        height_of_new_image = sum(heights)

        new_im = Image.new('RGB', (width_of_new_image, height_of_new_image))
        new_pos = 0
        
        for im in imgs:
            new_im.paste(im, (0, new_pos))
            new_pos += im.size[1] #position for the next image
        new_im.save('mergedBooks.png') #change the filename if you want

   
    error_found = False
    
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    try:
        driver.get("https://books.google.com/")
        driver.find_element_by_css_selector('#oc-search-input').send_keys(chosen_word)
        driver.find_element_by_css_selector("#oc-search-button > input:nth-child(1)").click()
        decade_count = 0

        # These three lists initialize the lists that will store decades, hyperlinks, 
        # and titles, and used later on to create graphs.

        decade_list = []
        hyperlink_list = []
        title_list = []
        books_entered = []
       
        # curr_year will be the variable that is the end of the current interval that we are looking
        # at. 

        curr_year = int(start) + int(interval)

        prev = start
        
        decade_list.append(prev)
        
        
        book_name = []




    # Iterates through this loop until the year that we are looking for has been reached.

        while (end_year>=curr_year):

            end_of_page = False

            decade_list.append(curr_year)

            c=0
            break_point = []

            sleep(2) 

            if (prev == start):

                view = driver.find_elements_by_class_name("KTBKoe")[0]
                view.click()

                driver.find_element_by_css_selector("div.EwsJzb:nth-child(1) > g-menu:nth-child(1) > g-menu-item:nth-child(2) > div:nth-child(1) > a:nth-child(1)").click()
                
                sleep(2)
                
                if hasCss(".std > a:nth-child(1)"):
                    driver.find_element_by_css_selector("#oc-search-button > input:nth-child(1)").click()
      
                sleep(1)
        
                if (analysis_type!="M-magazine, B-book, N-newspapers" and analysis_type!=""):
            
                    if (analysis_type.lower() == "m" or analysis_type.lower() == "b" or analysis_type.lower() == "n"):
                       
                        driver.find_element_by_css_selector("#hdtbMenus > span:nth-child(3) > g-popup:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
                        
                       
                        if (analysis_type.lower() == "b"):
                                                            
                            driver.find_element_by_xpath("/html/body/div[6]/div/div[6]/div/g-menu/g-menu-item[2]/div/a").click()
                        
                        elif (analysis_type.lower() == "m"):
                            
                            driver.find_element_by_xpath("/html/body/div[6]/div/div[6]/div/g-menu/g-menu-item[3]/div/a").click()
                            
                
                        else:
                            driver.find_element_by_xpath("/html/body/div[6]/div/div[6]/div/g-menu/g-menu-item[4]/div/a").click()
                            
                
            
                    else:
                        print("Your analysis entry was invalid, the program will continue.")
                        print("If you wish to get results only for , please close the window and enter a valid entry.")


            
            print(f"For this iteration, we will go through {prev} - {curr_year}")

            sleep(3)
            date=driver.find_elements_by_class_name("KTBKoe")[2]
            date.click()

            custom = driver.find_element_by_css_selector("div.EwsJzb:nth-child(1) > g-menu:nth-child(1) > g-menu-item:nth-child(5) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
            custom.click()

            sleep(2)

            driver.find_element_by_css_selector("#OouJcb").send_keys(prev)
            driver.find_element_by_css_selector("#rzG2be").send_keys(curr_year-1)
            driver.find_element_by_css_selector(".Ru1Ao").click()


            page=2
            num_image=0


            authorList = []
            tmpHyper = []
            tmpTitle = []

        
            while (len(tmpHyper)<total_books and end_of_page == False):
                
                
                
                sleep(1)
                num_books = len(driver.find_elements_by_class_name("Yr5TG"))
                
                print(f"Total number of books found for Page {page-1} is {num_books}.")
                
               
                
                
                
  
        # This counts the number of books and the variable count is
        # counting the iteration number.

        # The program will only do this once the crawler
        # has arrived to a new page.



        # Book count will keep track of which book we are on on the
        # page, and elems will contain all of the links to the books
        # that we will use to enter each book.

                book_count=0
                sleep(1)
                hyp_count = 1


            # Then, the program will loop through all of the found books here.
            # Check if we have seen this book already ; we will do this by checking if the book name exists already in the book_name
                
                tmp = 0
                curr = 0

                
               
                
                initial_scroll_height = 490
                
               
                for i in range(1,num_books):
                    
                    #if (is_en==False):
                        #file = open(f"result{decade_count}.txt","w")
                
                
                   
                    same_author = False

                    if (num_books==0):
                        end_of_page = True
                        break


                    isValid = False

                    in_list = True

                    sleep(2)  


                    
                    print(initial_scroll_height)
                    found = True 

                    driver.switch_to.default_content()
                    
                    
                    
                    if (i==1):
                
                        sleep(2)
                        
                        try:
                            sleep(2)                                   
                            elem = driver.find_element_by_xpath("/html/body/div[6]/div/div[10]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/a/h3")
                        
                        except Exception:
                            try:
                                sleep(2)    
                                elem = driver.find_element_by_xpath("/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div[2]/a/h3")
                            
                            except Exception:
                                try:
                                    i+=1
                                    sleep(2)
                                    elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div/div[2]/div[2]/div/div/div[{i}]/div[2]/a/h3")
                                except Exception:
                                    sleep(2)
                                    elem = driver.find_element_by_xpath("/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div[2]/a/div")
                                
                            
                    else:
                        try:   
                            sleep(2)
                            elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div/div[2]/div[2]/div/div/div[{i}]/div[2]/a/h3")
                        
                        except Exception:  
                            try:
                                sleep(2)
                                elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div[{i}]/a/h3")
                            except Exception:
                                try:
                                    sleep(2)
                                    elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div[{i}]/a/div")
                                except Exception:
                                    try:
                                        sleep(2)
                                        elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div[{i}]/a/div")
                                    except Exception:
                                        try:
                                            elem =  driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[{i}]/div[2]/a/h3")
                                        except Exception:
                                            elem =  driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div[{i}]/div[2]/a/h3")
                                    
                                
                            
                            
                    raw_title = elem.text
                   
                    
        
                    try:                                        
                        text_type = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[{i}]/div/div[2]/div[2]/span[3]").text
                    
                    except Exception: 
                        i+=1   
                        text_type = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[{i}]/div/div[2]/div[2]/span[3]").text
                    
                    
                    try:
                        elem.click()
                        
                    except Exception:
                        
                        try:
                            
                            driver.execute_script(f"window.scrollBy(0, {-100})","")
                            elem.click()
                        
                        except Exception:
                            
                            driver.execute_script(f"window.scrollBy(0, {50})","")
                            elem.click()
                            
                        
                    
                    
                    #WebDriverWait(driver, 10).until(EC.visibility_of(elem))
                    
                    #time.sleep(0.5)
                    #driver.execute_script("arguments[0].click();", elem)

                    
                    #elem.click()
                    
                    try:
                        test = driver.find_element_by_css_selector(".XQ7Wld > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)")
                       # test = driver.find_element_by_xpath("//span[text()='Language: ']/following-sibling::span")
                        check_language = test.text.lower()
                        print(f"g: {raw_title}")
                        driver.back()
                        driver.switch_to.default_content()
                        

                    except Exception:
                        
                        driver.back()
                        driver.switch_to.default_content()
                        raw_title = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[{i}]/div[2]/div[3]/span").text




                        if ':' in raw_title or ';' in raw_title or '-' in raw_title or ',' in raw_title:

                            if ':' in raw_title:
                                check_language = detect(raw_title.split(":")[0])

                            elif ';' in raw_title:
                                check_language = detect(raw_title.split(";")[0])

                            elif '-' in raw_title:
                                check_language = detect(raw_title.split('-')[0])

                            else:
                                check_language = detect(raw_title.split(',')[0])

                        else:
                            check_language = detect(raw_title)

                    
                    if check_language=='english':
                        check_language = 'en' 
                        
                    else:
                        with open('languages.txt','r') as file:
                            for line in file:
                                #print(line.split(" ")[1])

                                if (len(line.split(" "))== 3):

                                    if check_language == line.split(" ")[0].strip().lower():
                                        check_language = (line.split(" ")[2].strip())
                                else:
                                    if check_language == line.split(" ")[0].strip().lower():
                                        check_language = (line.split(" ")[1].strip())
                    # make text file with references
                 
                    #driver.back() 

                    #driver.switch_to.default_content()

                    sleep(3)

                    # If the book is not in english, or is a dictionary, the program will skip it, since
                    # users will not be able to make much use of information in those books.
                   
                    print(check_language)
                    if (check_language == language and 'ictionar' not in raw_title.lower() and 'ncyclop' not in raw_title.lower() and 'atalogue' not in raw_title.lower()):
                        
                        author = ""

                        try:    
                            tmpVar = driver.find_element_by_css_selector(f"div.Yr5TG:nth-child({i}) > div:nth-child(2) > div:nth-child(3) > a:nth-child(1) > span:nth-child(1)")                                                
                            author = tmpVar.text
                            
                        except Exception:
                            
                            try:
                                tmpVar = driver.find_element_by_css_selector(f"div.Yr5TG:nth-child({i}) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1)")  
                                author = tmpVar.text

                            except Exception:
                                pass

                        if (author!=""):
                            author = " ".join(author.split(" ")[:2]).lower()

                            if author not in authorList and author.isdigit()==False:
                                isValid = True
                                authorList.append(author)
                        else:
                            same_author = True





                        title = raw_title.lower()

                        if ':' in title or ';' in title or '-' in title or ',' in title:

                            first = ""
                            sec = ""

                            if ':' in title:

                                if (len(title.split(':'))>2):

                                    first = title.split(":")[0]+" "+title.split(":")[1]

                                    if ('page' not in sec):
                                        sec = title.split(":")[2]

                                else:

                                    first = title.split(':')[0]

                                    if ('page' not in sec):
                                        sec = title.split(":")[1]

                                first = re.sub('[^a-zA-Z0-9-_*.] ', ' ', first)
                                sec = re.sub('[^a-zA-Z0-9-_*.] ', ' ', sec)

                                if (any(first in word for word in authorList) == False and any(sec in word for word in authorList) == False):
                                    isValid = True
                                    authorList.append(first)
                                    authorList.append(sec)
                                else:
                                    isValid = False



                            elif ';' in title: 

                                if (len(title.split(';'))>2):

                                    first = title.split(";")[0]+" "+title.split(";")[1]

                                    if ('page' not in sec):
                                        sec = title.split(";")[2]

                                else:

                                    first = title.split(';')[0]


                                    if ('page' not in sec):  
                                        sec = title.split(";")[1]

                                first = re.sub('[^a-zA-Z0-9-_*.] ', ' ', first)
                                sec = re.sub('[^a-zA-Z0-9-_*.] ', ' ', sec)

                                if (any(first in word for word in authorList) == False and any(sec in word for word in authorList) == False):
                                    
                                    isValid = True
                                    authorList.append(first)
                                    authorList.append(sec)
                                    
                                else:
                                    isValid = False



                            elif '-' in title:


                                if (len(title.split('-'))>2):

                                    first = title.split("-")[0]+" "+title.split("-")[1]

                                    if ('page' not in sec):
                                        sec = title.split("-")[2]

                                else:

                                    first = title.split('-')[0]

                                    if ('page' not in sec):
                                        sec = title.split("-")[1]
                                        
                                        
                                

                                first = re.sub('[^a-zA-Z0-9-_*.] ', ' ', first)
                                sec = re.sub('[^a-zA-Z0-9-_*.] ', ' ', sec)


                                if (any(first in word for word in authorList) == False and any(sec in word for word in authorList) == False):
                                    
                                    isValid = True
                                    authorList.append(first)
                                    authorList.append(sec)
                                    
                                else:
                                    isValid = False





                            elif ',' in title:

                                if (len(title.split(','))>2):

                                    first = title.split(",")[0]+" "+title.split(",")[1]

                                    if ('page' not in sec):

                                        sec = title.split(",")[2]

                                else:

                                    first = title.split(',')[0]

                                    if ('page' not in sec):

                                        sec = title.split(",")[1]

                                first = re.sub('[^a-zA-Z0-9-_*.] ', ' ', first)
                                sec = re.sub('[^a-zA-Z0-9-_*.] ', ' ', sec)

                                if (any(first in word for word in authorList) == False and any(sec in word for word in authorList) == False):
                                    
                                    isValid = True
                                    authorList.append(first)
                                    authorList.append(sec)
                                    
                                else:
                                    isValid = False



                        else: 
                            title = re.sub('[^a-zA-Z0-9-_*.] ', ' ', title)

                            if title not in authorList:
                                isValid = True
                                authorList.append(title)
                            else:
                                isValid = False





            # Sometimes, google books isn't formatted in the
            # way that the book is in the form of a pop up.

            # So, to account for this, we see if the website 
            # has more than one frame.

            # If it does, we switch the reference frame to the pop
            # up, else we keep it as is.

                    print(isValid)
                    print(same_author)
                    if (isValid and same_author == False):
                        
                        tmpTitle.append(raw_title)
                        
                        
                        link = driver.find_element_by_css_selector(f"div.Yr5TG:nth-child({i}) > div:nth-child(2) > a:nth-child(1)")
                        tmpHyper.append(link.get_attribute("href"))  
                         
                        left = 25
                        top = 255
                        right = 1175
                        bottom = 737


                        new_width  = (1175-25)*2
                        new_height = (737-255)*2

                        needs_back = False

                        sleep(1)

                        if (i==1):

                            sleep(2)

                            try:
                                sleep(2)
                                elem = driver.find_element_by_xpath("/html/body/div[6]/div/div[10]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/a/h3")

                            except Exception:
                                try:
                                    sleep(2)
                                    elem = driver.find_element_by_xpath("/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div[2]/a/h3")

                                except Exception:
                                    try:

                                        i+=1
                                        sleep(2)
                                        elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div/div[2]/div[2]/div/div/div[{i}]/div[2]/a/h3")
                                    except Exception:
                                         elem = driver.find_element_by_xpath("/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div[2]/a/div")


                        else:
                            try:  
                                sleep(2)
                                elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div/div[2]/div[2]/div/div/div[{i}]/div[2]/a/h3")

                            except Exception:  
                                try:
                                    sleep(2)
                                    elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div[{i}]/a/h3")
                                except Exception:
                                    try:
                                        sleep(2)
                                        elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div[{i}]/a/div")
                                    except Exception:
                                        try:
                                            sleep(2)
                                            elem = driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/div[{i}]/a/div")
                                        except Exception:
                                            try:
                                                elem =  driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[{i}]/div[2]/a/h3")
                                            except Exception:
                                                elem =  driver.find_element_by_xpath(f"/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div[{i}]/div[2]/a/h3")

                        #driver.execute_script("arguments[0].click();", elem)
                        elem.click()
                        sleep(2)

                        try:
                            driver.switch_to.frame("s7Z8Jb")

                        except WebDriverException:
                            pass

                        sleep(1)


            # Next, we check if the website contains the "View all"
            # button that helps us find the specific parts of the text
            # that contain the word that we are seeking to understand.

            # If it doesn't contain it, it will simply take a screenshot,
            # then exit.

                        try:
                            # Try why doesn't this work.
                            driver.find_element_by_css_selector('span.search-bar-link:nth-child(6)').click()
                            driver.find_element_by_css_selector('span.search-bar-link:nth-child(6)').clear()
                            driver.find_element_by_css_selector('span.search-bar-link:nth-child(6)').send_keys(chosen_word)
                            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/form/table/tbody/tr/td[3]/input').click()

                        except Exception:
                            pass
                            if (text_type == 'Magazine'):

                                driver.find_element_by_css_selector("#\:5 > img:nth-child(1)").click()
                                top = 315
                                needs_back = True

                            if (text_type == 'Newspaper'):
                                driver.find_element_by_css_selector("#\:4 > img:nth-child(1)").click()
                                top = 315
                                needs_back = True



                            curr_height=0

                            bottom = 730

                            if (text_type!='Newspaper'):
                                driver.execute_script("document.body.style.transform='scale(1.85)';")
                            try:
                                sleep(2)
                                elem = driver.find_element_by_class_name("scroll-background")

                                total_height = float(elem.get_attribute("style").split("height: ")[1].split("px")[0])

                                sleep(2)

                                # While we have not reached the end of the page,
                                # we will screenshot all of the relevant sections
                                # of the book that contain the word.

                                # This loop will continue to scroll down until we have 
                                # reached the end of the page.

                                # I've noticed that sometimes, a book can have too many pages. This 
                                # might skew our representation of how the text network analysis looks.

                                # So, I am going to put a counter, and only allow
                                # a maximum of 8 screenshots per book, and 20 if there are keywords.
                                
                                print(f"Height: {total_height}")
                                    
                                if (total_height > 1000):
                                    driver.execute_script(f"arguments[0].scrollBy(0, {int(total_height/2)})",driver.find_element_by_class_name("overflow-scrolling"))

                                
                                
                                
                                screenshot_count=0

                                not_first = False

                                sleep(1)

                                while curr_height <= total_height and screenshot_count < screenshot_max:

                                # Give the program some time to load the book.

                                    sleep(2)

                                    driver.save_screenshot(f"{num_image}.png")                        
                                    img = change_contrast(Image.open(f"{num_image}.png"),40)
                                    area = (left, top, right, bottom)
                                    img = img.crop(area)
                                    img = img.resize((new_width,new_height), Image.ANTIALIAS)
                                    img.save(f"{num_image}.png")
                                    driver.execute_script("arguments[0].scrollBy(0, 225)",driver.find_element_by_class_name("overflow-scrolling"))
                                    curr_height += driver.execute_script("return document.documentElement.scrollHeight")
                                    screenshot_count+=1
                                    num_image+=1

                                sleep(1)

                            except Exception:
                                pass


                        except Exception:


                            try:

                                driver.find_element_by_xpath('//*[@id="search_form_input"]').clear()

                                top = 260

                            except Exception:
                                pass
                            if (text_type == 'Magazine'):

                                driver.find_element_by_css_selector("#\:5 > img:nth-child(1)").click()
                                top = 315
                                needs_back = True

                            if (text_type == 'Newspaper'):

                                driver.find_element_by_css_selector("#\:4 > img:nth-child(1)").click()
                                top = 315
                                needs_back = True

                            curr_height=0

                            if (text_type!='Newspaper' and document.body!=null):

                                driver.execute_script("document.body.style.transform='scale(2.15)';")

                            sleep(2)

                            try:
                                elem = driver.find_element_by_class_name("scroll-background")
                                total_height = float(elem.get_attribute("style").split("height: ")[1].split("px")[0])

                                sleep(2)

                        # While we have not reached the end of the page,
                        # we will screenshot all of the relevant sections
                        # of the book that contain the word.

                        # This loop will continue to scroll down until we have 
                        # reached the end of the page.

                        # I've noticed that sometimes, a book can have too many pages. This 
                        # might skew our representation of how the text network analysis looks.

                        # So, I am going to put a counter, and only allow
                        # a maximum of 20 screenshots per book

                                screenshot_count=0

                                not_first = False

                                while curr_height <= total_height and screenshot_count < 4:

                                # Give the program some time to load the book.

                                    sleep(1)
                                    driver.save_screenshot(f"{num_image}.png")                        
                                    img = change_contrast(Image.open(f"{num_image}.png"),40)
                                    area = (left, top, right, bottom)
                                    img = img.crop(area)
                                    img = img.resize((new_width,new_height), Image.ANTIALIAS)
                                    img.save(f"{num_image}.png")
                                    driver.execute_script("arguments[0].scrollBy(0, 220)",driver.find_element_by_class_name("overflow-scrolling"))
                                    curr_height += driver.execute_script("return document.documentElement.scrollHeight")
                                    screenshot_count+=1
                                    num_image+=1




        #______________________________________________________________________    

                                sleep(1)
                            except Exception:
                                pass



                    break_point.append(num_image)                        

                    sleep(2)                       

                    driver.execute_script("window.history.go(-1)")



                    if (needs_back == True):

                        driver.execute_script("window.history.go(-1)")


                    driver.switch_to.default_content()

                    sleep(1)


                    if (i>1):
                        
                        driver.execute_script(f"window.scrollBy(0, {initial_scroll_height})","")
                        initial_scroll_height -=21
                        sleep(3)

               
               
                    
                    page += 1

                    if (page>=13):

                        page = 13

                    driver.switch_to.default_content()

                    driver.forward()

                    driver.back()

                    driver.refresh()

                    driver.switch_to.default_content()

                    sleep(2)

                    try:   
                        select=f".AaVjTc > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child({page}) > a:nth-child(1)"

                        driver.find_element_by_css_selector(select).click()

                    except Exception:

                        end_of_page = True




                    hyperlink_list.append(tmpHyper)

                    title_list.append(tmpTitle)


            
            if (len(hyperlink_list) == 0):

                print("There were no results fitting the requirements, please edit the variables in your entry.")
                driver.quit()

            else:
                
                if (len(tmpHyper) != total_books):
                    
                    print(f"We only found {len(tmpHyper)} books although you resquested that we go through {total_books}. ")
                    print("If you want to increase the number of books, please quit the window. Otherwise, the program will continue.")
                    sleep(1)
                    
                    
                books_entered.append(len(tmpTitle))
                
                
                # Check here if num_images > 30, split it into num_images/30 files. 
                

                if (num_image > 12):

                    alphabet_string = string.ascii_lowercase
                    alphabet_list = list(alphabet_string)

                    # Max for each is 40 so we have to split it as many times as we can.
                    # ** Get the breakpoint of the number that is the closest to the
                    # one that we are looking for.

                    split_file = int(num_image/20)-1

                    tmp_t =[]
                    previous = -1
                    curr = 1



                    # Sets the breakpoints that the pdfs will enter by.

                    while (previous!=len(break_point)-1):

                        calculate_closest = 20 * curr

                        n = min(break_point, key=lambda x:abs(x-calculate_closest))

                        idx = break_point.index(n)


                        if (previous == idx):

                            idx = len(break_point)-1
                            tmp_t.append(break_point[idx])
                            break


                        if (break_point[idx] - break_point[previous] > 20):

                            while (break_point[idx] - break_point[previous] > 20):
                                idx = idx-1

                        curr +=1

                        previous = idx

                        tmp_t.append(break_point[idx])

                    # Initialize the start and go through and append each picture
                    # to the respective pdf file.

                    curr = 0
                    count = 0



                    while (count<split_file):    

                        imagelist = []

                        while (curr<tmp_t[count]):

                            if (curr in break_point and curr!=num_image-1):

                                tmp1=Image.open('breakpage.png')
                                con1=tmp1.convert('RGB')
                                tmp=Image.open(f'{curr}.png')
                                con=tmp.convert('RGB')
                                imagelist.append(con1)
                                imagelist.append(con)

                            elif (curr==tmp_t[count]-1):

                                tmp1=Image.open('breakpage.png')
                                con1=tmp1.convert('RGB')
                                tmp=Image.open(f'{curr}.png')
                                con=tmp.convert('RGB')
                                imagelist.append(con)
                                imagelist.append(con1)

                            else:

                                tmp=Image.open(f'{curr}.png')
                                con=tmp.convert('RGB')
                                imagelist.append(con)

                            curr +=1


                        merge_images_vertically(imagelist)

                        image = Image.open('mergedBooks.png')


                        pdf_bytes = img2pdf.convert(image.filename)


                        file = open(f'mergedImages{str(decade_count)+alphabet_list[count]}.pdf', "wb")

                        count+=1

                        file.write(pdf_bytes)


                        image.close()

                        file.close()

                else:

                    imagelist = []

                    for i in range(num_image):

                        if (i in break_point and i!=num_image-1):

                            tmp1=Image.open('breakpage.png')
                            con1=tmp1.convert('RGB')
                            tmp=Image.open(f'{i}.png')
                            con=tmp.convert('RGB')
                            imagelist.append(con1)
                            imagelist.append(con)

                        elif (i==num_image-1):

                            tmp1=Image.open('breakpage.png')
                            con1=tmp1.convert('RGB')
                            tmp=Image.open(f'{i}.png')
                            con=tmp.convert('RGB')
                            imagelist.append(con)
                            imagelist.append(con1)

                        else:

                            tmp=Image.open(f'{i}.png')
                            con=tmp.convert('RGB')
                            imagelist.append(con)

                    print(imagelist)
                    print(len(imagelist))
                    merge_images_vertically(imagelist)

                    image = Image.open('mergedBooks.png')


                    pdf_bytes = img2pdf.convert(image.filename)


                    file = open(f'mergedImages{decade_count}.pdf', "wb")


                    file.write(pdf_bytes)

                    image.close()


                    file.close()

                    
                prev = curr_year

                tmp=[str(i) for i in str(curr_year)]

                pre_start  = "".join(tmp[:2])

                pre_start = int(pre_start)

                suf_start  = "".join(tmp[2:])

                suf_start = int(suf_start)

                if (suf_start == 0):
                    pre_start +=1
                    curr_year = pre_start*100

                else:    
                    curr_year=pre_start*100+(suf_start+interval)
                    
                decade_count +=1
                tmp = 1
                
                driver.switch_to.default_content()
                
               
              
                
                if (page==1):
                    
                    while (page>0):
                        
                        driver.back()
                        driver.refresh()
                        page -= 1
                        sleep(1)
                        
                else:
                    tmp=2
                    while (tmp < page):
                        
                        driver.back()
                        driver.refresh()
                        tmp+=1
                        sleep(1)


              

    except Exception as e:
        
        error_found= True
        print(traceback.format_exc())
        
        if ('RuntimeError' in e.__class__.__name__):
            print(f"Only {total_books} books were found, the program will continue but please close if you wish to produce a graph for this interval.")
            error_found = False
            #goto(905)
            
            
        
        elif ('NoSuchWindowException' not in e.__class__.__name__ and 'NameError' not in e.__class__.__name__):
            
            driver.close()
            chosen_word = chosen_word.split(" ")[0]
            print("There was a network error, the program will restart.")
            compute(chosen_word,interval,start_date,end_date,total_books,keywords,analysis_type,language)
        
        elif ('NoSuchWindowException' in e.__class__.__name__):
            
            print("Browser has been closed, will quit the program.")
            driver.quit()
            
        
            
            
           
        
    # If the program quits the function because of an exception, it will not go to the next functions and 
    # will terminate.
    
    if (error_found == False):
        
        chosen_word = GoogleTranslator(source=language, target='en').translate(text=chosen_word.split(" ")[0])  
        keywords = GoogleTranslator(source=language, target='en').translate(text=keywords)  
        driver.quit()
        #save_it(decade_list,hyperlink_list,chosen_word,interval,start,end_year,total_books,title_list,books_entered,keywords,language,is_en)

app = Flask(__name__)
cors = CORS(app , resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})

input_values = dict()
check = False

# def index():

#     return render_template("index.html",check=check,dictionary=input_values)

# @app.route("/",methods=['GET','POST'])

# # depending on whether the button is update or submit, 
# # I change what I do.
# def index_post():

#     check = True
#     if request.method=='POST':
#         #result = request.form
#         #print(result)
#         try:
#             keywords = request.form["keyword"]
#             if keywords!='':
#                 input_values['keyword'] = keywords
              
#         except Exception:
#             pass

#         try:
#             interval = request.form["interval"]
#             if interval!='':
#                 input_values['interval'] = interval
                
           
#         except Exception:
#             pass

#         try:
#             startDate = request.form["startDate"]
#             if startDate!='':
#                 input_values['startDate'] = startDate
              
           
#         except Exception:
#             pass
        
#         try:
#             endDate = request.form["endDate"]
#             if endDate!='':
#                 input_values['endDate'] = endDate
              
           
#         except Exception:
#             pass
        
#         try:
#             numBooks = request.form["numBooks"]
#             if numBooks!='':
#                 input_values['numBooks'] = numBooks
              
           
#         except Exception:
#             pass
        



#         # Initialize a new dictionary that only stores the values
#         # that have been initialized.
        
#         return render_template("index.html",check=check,dictionary=input_values)
        
 

@app.route("/result",methods=['POST']) 


def input():

    def start_program(inputs):
        compute(inputs['keyword'],inputs['interval'],inputs['startDate'],inputs['endDate'],inputs['numBooks'],inputs['extraWords'],inputs['analysisType'],inputs['language'])
        return

    if request.method == 'POST': 
        inputs = json.loads(list((request.form).keys())[0])
        
        print(inputs)

        if (inputs['keyword']=='' or inputs['interval']=='' or inputs['startDate']=='' or inputs['endDate']=='' or inputs['numBooks']==''):

            data = {"response":"please enter all the correct values."} # Your data in JSON-serializable type        
            return jsonify(data)
        else:

           
            data = {"response":"Redirecting to the loading page..."} # Your data in JSON-serializable type

            thread = Thread(target=start_program(inputs)).start()
        
            return jsonify(data)
            
       


if __name__=="__main__":
    app.run(debug=True)