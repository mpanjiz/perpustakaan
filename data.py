import model
import uuid;
import bcrypt;

def initRole()  :
    role = [{
        "id":"9EE09436-C88E-4B59-B395-48FA232F88AC",
        "name": "customer"
    },
    {
        "id":"2499ACEC-C914-4040-96DD-8FCA17B7EC9F",
        "name": "admin"
    }]
    return role;

def initUser()  :
    users = [{
        "id":"C344C6F0-C8C1-4D79-A95D-534B83E33B12",
        "id_role": "9EE09436-C88E-4B59-B395-48FA232F88AC",
        "username": "budi007",     
        "password": "budi1234",
        "ktp": "3201234567890"
    },
    {
        "id":"C019DB56-62BB-4B52-8293-7E942F3F13EE",
        "id_role": "9EE09436-C88E-4B59-B395-48FA232F88AC",
        "username": "alex008",     
        "password": "alex1234",
        "ktp": "3211234567891"
    },
    {
        "id":"3C63D16D-F601-4BB7-A64A-0A07C840D1A8",
        "id_role": "9EE09436-C88E-4B59-B395-48FA232F88AC",
        "username": "brown001",     
        "password": "brown1234",
        "ktp": "3221234567892"
    },
    {
        "id":"82B106C4-724A-4291-85AE-A9BCE6BAF125",
        "id_role": "2499ACEC-C914-4040-96DD-8FCA17B7EC9F",
        "username": "superadmin",     
        "password": "admin123",
        "ktp": "3231234567893"
    },
    {
        "id":"E4D248F3-72BD-4598-895C-FF9B0BD37BDD",
        "id_role": "9EE09436-C88E-4B59-B395-48FA232F88AC",
        "username": "admin",     
        "password": "admin123",
        "ktp": "3241234567894"
    }]

    for user in users :
        bytes = user["password"].encode("utf-8")
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        user["password"] = hash

    return users;

def initCategory()  :
    category = [{
        "id":"3C809DDC-5F98-45AA-9E0F-877FF379C318",
        "name": "horor"
    },
    {
        "id":"FB5350E1-4D9C-4E2F-907E-6CFFEA9C4AC7",
        "name": "romance"
    },
    {
        "id":"AA5A3C4C-4CFE-4908-8B50-F392D0D7C18C",
        "name": "ensiklopedia"
    },
    {
        "id":"1046387D-5FFF-449E-8505-CA43988E8245",
        "name": "biografi"
    },
    {
        "id":"1212AEBB-E824-497D-9F6B-8C5D1560D78D",
        "name": "kamus"
    },
    {
        "id":"043D9450-EE28-407A-B1C9-C3249549FA66",
        "name": "komik"
    },
    {
        "id":"E217B9D9-7FA2-406B-9EA3-B1B58888DA59",
        "name": "lainnya"
    }]
    return category;

def initCatalogue() :
    catalogue = [
    {
        "id":"8C63D77F-FFF4-4F50-AF22-A091222002D0",
        "id_category": "FB5350E1-4D9C-4E2F-907E-6CFFEA9C4AC7",
        "title": "Pahe Telecinta",     
        "published_date": "2007-04-01",
        "writer": "Endang Rukmana",
        "capacity": 5,
        "max_day_loans": 5
    },
    {
        "id":"586B1558-4E0A-4650-9051-EF144700B2A2",
        "id_category": "3C809DDC-5F98-45AA-9E0F-877FF379C318",
        "title": "Entrok",     
        "published_date": "2010-04-10",
        "writer": "Okky Madasari",
        "capacity": "0",
        "max_day_loans": 3
    },
    {
        "id":"90498CC0-8E6D-4F02-A694-E76C87188395",
        "id_category": "1046387D-5FFF-449E-8505-CA43988E8245",
        "title": "Catatan Seorang Demonstran",     
        "published_date": "1983-05-01",
        "writer": "Soe Hok Gie",
        "capacity": "3",
        "max_day_loans": 4
    }]
    return catalogue;

def initTrx()  :
    trx = [{
        "id":"0586023E-6A1A-4B8F-AA0F-1C3A571196DD",
        "id_user": "C344C6F0-C8C1-4D79-A95D-534B83E33B12",
        "id_catalogue": "586B1558-4E0A-4650-9051-EF144700B2A2",
        "start_loans_date": "2024-02-20",
        "end_loans_date": "2024-02-22",     
        "loans_day": 3,
        "isReturned": False
    }]
    return trx;