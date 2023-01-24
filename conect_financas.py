from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import time
import openpyxl
import pickle



def machine():
    idx = 0
    cod_list = []
    with open('variaveis.pickle', 'rb') as file:
        nif = pickle.load(file)
        pasw = pickle.load(file)

        nif_d = pickle.load(file)
        #nome_d = pickle.load(file)
        cede_d = pickle.load(file)
        cp_d = pickle.load(file)
        local_d = pickle.load(file)

        morad_lc = pickle.load(file)
        cp_lc = pickle.load(file)
        local_lc = pickle.load(file)
        data_lc = pickle.load(file)

        morad_ld = pickle.load(file)
        cp_ld = pickle.load(file)
        local_ld = pickle.load(file)

        desig_b = pickle.load(file)
        qtd_b = pickle.load(file)
        und_d = pickle.load(file)

        h_list = pickle.load(file)
        d_dir = pickle.load(file)
        xl_dir = pickle.load(file)
        s_name = pickle.load(file)
        n_guias = pickle.load(file)
        row = pickle.load(file)
        coll = pickle.load(file)

    d_dir = str(d_dir).replace('/', r"\"").replace('"','')
    h_list = str(h_list).rstrip().split(',')

    options = ChromeOptions()
    chrome_prefs = {
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True,
        "download.open_pdf_in_system_reader": False,
        "profile.default_content_setting.popups": 0,
        "download.default_directory": d_dir,
        "download.directory_upgrade": True
    }
    options.add_experimental_option("prefs", chrome_prefs)
    options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.acesso.gov.pt/jsp/loginRedirectForm.jsp?path=DocTransporte%2FpainelRemetente.action&partID=SGDT')


    box_nif = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/label[2]')
    box_nif.click()

    boxnif = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/div[2]/div/form/div[1]/div/div/input')
    boxnif.send_keys(nif)

    boxpass = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/div[2]/div/form/div[2]/div/div/input')
    boxpass.send_keys(pasw)

    go = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/div[2]/div/form/button')
    go.click()

    btn1 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[5]/div[3]/ul/li[1]/div/div/p[2]/a')
    btn1.click()

    tab1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[1]/div/div/select/option[2]')
    tab1.click()

    time.sleep(2)

    point1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[2]/div/div/div/select/option[3]')
    point1.click()

    d1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[9]/div[1]/div/div/input')
    d1.send_keys(nif_d)

    #d2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[8]/div[2]/div/div/input')
    #d2.send_keys(nome_d)

    d3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[10]/div[1]/div/div/textarea')
    d3.send_keys(cede_d)

    d4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[10]/div[2]/div/div/input')
    d4.send_keys(cp_d)

    d5 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[11]/div/div/div/input')
    d5.send_keys(local_d)


    lc1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[13]/div[1]/div/div/textarea')
    lc1.send_keys(morad_lc)

    lc2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[13]/div[2]/div/div/input')
    lc2.send_keys(cp_lc)

    lc3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[14]/div/div/div/input')
    lc3.send_keys(local_lc)

    lc4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[15]/div[1]/div/div/div/input')
    lc4.send_keys(data_lc)

    lc_hora = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[15]/div[2]/div/div/input')
    lc_hora.send_keys(h_list[idx])
    idx += 1

    #print(idx)
    #print(h_list[1])

    ld1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[17]/div[1]/div/div/textarea')
    ld1.send_keys(morad_ld)

    ld2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[17]/div[2]/div/div/input')
    ld2.send_keys(cp_ld)

    ld3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[18]/div/div/div/input')
    ld3.send_keys(local_ld)


    ben1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[22]/div/div/table/tbody/tr/td[1]/div/div/input')
    ben1.send_keys(desig_b)

    ben2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[22]/div/div/table/tbody/tr/td[2]/div/div/input')
    ben2.send_keys(qtd_b)

    ben3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[22]/div/div/table/tbody/tr/td[3]/div/div/input')
    ben3.send_keys(und_d)

    submit = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[24]/div/div/button')
    submit.click()

    time.sleep(3)
    
    #################Numero pa  lista do excell
    num = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[7]/div[1]/div[2]/div[2]/span')
    xlnum = num.text

    cod_list.append(xlnum)

    ########################Download

    ver_doc = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[7]/div[16]/div/div/a[1]')
    link = ver_doc.get_attribute('href')
    
    driver.get(link)
    
    #############################

    ctrl = 0
    while ctrl < int(n_guias)-1:
        driver.back()
        time.sleep(3)
        re_tab1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[1]/div/div/select/option[3]')
        re_tab1.click()
        time.sleep(2)
        rere_tab1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[1]/div/div/select/option[2]')
        rere_tab1.click()
        time.sleep(2)

        point1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[2]/div/div/div/select/option[3]')
        point1.click()

        lc_hora = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[15]/div[2]/div/div/input')
        lc_hora.clear()
        lc_hora.send_keys(h_list[idx])
        idx += 1

        submit = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/form/div[24]/div/div/button')
        submit.click()
        time.sleep(3)
        num = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[7]/div[1]/div[2]/div[2]/span')
        xlnum = num.text
        cod_list.append(xlnum)


        ver_doc = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[7]/div[16]/div/div/a[1]')
        link = ver_doc.get_attribute('href')
        driver.get(link)

        ctrl += 1


    bok = openpyxl.load_workbook(xl_dir)
    sht = bok[s_name]

    for x in range(len(cod_list)):
        cel = coll + str(row)
        sht[cel] = cod_list[x]
        row = int(row) + 1

    bok.save(xl_dir)
