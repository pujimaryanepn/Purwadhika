#!/usr/bin/env python
# coding: utf-8

# # Post-Disaster Disability Aid Distribution Management System

# ### What?
# Post-disaster: the period after a disaster occurs, includes  the time between the disaster and the reconstruction of normal life.
# 
# Disability aid: tools, devices, or equipment that help people with disabilities perform daily tasks, improve mobility, and increase independence. 
# 
# Distribution management system: used for monitors and controls distribution of aid for people with disabilities.

# ### Who?
# This mini app is used by admins to record and monitor data on the distribution of aid to people with disabilities affected by disasters.

# ### How?
# This mini app has 2 main menus:
# #### 1. Manage Disability Data: a menu containing CRUD features to record data on people with disabilities who are affected by disasters
# 1.1 : View Registered Disabled Person
# 
# 1.2 : Register New Data for Disabled Person
# 
# 1.3 : Update Disabled Person Data
# 
# 1.4 : Delete Disabled Person Data
# #### 2. Manage Disability Aid Distribution: a menu containing read and update feature to monitor aid distribution to target
# 2.1 : View Aid Distribution Status
# 
# 2.2 : Update Distribution Status

# In[2]:


dis_data = {'KTP Number': [38001, 31006, 38003, 34004, 32005],
            'Name': ['Pearl', 'Squidward', 'Kitty', 'Pooh', 'Olaf'],
            'Age': [9, 51, 25, 18, 46],
            'Disability Condition': ['Cerebral Palsy', 'Stroke', 'Blind', 'Leg Amputated', 'Blind'],
            'Disability Aid': ['Wheel Chair', 'Wheel Chair', 'White Cane', 'Crutches', 'White Cane'],
            'Refugee Post': ['Post 1', 'Post 2', 'Post 1', 'Post 1', 'Post 4'],
            'Distribution Status': ['On Process', 'On Process', 'On Process', 'On Process', 'On Process']  
}

# Main Menu
def display_menu():
    print("\nPost-Disaster Disability Aid Distribution Management System")
    print("Main Menu:")
    print("1. Manage Disability Data")
    print("2. Manage Disability Aid Distribution")
    print("3. Exit")

# Menu 1: Manage Disability Data
def manage_person_registration(dis_data):
    while True:
        print("\n1. View Registered Disabled Persons")
        print("2. Register New Data for Disabled Person")
        print("3. Update Disabled Person Data")
        print("4. Delete Disabled Person Data")
        print("5. Back to Main Menu") 

        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            view_existing_data(dis_data)
        elif choice == '2':
            create_new_data(dis_data)
        elif choice == '3':
            update_data(dis_data)
        elif choice == '4':
            delete_data(dis_data)
        elif choice == '5':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid option!")

# 1.1: View Registered Disabled Person
def view_existing_data(dic):
    if len(dic['KTP Number']) == 0:                   
        print("\nData does not exist!") 
        return
    
    print("\nWould you like to filter the data? (Y/N)")
    filter_choice = input().strip().lower()
    
    if filter_choice == 'y':
        print("\nChoose a filter option:")
        print("1. Filter by Disability Condition")
        print("2. Filter by Disability Aid")
        print("3. Filter by Refugee Post")
        print("4. Filter by Distribution Status")
        
        filter_option = input("\nEnter the number for your filter option: ").strip()
        
        if filter_option == '1':
            condition = input("Enter Disability Condition: ").strip().capitalize()  
            filtered_data = [i for i in range(len(dic['Disability Condition'])) if dic['Disability Condition'][i].lower() == condition.lower()]
        elif filter_option == '2':
            aid = input("Enter Disability Aid: ").strip().capitalize()
            filtered_data = [i for i in range(len(dic['Disability Aid'])) if dic['Disability Aid'][i].lower() == aid.lower()]
        elif filter_option == '3':
            region = input("Enter Refugee Post: ").strip().capitalize()
            filtered_data = [i for i in range(len(dic['Refugee Post'])) if dic['Refugee Post'][i].lower() == region.lower()]
        elif filter_option == '4':
            status = input("Enter Distribution Status: ").strip().capitalize()
            filtered_data = [i for i in range(len(dic['Distribution Status'])) if dic['Distribution Status'][i].lower() == status.lower()]
        else:
            print("Invalid option! Showing all data.")
            filtered_data = range(len(dic['KTP Number']))
    else:
        filtered_data = range(len(dic['KTP Number'])) 
    
    filtered_data = sorted(filtered_data, key=lambda x: dic['KTP Number'][x])
    
    print('\nThe Disability Data: ')
    print(f"\n{'KTP Number':<10} | {'Name':<15} | {'Age':<10} | {'Disability Condition':<20} | {'Disability Aid':<15} | {'Refugee Post':<15} | {'Distribution Status':<15}")
    print("---------------------------------------------------------------------------------------------------------------------")
    
    for i in filtered_data:
        print(f"{dic['KTP Number'][i]:<10} | {dic['Name'][i]:<15} | {dic['Age'][i]:<10} | {dic['Disability Condition'][i]:<20} | {dic['Disability Aid'][i]:<15} | {dic['Refugee Post'][i]:<15} | {dic['Distribution Status'][i]:<15}")
    print()

# 1.2: Register New Data for Disabled Person
def create_new_data(dic):
    while True:
        new_KTP_number = input('Enter 5-digit KTP Number: ')
        if len(new_KTP_number) == 5 and new_KTP_number.isdigit():
            new_KTP_number = int(new_KTP_number)
            if new_KTP_number in dic['KTP Number']:
                print(f'Data with KTP {new_KTP_number} already exists')
            else:
                break
        else:
            print("Invalid KTP Number! It must be exactly 5 digits.")
    new_name = str(input('Enter name: '))
    new_age = int(input('Enter age: '))
    new_cond = str(input('Enter disability condition: '))
    new_aid = str(input('Enter disability aid required: '))
    new_post = f"Post {int(input('Enter the refugee post number: '))}"
    new_status = "On Process"
            
    dic['KTP Number'].append(new_KTP_number)
    dic['Name'].append(new_name)
    dic['Age'].append(new_age)
    dic['Disability Condition'].append(new_cond)
    dic['Disability Aid'].append(new_aid) 
    dic['Refugee Post'].append(new_post)
    dic['Distribution Status'].append(new_status)
    print('Data has been added successfully!')

# 1.3: Update Disabled Person Data
def update_data(dic):
    KTP_number = (input("Enter KTP number to update: "))
    
    if len(KTP_number) == 5 and KTP_number.isdigit():
        KTP_number = int(KTP_number)
        if KTP_number in dic['KTP Number']:
            index = dic['KTP Number'].index(KTP_number)
            print(f"Updating entry for {dic['Name'][index]}")
        
            while True:
                print("\nWhat would you like to update?")
                print("1. Name")
                print("2. Age")
                print("3. Disability Condition")
                print("4. Disability Aid")
                print("5. Refugee Post")
                print("6. Done (Go back to previous menu)")

                choice = input("Select an option (1-6): ")

                if choice == '1':
                    dic['Name'][index] = input(f"Update Name (current: {dic['Name'][index]}): ") or dic['Name'][index]
                    print("Name updated successfully!")
                elif choice == '2':
                    dic['Age'][index] = int(input(f"Update Age (current: {dic['Age'][index]}): ") or dic['Age'][index])
                    print("Age updated successfully!")
                elif choice == '3':
                    dic['Disability Condition'][index] = input(f"Update Disability Condition (current: {dic['Disability Condition'][index]}): ") or dic['Disability Condition'][index]
                    print("Disability Condition updated successfully!")
                elif choice == '4':
                    dic['Disability Aid'][index] = input(f"Update Disability Aid (current: {dic['Disability Aid'][index]}): ") or dic['Disability Aid'][index]
                    print("Disability Aid updated successfully!")
                elif choice == '5':
                    post_number = input(f"Update Post (current: {dic['Refugee Post'][index]}), enter only the post number: ")
                    dic['Refugee Post'][index] = f"Post {post_number}"
                    print("Post updated successfully!")
                elif choice == '6':
                    print("Finished updating entry.")
                    break
                else:
                    print("Invalid choice, please choose a valid option.")

        else:
            print("KTP number not found.")
    else:
        print("Invalid KTP Number! It must be exactly 5 digits.")

# 1.4: Delete Disabled Person Data
def delete_data(dic):
    KTP_number = int(input("Enter KTP number to delete: "))
    if KTP_number in dic['KTP Number']:
        index = dic['KTP Number'].index(KTP_number)
        for key in dic:
            dic[key].pop(index)
        print(f"Data with KTP {KTP_number} has been deleted.")
    else:
        print("KTP number not found.")            
            

# Menu 2: Manage Disability Aid Distribution
def aid_distribution_management(dis_data):
    while True:
        print("\n1. View Aid Distribution Status")
        print("2. Update Distribution Status")
        print("3. Back to Main Menu")

        choice = input("\nSelect an option (1-3): ")

        if choice == '1':
            view_aid_distribution_status(dis_data)  
        elif choice == '2':
            update_distribution_status(dis_data) 
        elif choice == '3':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid option!")

# 2.1. View Aid Distribution Status
def view_aid_distribution_status(dis_data):
    if len(dis_data['KTP Number']) == 0:
        print("\nData does not exist!") 
        return
    
    sorted_indices = sorted(range(len(dis_data['Distribution Status'])), key=lambda x: dis_data['Distribution Status'][x])

    print('\nSorted Disability Aid Distribution Data:')
    print(f"\n{'KTP Number':<10} | {'Name':<15} | {'Age':<10} | {'Disability Condition':<20} | {'Disability Aid':<15} | {'Refugee Post':<15} | {'Distribution Status':<15}")
    print("---------------------------------------------------------------------------------------------------------------------")
    
    for i in sorted_indices:
        print(f"{dis_data['KTP Number'][i]:<10} | {dis_data['Name'][i]:<15} | {dis_data['Age'][i]:<10} | {dis_data['Disability Condition'][i]:<20} | {dis_data['Disability Aid'][i]:<15} | {dis_data['Refugee Post'][i]:<15} | {dis_data['Distribution Status'][i]:<15}")
    print()

# 2.2. Update Distribution Status
def update_distribution_status(dis_data):
    choice = input("Do you want to input manually by KTP Number? (Y/N): ").upper()

    if choice == 'Y':
        KTP_number = int(input("Enter KTP number to update status: "))
        if KTP_number in dis_data['KTP Number']:
            index = dis_data['KTP Number'].index(KTP_number)
            dis_data['Distribution Status'][index] = "Delivered"
            print(f"Updated status for {dis_data['Name'][index]} (KTP: {dis_data['KTP Number'][index]}) to 'Delivered'.")
        else:
            print("KTP number not found.")

    elif choice == 'N':
        option = input("Update based on: 1. Refugee Post, 2. Disability Aid (1/2): ")

        if option == '1':
            post = input("Enter the post (e.g., 'Post 1'): ")
            indices = [i for i, addr in enumerate(dis_data['Refugee Post']) if addr == post]
            if indices:
                for i in indices:
                    dis_data['Distribution Status'][i] = "Delivered"
                    print(f"Updated status for {dis_data['Name'][i]} (KTP: {dis_data['KTP Number'][i]}) to 'Delivered'.")
            else:
                print(f"No entries found for {post}.")

        elif option == '2':
            aid = input("Enter the disability aid (e.g., 'Wheel Chair'): ")
            indices = [i for i, a in enumerate(dis_data['Disability Aid']) if a == aid]
            if indices:
                for i in indices:
                    dis_data['Distribution Status'][i] = "Delivered"
                    print(f"Updated status for {dis_data['Name'][i]} (KTP: {dis_data['KTP Number'][i]}) to 'Delivered'.")
            else:
                print(f"No entries found for aid type '{aid}'.")
        else:
            print("Invalid option.")
    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")

# Main Program
def main():
    while True:
        display_menu()
        choice = input("\nSelect an option (1-3): ")  
        
        if choice == '1':
            manage_person_registration(dis_data)
        elif choice == '2':
            aid_distribution_management(dis_data)
        elif choice == '3':
            print("Good Bye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




