from random import choice

num_people = int(input("Enter the number of friends joining (including you):\n"))
if num_people <= 0:
    print("No one is joining for the party")
else:
    people = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(1, num_people + 1):
        people[input()] = 0

    final_bill = int(input())

    for person in people:
        people[person] = bill_per_person

    print("""
Do you want to use the "Who is lucky?" feature? Write Yes/No:
    """)

    response = input()

    if response == "Yes":
        lucky = choice(list(people.keys()))
        people[lucky] = 0
        print(f"{lucky} is the lucky one!")
        bill_per_person = round(final_bill / num_people - 1, 2)
        print(people)
    elif response == "No":
        print("No one is going to be lucky")
        bill_per_person = round(final_bill / num_people, 2)
        print(people)
