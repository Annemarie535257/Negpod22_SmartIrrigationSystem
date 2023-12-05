#The codes for function to validate user input
#In order to inform if irrigation is needed or not
def validate_user_input(input_value):
    if input_value.lstrip('-').isdigit():
        validated_input = int(input_value)
        if validated_input <= 5:
            return True
        else:
            return False
    else:
        return False


user_input = input("Enter The water level in the soil: ")

if validate_user_input(user_input):
    print("Irrigation Needed!")
else:
    print("Enough water in the soil No irrigation needed.")

