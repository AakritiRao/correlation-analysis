import mysql.connector as sql
import xlsxwriter
import sys

def main():
    #enter all database login info here
    db = sql.connect(host="impulse.cmmombcefgn8.us-east-2.rds.amazonaws.com",user="andrew.d", password="UiT[dmaoxMmL9oKDJ@LU@bEpigU>efQ6", database="Impulse-copy-stale")
    c = db.cursor()
    cmd = "SELECT COUNT(DISTINCT voterId) FROM votes WHERE voterId IN (SELECT DISTINCT voterId FROM votes WHERE questionId = '4e1e4a46-38d8-4155-ae55-23e38e5db3ad' AND vote='1')"
    c.execute(cmd)
    rows = c.fetchall()
    print(rows[0][0])

main()
