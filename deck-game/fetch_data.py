import mysql.connector
import random
from django.shortcuts import redirect, render


def mysql_connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="admin",
        database="idea2",
    )
    return mydb


# def get_count(mydb):
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT  count(*) FROM app_status")
#     return mycursor.fetchone()[0]

#
def get_count_id(mydb, id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT  count(*) FROM app_status where uid = " + str(id))
    return mycursor.fetchone()[0]


# def get_data_id(mydb, id):
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT  uid FROM app_status where uid = " + str(id))
#     return mycursor.fetchone()[0]
#
#
# def get_status(mydb, id):
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT  uid_status FROM app_status where uid = " + str(id))
#     return mycursor.fetchone()[0]
#

def gen_unique_id():
    unique_id = (random.randint(1000, 9999))
    return unique_id


def insert_data_pin(mydb):
    mycursor = mydb.cursor()
    got_unique_id = False
    id = gen_unique_id()
    while not got_unique_id:
        if get_count_id(mydb, id) == 0:
            sql = "INSERT INTO app_status (uid, uid_status) VALUES (%s, %s)"
            value = (str(id), "running")
            mycursor.execute(sql, value)
            mydb.commit()
            return id
        else:
            id = gen_unique_id()


def update_data(uid, variable_status, final_answer):
    mydb = mysql_connect()
    mycursor = mydb.cursor()
    uid = str(uid)
    variable_status = str(variable_status)
    final_answer = str(final_answer)
    sql = "UPDATE app_status SET uid_status='" + variable_status + "', final_answer= " + final_answer + " where uid =" + uid
    print(sql)
    try:
        mycursor.execute(sql)
        mydb.commit()
        return True

    except:
        return False
#

def fetch_unique_id():
    mydb = mysql_connect()
    return insert_data_pin(mydb)

#
# # added for final
# def fetch():
#     last_answer = FINAL_ANSWER
#     print("---------------------------------------------------", last_answer)
#     return last_answer
#
#
# def display(uid_status):
#     mydb = mysql_connect()
#     if uid_status == "running":
#         return uid_status(mydb)


def fetch_from_db(id):
    mydb = mysql_connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT uid_status, CASE  WHEN isnull(final_answer) = 0 THEN final_answer ELSE -1 END as "
                     "finalanswer FROM app_status where uid = " + str(id))
    fetch_one = mycursor.fetchall()[0]
    if fetch_one[0].lower() == "running":
        return "It is running"
    elif fetch_one[0].lower() == "final answer":
        return str(fetch_one[1])
    else:
        return "Go for new PIN, the game has stopped"

# def fetch_from_db(mydb, uid_status):
#     mycursor = mydb.cursor()
#     id = gen_unique_id()
#     if uid_status == "running":
#         return uid_status
#     elif uid_status == "stop":
#         sql = "INSERT INTO app_status (uid, uid_status) VALUES (%s, %s)"
#         value = (str(id), "running")
#         mycursor.execute(sql, value)
#         mydb.commit()
#         return id
#     elif uid_status == "FINAL_ANSWER":
#         return FINAL_ANSWER
update_data(8498,'Final Answer',22)
# print(get_data_id(mysql_connect(),1234))
# print(get_count(mysql_connect()))
# print(insert_data(mysql_connect()))
