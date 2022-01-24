# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:54:45 2022

@author: frost
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time as time
import numpy as np


def scraper_method(email, password, job_name, job_city):
    
    driver = webdriver.Chrome(executable_path= "C:/Users/frost/Documents/glassdoor_scraper/chromedriver.exe") 
    driver.maximize_window()
    
    driver.get("https://www.glassdoor.com/index.htm")
    
    driver.find_element(By.XPATH,"//button[@class='d-none d-lg-block p-0 LockedHomeHeaderStyles__signInButton']").click()
    
    driver.find_element(By.ID, "userEmail").send_keys(email)
    
    driver.find_element(By.ID, "userPassword").send_keys(password + Keys.ENTER)
    
    time.sleep(2)
    
    search_field = driver.find_element(By.XPATH, "//input[@aria-label='Search Keyword']")
    search_field.send_keys(job_name)
    
    location_field = driver.find_element(By.XPATH, "//input[@aria-label='Search Location']")
    
    location_field.click()
    
    driver.find_element(By.XPATH, "//div[@aria-label='Clear']").click()
    
    location_field.send_keys(job_city + Keys.ENTER)
    
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//div[@class='mt-std d-flex justify-content-center']/a").click()
    
    time.sleep(2)
    
    #Get Jobs From Pages
    job_page = job_df_creator(driver)
    
    #Return Df
    df = pd.DataFrame(job_page)  
    driver.close() 
    return df 

     
def job_df_creator(driver):    
    
    works = driver.find_elements(By.XPATH,"//ul[@class='hover p-0  job-search-key-kgm6qi exy0tjh1']/li")
    
    time.sleep(5)
    
    job_list = []
    
    for work in works:
        #Get Titles From Jobs
        try:
            job_title = work.find_elements(By.XPATH,".//div[@class='d-flex flex-column job-search-key-1pzmdmc e1rrn5ka1']/a")[0].get_attribute("title")
            #print(job_title)
        except:
            #print("This job has no title.")
            job_title = np.nan
            
        #Get Position From Jobs
        
        try:
            job_position = work.find_elements(By.XPATH,".//a[@class='jobLink job-search-key-1rd3saf eigr9kq1']/.//span")[0].text
            #print(job_position)
        except:
            #print("This job has no position.")
            job_position = np.nan
            
        #Get Rating From Jobs   
        try:
            job_rating = work.find_elements(By.XPATH,".//div[@class='d-flex flex-column job-search-key-1pzmdmc e1rrn5ka1']/.//span[@class=' job-search-key-srfzj0 e1cjmv6j0']")[0].text
            #print(rating_test)
        except:
            #print("This job has no rating.")
            job_rating = np.nan
            
        #Get Location From Jobs
        try:
            job_location = work.get_attribute("data-job-loc")
            #print(job_location)
        except:
            #print("This job has no location.")
            job_location = np.nan
    
        #Get Job Salary From Jobs
        try:
            job_salary_est = work.find_elements(By.XPATH,".//span[@data-test='detailSalary']")[0].text
            #print(job_salary_est + "\n")
        except:
            #print("This job has no salary estimate.")
            job_salary_est = np.nan
            
        #Get Job Post Date From Jobs
        try:
            job_post_date = work.find_elements(By.XPATH,".//div[@data-test='job-age']")[0].text
            #print(job_post_date)
        except:
            #print("This job has no post date.")
            job_post_date = np.nan
            
        job_item = {
            "job_title": job_title,
            "job_position": job_position,
            "job_rating": job_rating,
            "job_location": job_location,
            "job_salary_est": job_salary_est,
            "job_post_date": job_post_date
            }
        
        job_list.append(job_item)
     
    return job_list  
        
    
     

       
    
        