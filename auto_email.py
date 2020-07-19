def send_email(name,email):
    import smtplib
    from string import Template
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.application import MIMEApplication
    
    

    
    
    
    def template_reader(filename):
        with open(filename,'r',encoding='utf-8') as file:
            draft=file.read()
            return Template(draft)
        
        
    template_content=template_reader("template.txt")
    password="**************"
    from_email="********@gmail.com"
    to_email=email
    subject="Confirmation email"
    gmail=smtplib.SMTP(host="smtp.gmail.com",port=587)#change to suitable host and port
    gmail.starttls()
    gmail.login(from_email,password)
    msg=MIMEMultipart()
   
    message=template_content.substitute(YOURNAME=name)
    msg.attach(MIMEText(message,'plain'))
    
    
    #adding pdf attachment
    with open('Buddy Guideline2.pdf', "rb") as f:
            
        attach_pdf = MIMEApplication(f.read(),_subtype="pdf")
        attach_pdf.add_header('Content-Disposition','attachment',filename='Buddy Guideline2.pdf')
        msg.attach(attach_pdf)
    #adding first logo 
    msgText = MIMEText('<p><img src="cid:image1"></p>', 'html')
    msg.attach(msgText)

    
    fp = open('first_image.png', 'rb')
    msgImage1 = MIMEImage(fp.read())
    fp.close()

    
    msgImage1.add_header('Content-ID', '<image1>')
    msg.attach(msgImage1)
    
    #adding second logo
    
    msgText2 = MIMEText('<p><img src="cid:image2"></p>', 'html')
    msg.attach(msgText2)

    
    fp2 = open('second_image.png', 'rb')
    msgImage2 = MIMEImage(fp2.read())
    fp2.close()

    
    msgImage2.add_header('Content-ID', '<image2>')
    msg.attach(msgImage2)
    #adding third logo
    msgText3 = MIMEText('<p><img src="cid:image3"></p>', 'html')
    msg.attach(msgText3)

    
    fp3 = open('third_image.png', 'rb')
    msgImage3 = MIMEImage(fp3.read())
    fp3.close()

    
    msgImage3.add_header('Content-ID', '<image3>')
    msg.attach(msgImage3)
    #adding fourth logo
    msgText4 = MIMEText('<p><img src="cid:image4"></p>', 'html')
    msg.attach(msgText4)

    
    f4 = open('fourth_image.png', 'rb')
    msgImage4 = MIMEImage(f4.read())
    f4.close()

    
    msgImage4.add_header('Content-ID', '<image4>')
    msg.attach(msgImage4)
    #adding fifth logo
    msgText5 = MIMEText('<p><img src="cid:image5"></p>', 'html')
    msg.attach(msgText5)

    
    fp5 = open('fifth_image.png', 'rb')
    msgImage5 = MIMEImage(fp5.read())
    fp5.close()

    
    msgImage5.add_header('Content-ID', '<image5>')
    msg.attach(msgImage5)
  
   
        
            
    
    #sending email
    msg['Subject']=subject
    msg['To']=to_email        
    msg['From']=from_email
    
    
   
    gmail.send_message(msg)
    gmail.quit()


if __name__ =="__main__":
    template_content=send_email("user_name","*******@gmail.com")
   
    


