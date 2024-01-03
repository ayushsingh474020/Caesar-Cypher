from art import logo



choice=True
print(logo)
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while(choice):
  user_input=input("What do you want to do: encode/decode ")
  shift=int(input("Enter the amount of shift"))
  shift=shift%26
  if(user_input=="encode"):
    user_msg=input("Enter your message to be encoded")
    user_msg=user_msg.lower()
    encoded_msg=""
    for letter in user_msg:
      if(letter in letters):
        encoded_msg+=letters[(letters.index(letter)+shift)%26]
      else:
        encoded_msg+=letter
    print(f"encoded message is {encoded_msg}")

  else:
    user_msg=input("Enter your message to be encoded")
    user_msg=user_msg.lower()
    decoded_msg=""
    for letter in user_msg:
      if(letter in letters):
        decoded_msg+=letters[(letters.index(letter)-shift+26)%26]
      else:
        decoded_msg+=letter
    print(f"decoded message is {decoded_msg}")
  choice=bool(input("Do you want to continue True/False"))  