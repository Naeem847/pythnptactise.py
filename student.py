while True:
    stud_data = {
        "student1": {"name": "naeem", "mis_id": 25599},
        "student2": {"name": "talha", "mis_id": 24466},
        "student3": {"name": "raffay", "mis_id": 23377},
    }
    name = input("Enter your name or type 'exit' to quit:\n")
    if name.lower() == "exit":
        print("Exiting the attendance system. Goodbye!")
        break
    mis_id_input = input("Enter your MIS ID or type 'exit' to quit:\n")
    if mis_id_input.lower() == "exit":
        print("Exiting the attendance system. Goodbye!")
        break
    mis_id = int(mis_id_input)
    for student in stud_data.values():
        if student["name"] == name and int(student["mis_id"]) == mis_id:
            print("Present")
            break
    else:
        print("absent")
