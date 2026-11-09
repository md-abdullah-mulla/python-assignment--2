name = input("Enter Your Student Name : ")

sub1 = float (input("Enter Your Subject 1 mark :"))
sub2 = float(input("Enter Your Subject 2 mark :"))
sub3 = float(input("Enter Your Subject 3 mark :"))

total = sub1+sub2+sub3
avg = total/3

if avg >= 80:
    grade = "A+"
elif avg >= 70:
    grade = "A"
elif avg >= 60:
    grade = "B"
elif avg >= 50:
    grade = "C"
else:
    grade = "F"
print(f"Student Name: {name}")
print(f"Total Marks: {total:.0f}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")

