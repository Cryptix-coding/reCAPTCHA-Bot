# reCAPTCHA Bot
This bot can solve the Google Recaptcha for you completely automated.

#How the bot works
1. opening of the page with the reChaptcha (Demo) (https://www.google.com/recaptcha/api2/demo)
2. search frame with the reCpatcha
3. wait
4. activate checkbox
5. wait
6. select audio challenge (easier than images challenge; see 10.)
7. wait
8. listen to audio challenge
9. find the link with audio challenge and download audio file
10. convert the audio file into text with the Google-Voice-Recognition
11. enter text in the field and confirm

#needed libraries
selenium + appropriate browser driver
- Chrome: https://chromedriver.chromium.org/downloads
- Firefox: https://github.com/mozilla/geckodriver/releases

FFmpeg (https://lame.buanzo.org/#lamewindl)   
pydub   
webdriver-manager   
SpeechRecognition
