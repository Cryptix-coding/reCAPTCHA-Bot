import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pydub
import urllib
import speech_recognition


data_path = "C:\\Users\\User\\reCAPTCHA Bot" #insert here your path to the Python file
browser = webdriver.Firefox("C:\\Users\\User\\geckodriver-v0.29.0-win64") #if you use Firefox + enter the path were you have installed the webdriver-file linked in the README.md
#browser = webdriver.Chrome("chromedriver.exe) #if you use Chrome
browser.get("https://www.google.com/recaptcha/api2/demo") #opening of the reCaptcha test page from Google

#searching of the checkbox frame on a webpage
frames = browser.find_elements_by_tag_name("iframe")
browser.switch_to.frame(frames[0])
time.sleep(random.randint(2,4))
browser.find_element_by_class_name("recaptcha-checkbox-border").click()

#searching of the audio-button
browser.switch_to.default_content()
frames = browser.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
browser.switch_to.frame(frames[0])
time.sleep(random.randint(2,4))
browser.find_element_by_id("recaptcha-audio-button").click()

browser.switch_to.default_content()
frames = browser.find_elements_by_tag_name("iframe")
browser.switch_to.frame(frames[-1])
time.sleep(random.randint(2,4))
browser.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()

#downloading and saving of the audio-file
src = browser.find_element_by_id("audio-source").get_attribute("src")
urllib.request.urlretrieve(src, data_path + "\\audio.mp3")
sound = pydub.AudioSegment.from_mp3(data_path + "\\audio.mp3").export(data_path + "\\audio.wav", format = "wav")

#using of Googles speechrecognition to translate the audiofile into text
recognizer = speech_recognition.Recognizer()
google_audio = speech_recognition.AudioFile(data_path + "\\audio.wav")
with google_audio as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio, language="en-EN") #insert the Language of your Country, otherwhise, the translated text and the audiofile won't match

#writing the text into the reCaptcha field
print("<Erkannter Text>: {}".format(text))
inputfield = browser.find_element_by_id("audio-response")
inputfield.send_keys(text.lower())
inputfield.send_keys(Keys.ENTER)
