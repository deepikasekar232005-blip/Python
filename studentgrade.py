mark = int(input("Enter the mark:"))
if mark > 91 and mark < 100:
    print("Scored A grade")
elif mark > 81 and mark < 90:
    print("Scored B grade")
elif mark > 71 and mark < 80:
    print("Scored C grade")
elif mark > 61 and mark < 70:
    print("Scored D grade")
elif mark > 51 and mark <60:
    print("Scored E grade")
else:
    print("Failed")