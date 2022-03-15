
class patient:
    Name = "n/a"
    DateOfBirth = "0/0/0000"
    PaymentInfo = []


class PaymentInformation:
    CardNumber = 0
    NameOnCard = "John Smith"
    ExpDate = "0/0000"

class Address:
    AddressLine1 = "1234 1st Street"
    AddressLine2 = "Apt 1"
    City = "Los Angeles"
    State = "CA"
    ZIP = 0

class Payment:
    PaymentType = "Online"
    Amount = 0.0
    PaidStatus = False
    PaymentDueBy = "0/0/0000"
    ProcedureDone = "n/a"
    Date = "0/0/0000"