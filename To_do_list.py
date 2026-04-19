print('To_Do_List📋\n')

task = []
while True:
 print('1. Add Task')
 print('2. View Task')
 print('3. Remove Task')
 user = input('What do you want to do(1/2/3)')
 if user == '1':
    new_task = input('Add task in to_do_list:')
    task.append(new_task)
    print('Task added!')
    

 elif user == '2':
    print(task)

 elif user == '3':
    remove = input('what you want to remove form to_do_list:')
    try: 
      task.remove(remove)
      print('tasks removed')
    except:
        print('that task does not exist!')  


 play_again = input('Do you want to run again(yea/no)').lower()
 if play_again == 'no':
  print('thank you!')
  break

















