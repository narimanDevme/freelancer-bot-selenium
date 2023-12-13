import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from chatgpt import GPT
from APIhandler import APIhandler






class dev_controler():
    count_halth = 0 
    def see_discrib(url , test_link_chanse):
        response = requests.get(url)
        if response.status_code == 200 :
            soup = BeautifulSoup(response.text, 'html.parser')
#------------------------------------------------------------------------------------------------------------------>
#  objackts :

            try:
                projeckt_name  = soup.select_one("#main > div > div > div > div.Grid-col.Grid-col--desktopSmall-8 > section:nth-child(1) > div > div.Card-body.PageProjectViewLogout-projectDetails-card > div.Grid.PageProjectViewLogout-projectInfo-Grid > div.Grid-col.Grid-col--tablet-8 > h1")
                projeckt_name = projeckt_name.text
                projeckt_body = soup.select_one("#main > div > div > div > div.Grid-col.Grid-col--desktopSmall-8 > section:nth-child(1) > div > div.Card-body.PageProjectViewLogout-projectDetails-card > div.PageProjectViewLogout-detail")
                projeckt_body = projeckt_body.text
                projeckt_many = soup.select_one("#main > div > div > div > div.Grid-col.Grid-col--desktopSmall-8 > section:nth-child(1) > div > div.Card-body.PageProjectViewLogout-projectDetails-card > div.Grid.PageProjectViewLogout-projectInfo-Grid > div.Grid-col.Grid-col--tablet-4 > p.PageProjectViewLogout-projectInfo-byLine")
                projeckt_many = projeckt_many.text
                projeckt_location = soup.select_one("#main > div > div > div > div.Grid-col.Grid-col--desktopSmall-4.PageProjectViewLogout-sideContent-container > aside > div.PageProjectViewLogout-detail-reputation.PageProjectViewLogout-detail-tags > div > div:nth-child(2) > span > span.PageProjectViewLogout-detail-reputation-item-locationItem.PageProjectViewLogout-detail-reputation-item-text")
                if projeckt_location:
                    projeckt_location = projeckt_location.text
                else:
                    None
                projeckt_ablity = soup.select_one("#main > div > div > div > div.Grid-col.Grid-col--desktopSmall-8 > section:nth-child(1) > div > div.Card-body.PageProjectViewLogout-projectDetails-card > div.PageProjectViewLogout-detail > p.PageProjectViewLogout-detail-tags").text
                projeckt_avereg_many = soup.select_one("h2.Card-heading")
                ss2 = "average"
                ss = "Project ID"
                ss3 = "for"
                if projeckt_avereg_many == None:
                    projeckt_avereg_many = soup.select_one("h2.Card-heading")
                    if projeckt_avereg_many:
                        projeckt_avereg_many = projeckt_avereg_many.text
                    else:
                        None
                else:
                    projeckt_avereg_many = projeckt_avereg_many.text
                    projeckt_avereg_many = projeckt_avereg_many[projeckt_avereg_many.find(ss2)+7:projeckt_avereg_many.find(ss3)]
                
    #---------------------------------------------------------->>

            except:
                if dev_controler.count_halth > 5 :
                    dev_controler.count_halth = 0
                    return 10
                else:
                    dev_controler.count_halth += 1
                    result = dev_controler.see_discrib(url , 0)
                    return result
                

#------------------------------------------------------------------------------------------------------------------>
#
#
#
#
#
#
#
#
#------------------------------------------------------------------------------------------------------------------>>
# main :
            if projeckt_name or projeckt_body or projeckt_many or projeckt_location or projeckt_ablity :
                #all variable you need :
                #projeckt_name
                #projeckt_body[:projeckt_body.find(ss)]
                #projeckt_many
                #projeckt_avereg_many
                #projeckt_location.strip()
                #ave_org
                #GPT_ansewr
                #>>>>>>>>>>>>>>>>>>>>>>>>>

                #name 
                print(f"name >> {projeckt_name}")
                #Body
                print(f"Body >> \n{projeckt_body[:projeckt_body.find(ss)]}")
                #many
                print("=======>>")
                print(f"many >> {projeckt_many}")
                if "hour" in projeckt_many:
                    many_mark = projeckt_many[::-1]
                    many_mark = many_mark[:10]
                    h = many_mark.find("\\")
                    many_mark = many_mark[h-2:12]
                    many_mark = many_mark[::-1]
                    ave_org = APIhandler.gnaration_price(projeckt_avereg_many , projeckt_many)
                    price_status = APIhandler.check_mony(many_mark , ave_org)
                    print(f"many mark >> {many_mark}")
                    price_status = True
                else:
                    many_mark = projeckt_many[::-1]
                    many_mark = many_mark[:3]
                    many_mark = many_mark[::-1]
                    ave_org = APIhandler.gnaration_price(projeckt_avereg_many , projeckt_many)
                    price_status = APIhandler.check_mony(many_mark , ave_org)
                    print(f"many mark >> {many_mark}")
                #location
                try:
                    print(f"location >> {projeckt_location.strip()}")
                except:
                    None
                print(f"average many >> {projeckt_avereg_many}")
                print(f"Proposed price >> {ave_org}")
                
                print("gpt proposal >> >>\n")
                gpt_input = f"{projeckt_body[:projeckt_body.find(ss)]} . {GPT.default_promt}"
                GPT_ansewr = GPT.input(gpt_input)
                print(GPT_ansewr)
                print("\n>> >> >> >> >> >> >> >> >> >> \n")
                print(f"price check is {price_status}")
                tag_check = APIhandler.tag_check(projeckt_ablity)
                print(f"tag check is {tag_check}")




                return 200
#------------------------------------------------------------------------------------------------------------------>>
            else:
                if test_link_chanse < 4:
                    test_link_chanse = test_link_chanse +  1
                    result = dev_controler.see_discrib(url , test_link_chanse)
                    return result
                else:
                    print("link exit !")
                    return 888
        else:
            print(">>>>>>>>>>>>> try >>>>>>>>>>>>>")
            print(f"status error is {response.status_code}")
            print("connectionless !!!")
            if test_link_chanse < 4:
                    test_link_chanse = test_link_chanse +  1
                    result = dev_controler.see_discrib(url , test_link_chanse)
                    return result
            else:
                    print("link exit !")
                    return 404


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>














