# Imports
import smtplib
from email.message import EmailMessage
from cred import cred

# Functions
def sendEmail(to, subject):
   # Sending Emails

   # Basic implementation
   msg = EmailMessage()
   msg['Subject'] = subject
   msg['From'] = EMAIL_ID
   msg['To'] = to

   # Working with tables
   sno = index
   prod_list = products_list
   table_html = '''
<tr>
<td class="column1">{index}</td>
<td class="column2">{productName}</td>
<td class="column2">Rs. {productCost}</td>
</tr>
'''

   with open("table.html", "a") as f:
      for i in range(sno):
         table_html2 = table_html
         table_html2 = table_html2.replace("{index}", f"{i+1}")
         table_html2 = table_html2.replace("{productName}", f"{prod_list[i][0]}")
         table_html2 = table_html2.replace("{productCost}", f"{prod_list[i][1]}")
         f.write(f"\n{table_html2}")


   # Reading email.html file

   with open("email.html", "r") as f:
      email_content = f.read()

      with open("table.html") as ftable:
         final_table = ftable.read()
         email_content = email_content.replace("{tablesHere}", final_table)
         email_content = email_content.replace("{name}", username)
   
# Making table.html a basic template
   with open("table_temp.html", "r") as fTableTemp:
      table_template = fTableTemp.read()
      with open("table.html", "w") as f:
         f.write(table_template)

# Making email.html a basic template
   with open("email_temp.html", "r") as fEmailTemp:
      email_template = fEmailTemp.read()
      with open("email.html", "w") as f2:
         f2.write(email_template)
         
   msg.set_content(email_content, subtype="html")

   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login(EMAIL_ID, EMAIL_PASSWORD)
      smtp.send_message(msg)
   


# Global Variables
EMAIL_ID = cred['email']
EMAIL_PASSWORD = cred['password']
sum = 0
products_list = []
index = 0

# Email & Name Inputs & Checks
username = input("Please Enter Your Name : ")
email = input("Please Kindly Enter your correct Email, so we can contact you: ")

if "@" not in email:
   print("Please, Enter Correct Email Address!!")
   exit()
else:
   print("Thanks! For giving your Email!! :)")

# Main Code
while True: # --> Infinite Loop

   # Product Name Input
   buy_product = input("Enter the Product Name or q for quit: ")

   #Basic Checks
   if buy_product == "q":
      print(f"Your Total Cost of all products is ₹{sum}, Detailed List : \n")

      for product in products_list:
         print(f"{product[0]} : ₹{product[1]}")
      print(f"Total : ₹{sum}")

      print("\nThanks for Using MannTej Indian Kirana Store Program!! I hope your shop is growing well, Good Day :)\n")
      
      email_choice = input("Do you really want to send email to this user {y/n}: ")
      if email_choice == "y" or email_choice == "Y":
         sendEmail(email, f"{username}, Here's Your Bill Reciept!!")
      else:
         print("Okk! Email not sent!!")

      exit()

   else:

      # Product cost input
      product_cost = int(input(f"Enter the Cost of {buy_product} : "))

      products_list.append((buy_product, product_cost))
      sum += product_cost
      index += 1
