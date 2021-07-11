
#price of renting a movie per day = $3 per day
price_per_day = 3
little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
days = little_mermaid_days + brother_bear_days + hercules_days
total = days * price_per_day
print(f"Totale rental price is ${total}")

#Pay for different companies
google_rate = 400
amazon_rate = 380
facebook_rate = 350

google_hours = 6
amazon_hours = 4
facebook_hours = 10

google_pay = google_rate * google_hours
amazon_pay = amazon_rate * amazon_hours
facebook_pay = facebook_rate * facebook_hours

total = amazon_pay + google_pay + facebook_pay
print(f"Total paycheck is ${total}")

#Student enrollment eligibility
class_not_full = True
no_class_conflicts = True
enrollment_eligibility = class_not_full and no_class_conflicts
print(f"The class has room is", class_not_full)
print(f"The class fits the student's scheule", no_class_conflicts)
print(f"Can the student enroll?", enrollment_eligibility)


#product offer eligibility
is_premium_member = True
more_than_2_items = False
offer_still_good = True
offer_can_be_applied = offer_still_good and (more_than_2_items or is_premium_member)

#username/password exercises
username = 'codeup'
password = 'notastrongpassword'

password_long_enough = len(password) >= 5
username_short_enough = len(username) <= 20
username_and_password_different = username != password
username_has_spaces = username != username.strip()
password_has_spaces = password != password.strip()

username_is_good = username_short_enough and username_and_password_different and not username_has_spaces
password_is_good = password_long_enough and username_and_password_different and not password_has_spaces

credentials_are_good = username_is_good and password_is_good

print(username, password)
print("Password is long enough?", password_long_enough)
print("Username is short enough?", username_short_enough)
print("Username and password are different", username_and_password_different)
print("Username has spaces", username_has_spaces)
print("Password has spaces", password_has_spaces)
print("Username is good?", username_is_good)
print("Password is good?", password_is_good)
print("Credentials are good?", credentials_are_good)