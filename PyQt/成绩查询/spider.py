import urllib.request
from time import sleep
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By



def creat_request():
    url = 'https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fwebvpn.neu.edu.cn%2Flogin%3Fcas_login%3Dtrue'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
    }
    requests_ = urllib.request.Request(url=url, headers=headers)
    return requests_


def get_content(requests):
    response = urllib.request.urlopen(requests)
    content = response.read().decode('utf-8')
    return content


def login_in(idnum_in, pswd_in):
    '''登录'''
    url = 'https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fwebvpn.neu.edu.cn%2Flogin%3Fcas_login%3Dtrue'
    path = r"msedgedriver.exe"
    edgeoptiions = Options()
    edgeoptiions.add_argument('--headless')
    edgeoptiions.add_argument('--disable-gpu')
    browser = webdriver.Edge(service=Service(path), options=edgeoptiions)
    browser.get(url)
    browser.maximize_window()
    idnum = browser.find_element(By.ID, "un")
    idnum.send_keys(str(idnum_in))

    pswd = browser.find_element(By.ID, 'pd')
    pswd.send_keys(str(pswd_in))

    click_btn = browser.find_element(By.ID, 'index_login_btn')
    click_btn.click()
    sleep(1.5)

    js_bottom = 'document.documentElement.scrollTop=700'
    browser.execute_script(js_bottom)
    sleep(1)
    click_btn_2 = browser.find_element(
        By.XPATH, '//*[@id="group-3"]/div[4]/div/div[2]/p[1]')
    click_btn_2.click()
    sleep(1)

    '''新窗口'''

    main_window = browser.current_window_handle
    to_handle = browser.window_handles
    for handle in to_handle:
        if handle == main_window:
            continue
        else:
            browser.switch_to.window(handle)
            idnum_2 = browser.find_element(
                By.XPATH, '/html/body/div[2]/div/form/div/div[1]/input[1]')
            idnum_2.send_keys(str(idnum_in))
            pswd_2 = browser.find_element(
                By.XPATH, '/html/body/div[2]/div/form/div/div[1]/input[2]')
            pswd_2.send_keys(str(pswd_in))
            click_btn_2 = browser.find_element(
                By.XPATH, '//*[@id="index_login_btn"]')
            click_btn_2.click()
            sleep(1)
    js_bottom = 'document.documentElement.scrollTop=100'
    browser.execute_script(js_bottom)
    grades_click = browser.find_element(By.XPATH, '//*[@id="menu_panel"]/ul/li[1]/ul/div/li[20]/a')
    grades_click.click()
    sleep(1)
    grades_get = browser.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td[3]/div/div/div[3]/div[1]')
    return grades_get.text

 


if __name__ == "__main__":
    requests = creat_request()
    content = get_content(requests=requests)
    login_in('20205442', 'leslieleung6')
