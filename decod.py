import re
def decoder (pas,metin ) :
    texts = str("")
    k_sayt = {1:"a",2:"b",3:"c",4:"ç",5:"d",6:"e",7:"f",8:"g",9:"ğ",10:"h",11:"ı",12:"i",13:"j",14:"k",15:"l",16:"m",17:"n",18:"o",19:"ö",20:"p",21:"r",22:"s",23:"ş",24:"t",25:"u",26:"ü",27:"v",28:"y",29:"z"
    ,0:"_", 30 : "'", 31 : '"'}
    k_say = {"a":1,"b":2,"c":3,"ç":4,"d":5,"e":6,"f":7,"g":8,"ğ":9,"h":10,"ı":11,"i":12,"j":13,"k":14,"l":15,"m":16,"n":17,"o":18,"ö":19,"p":20,"r":21,"s":22,"ş":23,"t":24,"u":25,"ü":26,"v":27,"y":28,"z":29
    ," ":0, '"' : 30 ,"'":31}
    
    txtcpassl = []
    txtccon=[]
    txtccont =""
    s = int(0)

    password = str(pas)
    txt = str(metin)
    
    
   
    
    txtccont =  re.findall("<(.*?)>",str(txt))
    for i in txtccont:
        txtcpassl.append(i)
    t = int(0)
    tl = len(password)

    for i in txtcpassl :
        
        i = int(i)

    

    
    
    
        
        
        if s % 3 == 0:
            
            password_p = password[t]
            
            password_d = int(k_say[password_p])

            
            
            
            
            txtccon.append(int(i / password_d))
            #txtcpass = txtcpass / password_d
            #print(txtcpass)
            
            
            
            



        elif s %  2 == 0:
            password_p = password[t]
            
            
            password_d = int(k_say[password_p])
            
            
            
            txtccon.append(int(i / password_d))
        else :
            password_p = password[t]
            
            
            password_d = int(k_say[password_p])
            
            
            
            txtccon.append(int(i / password_d))
        if t == tl-1 :
            t = 1
        else :
            t = t+1 
        s = s+1


    for i in txtccon :
        c = k_sayt[i]
        texts = texts + c
    return texts



def encods(pas , txt        , d ="string"):
    k_say = {"a":1,"b":2,"c":3,"ç":4,"d":5,"e":6,"f":7,"g":8,"ğ":9,"h":10,"ı":11,"i":12,"j":13,"k":14,"l":15,"m":16,"n":17,"o":18,"ö":19,"p":20,"r":21,"s":22,"ş":23,"t":24,"u":25,"ü":26,"v":27,"y":28,"z":29
    ," ":0, '"' :30,"'":31}
    
    txtcpassl = []

    s = int(0)
    c = ""

    password = str(pas)
    text = str(txt)
    
    d = d
    t = int(0)
    tl = len(password)
   
    

    for i in text:
        
        if s % 3 == 0:
            
            password_p = password[t]
            
            password_d = int(k_say[password_p])
            text_d = k_say[i]
            txtcpass = password_d * text_d
            
            txtcpassl.append(txtcpass)
            
                
            #txtcpass = txtcpass / password_d
            #print(txtcpass)
            
            
            
            



        elif s %  2 == 0:
            password_p = password[t]
            
            password_d = int(k_say[password_p])
            text_d = k_say[i]
            txtcpass = password_d * text_d
            
            txtcpassl.append(txtcpass)
            
        else :
            password_p = password[t]
            
            password_d = int(k_say[password_p])
            text_d = k_say[i]
            txtcpass = password_d * text_d
            
            txtcpassl.append(txtcpass)
        if t == tl-1 :
            t = 1
        else :
            t = t+1 
        s = s+1
        
    for i in txtcpassl:
        c = c +"<" + str(i)+">"
    if d == "list":
        return txtcpassl
    elif d == "string":
        return c



#a = encods("ham","yeterartık")
#print(a)
#b = decoder("hamzaay",str(a))
#print(b)