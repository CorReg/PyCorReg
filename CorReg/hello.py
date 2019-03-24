import pyttsx3;

def HelloCorReg():
    engine = pyttsx3.init();
    engine.setProperty('rate', 100)     # setting up new voice rate
    engine.say("Hi guys, my name is PAMPA. do you know the Power of Correg ?");
    engine.say("Correg... The Method, The Concept, The Power");
    
    engine.runAndWait() 

