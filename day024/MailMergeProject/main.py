#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#-------IMPORTS-------
import os

#-------GLOBAL VARIABLES-------
PLACEHOLDER = "[name]"
INPUT_DIRECTORY_PATH = "day024/MailMergeProject/Input/Names/invited_names.txt"
OUTPUT_DIRECTORY_PATH = "day024/MailMergeProject/Output/ReadyToSend"

#-------FUNCTIONS-------
def search_and_replace(starting_file_path, search_word, replace_word, target_file_path):
   '''Takes starting file texts, locates placeholder and replaces with desired text, and then rewrites text in a new file location'''
   with open(starting_file_path, 'r') as file:
      file_contents = file.read()
      updated_contents = file_contents.replace(search_word, replace_word)

   with open(target_file_path, 'w') as file:
      file.write(updated_contents)


#Collect guest list names and place in list 'guest_list"
with open(INPUT_DIRECTORY_PATH) as names:
    guest_list = names.read().split()
    print(guest_list)

#Creates a new txt file with updated text
for guest in guest_list:
   file_name = f'{guest}_invitation.txt'
   target_file_path = os.path.join(OUTPUT_DIRECTORY_PATH, file_name)
   search_and_replace(og_file_path="day024/MailMergeProject/Input/Letters/starting_letter.txt", search_word=PLACEHOLDER, replace_word=guest, target_file_path=target_file_path)