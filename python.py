name="my name is imran";
print(name.upper())
print(name.lower());
sr1="imran khan is a student !!!"
print(sr1.rstrip("!"));
print(sr1.split()) #string to list
print(sr1.capitalize()); #frist word upper case
print(sr1.center(60));
print(sr1.count("i"));
print(sr1.endswith("!"));
print(sr1.find("is"));
sr2="IamProgramer689690"
print(sr2.isalnum())
sr3="IamImran"#do not use number
print(sr3.isalpha())
sr4="i am a student"
print(sr4.islower())
print(sr4.title())
print(sr4.replace("student","programmer"))