#MENU DRIVEN PROGRAM TO MAINTAIN THE ITEM - RECORDS OF A SUPERMARKET
import mysql.connector as sql
import sys
from tabulate import tabulate
cnobj=sql.connect(host='YOUR_HOST',user='YOUR_DAATABASE_USER',passwd='YOUR_DATABASE_PASSWORD',database='supermarket')
if cnobj.is_connected():
    print()
    print('SUCCESSFULLY CONNECTED WITH DATABASE')
    print()
csr=cnobj.cursor()

while True:
    print('=================================')
    print('            MAIN MENU            ')
    print('=================================')
    print('   1) PRODUCTS MANAGEMENT')
    print('   2) STAFF DETAILS MANAGEMENT ')
    print('   3) EXIT ')
    print('=================================')
    
    try:
        ch=int(input('Enter choice(1/2): '))
        print()

        #PRODUCTS MANAGEMENT
        if ch==1:
            while True:
                print('===========================')
                print('  PRODUCT MANAGEMENT MENU  ')
                print('===========================')
                print('   1) ADD ITEM ')
                print('   2) DELETE ITEM ')
                print('   3) SEARCH ITEM ')
                print('   4) DISPLAY ITEM ')
                print('   5) UPDATE ITEM')
                print('   6) GO TO MAIN MENU')
                print('===========================')
                print()
                try:
                    ch=int(input('Enter choice: '))
                    print()

                    # TO ADD A NEW ITEM
                    def add_items():
                        pid=int(input('Enter product id: '))
                        pname=input('Enter product name: ')
                        ptype=input('Enter product type: ')
                        pcost=float(input('Enter product cost: '))
                        pqty=int(input('Enter product quantity: '))
                        qry="INSERT INTO ITEMS VALUES({},'{}','{}',{},{});".format(pid,pname,ptype,pcost,pqty)
                        csr.execute(qry)
                        print('ITEM ADDED')
                        cnobj.commit()
                    
                    # TO DELETE ONE OR MORE ITEM
                    def delete_items():
                        print('===========================')
                        print('     ITEMS DELETE MENU     ')
                        print('===========================')
                        print('  1) DELETE ALL RECORDS ')
                        print('  2) DELETE ONE RECORD ')
                        print('  3) GO BACK ')
                        print('===========================')
                        try:
                            ch=int(input('Enter choice: '))
                            if ch==1:
                                qry="DELETE FROM ITEMS;"
                                csr.execute(qry)
                                print('ALL RECORDS DELETED')
                                cnobj.commit()
                            if ch==2:
                                p_id=int(input('Enter product id: '))
                                qry="DELETE FROM ITEMS WHERE pid={};".format(p_id)
                                csr.execute(qry)
                                print('RECORD DELETED')
                                cnobj.commit()
                            elif ch==3:
                                exit
                        except ValueError:
                            print('ENTER CORRECT CHOICE!!!!!!!! ')
                            print()
                            print()
                            
                    #TO FIND DETAILS OF AN ITEM
                    def search_items():
                        try:
                            p_id=int(input('Enter product id: '))
                            qry="SELECT * FROM ITEMS WHERE pid={};".format(p_id)
                            csr.execute(qry)
                            data=csr.fetchone()
                            record=[data]
                            h=['ID','NAME','TYPE','COST','QUANTITY']
                            print(tabulate(record,headers=h,tablefmt='psql'))
                                
                            print()
                            print('---------------------------')
                            print()
                            cnobj.commit()
                        except :
                            print('Item does not exist')

                    #TO DISPLAY THE ITEM DETAILS BASED ON CHOICE
                    def display_items():
                        print('==============================')
                        print('     ITEMS DISPLAY MENU       ')
                        print('==============================')
                        print('   1) DISPLAY ALL ITEMS')
                        print('   2) SORT BY PRODUCT TYPE ')
                        print('   3) SORT BY PRICE ')
                        print('   4) SORT BY QUANTITY ')
                        print('   5) GO BACK ')
                        print('==============================')
                        try:
                            ch=int(input('Enter choice: '))
                            if ch==1:
                                qry="SELECT * FROM ITEMS;"
                                csr.execute(qry)
                                data=csr.fetchall()
                                h=['ID','NAME','TYPE','COST','QUANTITY']
                                print(tabulate(data,headers=h,tablefmt='psql'))

                            elif ch==2:
                                qry="SELECT * FROM ITEMS ORDER BY PTYPE;"
                                csr.execute(qry)
                                print()
                                print('ORDERED BY PRODUCT TYPE')
                                data=csr.fetchall()
                                h=['ID','NAME','TYPE','COST','QUANTITY']
                                print(tabulate(data,headers=h,tablefmt='psql'))
                            elif ch==3:
                                qry="SELECT * FROM ITEMS ORDER BY PCOST;"
                                csr.execute(qry)
                                print()
                                print('ORDERED BY PRICE')
                                data=csr.fetchall()
                                h=['ID','NAME','TYPE','COST','QUANTITY']
                                print(tabulate(data,headers=h,tablefmt='psql'))
                            elif ch==4:
                                qry="SELECT * FROM ITEMS ORDER BY PQTY;"
                                csr.execute(qry)
                                print()
                                print('ORDERED BY QUANTITY')
                                data=csr.fetchall()
                                h=['ID','NAME','TYPE','COST','QUANTITY']
                                print(tabulate(data,headers=h,tablefmt='psql'))
                                print()
                                print()
                            elif ch==5:
                                exit
                        except ValueError:
                            print('ENTER CORRECT CHOICE!!!!!!!! ')
                            print()
                            print()
                        
                        print()

                    # TO UPDATE THE DETAILS OF AN ITEM
                    def update_items():
                        print('======================')
                        print('  ITEMS UPDATE MENU   ')
                        print('======================')
                        print('   1) UPDATE PRICE ')
                        print('   2) UPDATE QTY')
                        print('   3) GO BACK ')
                        print('======================')
                        try:
                            ch=int(input('Enter choice: '))
                            if ch==1:
                                p_id=int(input('Enter prodcut id: '))
                                nprc=int(input('Enter new price: '))
                                qry="UPDATE ITEMS SET PCOST={} WHERE PID={};".format(nprc,p_id)
                                csr.execute(qry)
                                print('PRICE UPDATED')
                                cnobj.commit()
                            elif ch==2:
                                p_id=int(input('Enter prodcut id: '))
                                nqty=int(input('Enter new quantity: '))
                                qry="UPDATE ITEMS SET PQTY={} WHERE PID={};".format(nqty,p_id)
                                csr.execute(qry)
                                print('QUANTITY UPDATED')
                                cnobj.commit()
                            elif ch==5:
                                 exit 
                                
                        except ValueError:
                            print('ENTER CORRECT CHOICE!!!!!!!! ')
                            print()
                            print()
                except ValueError:
                        print('ENTER CORRECT CHOICE!!!!!!!! ')
                        print()
                        print()
                if ch==1:
                    add_items()
                elif ch==2:
                    delete_items()
                elif ch==3:
                    search_items()
                elif ch==4:
                    display_items()
                elif ch==5:
                    update_items()
                elif ch==6:
                    break
                if ch>6:
                    print('CHOICE DOES NOT EXIST')
####################################################################################################################
        elif ch>3:
            print('ENTER CORRECT CHOICE')
            
        #STAFF DETAILS MANAGEMENT
        if ch==2:
            while True:
                print('===========================')
                print('   STAFF MANAGEMENT MENU   ')
                print('===========================')
                print('   1) ADD RECORD ')
                print('   2) DELETE RECORD ')
                print('   3) SEARCH RECORD ')
                print('   4) DISPLAY RECORDS')
                print('   5) UPDATE RECORD ')
                print('   6) GO TO MAIN MENU ')
                print('===========================')
                print()
                try:
                    ch=int(input('Enter choice: '))
                    print()

                    # TO ADD A NEW RECORD
                    def add_records():
                        sid=int(input('Enter staff id: '))
                        sname=input('Enter staff name: ')
                        sdept=input('Enter department: ')
                        semail=input('Enter staff email: ')
                        snum=int(input('Enter staff number: '))
                        salary=float(input('Enter staff salary: '))
                        doj=input("Enter staff's date of join: ")
                        qry="INSERT INTO STAFF VALUES({},'{}','{}',{},{},'{}',{});".format(sid,sname,sdept,snum,salary,semail,doj)
                        csr.execute(qry)
                        cnobj.commit()
                    
                    # TO DELETE ONE OR MORE DETAILS STAFFS
                    def delete_records():
                        print('============================')
                        print('     STAFF DELETE MENU      ')
                        print('============================')
                        print('   1) DELETE ALL RECORDS ')
                        print('   2) DELETE ONE RECORD ')
                        print('   3) GO BACK ')
                        print('============================')
                        print()
                        try:
                            ch=int(input('Enter choice: '))
                            if ch==1:
                                qry="DELETE FROM STAFF;"
                                csr.execute(qry)
                                cnobj.commit()
                                print("ALL RECORDS DELETED")
                            if ch==2:
                                s_id=int(input('Enter staff id: '))
                                qry="DELETE FROM STAFF WHERE id={};".format(s_id)
                                csr.execute(qry)
                                cnobj.commit()
                                print("RECORD DELETED")
                            elif ch==3:
                                exit
                        except ValueError:
                            print('ENTER CORRECT CHOICE!!!!!!!! ')
                            print()
                            print()
                            
                    #TO FIND DETAILS OF A STAFF
                    def search_records():
                        try:
                            s_id=int(input('Enter staff id: '))
                            qry="SELECT * FROM STAFF WHERE ID={};".format(s_id)
                            csr.execute(qry)
                            data=csr.fetchone()
                            record=[data]
                            h=['ID',' NAME ','DEPARTMENT','NUMBER','SALARY','EMAIL','DATE OF JOIN']
                            print(tabulate(record,headers=h,tablefmt='psql'))
                            print()
                            print('---------------------------')
                            print()
                            cnobj.commit()
                        except :
                            print('Rec does not exist')

                    #TO DISPLAY THE STAFF DETAILS BASED ON USERS CHOICE
                    def display_records():
                        print('==============================')
                        print('     STAFF DISPLAY MENU       ')
                        print('==============================')
                        print('   1) DISPLAY ALL RECORDS ')
                        print('   2) SORT BY NAME ')
                        print('   3) SORT BY DEPARTMENT ')
                        print('   4) SORT BY SALARY ')
                        print('   5) GO BACK ')
                        print('==============================')
                        try:
                            ch=int(input('Enter choice: '))
                            if ch==1:
                                    qry="SELECT * FROM STAFF;"
                                    csr.execute(qry)
                                    data=csr.fetchall()
                                    h=['ID',' NAME ','DEPARTMENT','NUMBER','SALARY','EMAIL','DATE OF JOIN']
                                    print(tabulate(data,headers=h,tablefmt='psql'))
                                    print()
                                

                            elif ch==2:
                                qry="SELECT * FROM STAFF ORDER BY SNAME;"
                                csr.execute(qry)
                                data=csr.fetchall()
                                print('ORDERED BY NAME (A-Z)')
                                h=['ID',' NAME ','DEPARTMENT','NUMBER','SALARY','EMAIL','DATE OF JOIN']
                                print(tabulate(data,headers=h,tablefmt='psql'))
                                print()
                            elif ch==3:
                                qry="SELECT * FROM STAFF ORDER BY DEPT;"
                                csr.execute(qry)
                                data=csr.fetchall()
                                print('ORDERED BY DEPARTMENT')
                                h=['ID',' NAME ','DEPARTMENT','NUMBER','SALARY','EMAIL','DATE OF JOIN ']
                                print(tabulate(data,headers=h,tablefmt='psql'))
                                print()
                            elif ch==4:
                                qry="SELECT * FROM STAFF ORDER BY SALARY;"
                                csr.execute(qry)
                                data=csr.fetchall()
                                print('ORDERED BY SALARY)')
                                h=['ID',' NAME ','DEPARTMENT','NUMBER','SALARY','EMAIL','DATE OF JOIN ']
                                print(tabulate(data,headers=h,tablefmt='psql'))
                                print()
                                print()
                            elif ch==5:
                                exit
                            elif ch>5:
                                print('ENTER CORRECT CHOICE!!')
                        except ValueError:
                            print('ENTER CORRECT CHOICE!!!!!!!! ')
                            print()
                            print()
                
                    

                    # TO UPDATE THE DETAILS OF STAFF
                    def update_records():
                        print('==============================')
                        print('      STAFF UPDATE MENU       ')
                        print('==============================')
                        print('   1) UPDATE SALARY ')
                        print('   2) UPDATE PHONE NUMBER ')
                        print('   3) UPDATE DEPARTMENT')
                        print('==============================')
                        try:
                            ch=int(input('Enter choice: '))
                            if ch==1:
                                s_id=int(input('Enter staff id: '))
                                nsal=int(input('Enter new salary: '))
                                qry="UPDATE STAFF SET SALARY={} WHERE ID={};".format(nsal,s_id)
                                csr.execute(qry)
                                print('SALARY UPDATED')
                                cnobj.commit()
                            elif ch==2:
                                s_id=int(input('Enter staff id: '))
                                new_num=int(input('Enter new number: '))
                                qry="UPDATE STAFF SET PHONE={} WHERE ID={};".format(new_num,s_id)
                                csr.execute(qry)
                                print('PHONE NUMBER UPDATED')
                                cnobj.commit()
                            elif ch==3:
                                s_id=int(input('Enter staff id: '))
                                ndept=input('Enter new department: ')
                                qry="UPDATE STAFF SET DEPT={} WHERE ID={};".format(ndept,s_id)
                                csr.execute(qry)
                                print('DEPARTMENT UPDATED')
                                cnobj.commit()
                            elif ch==4:
                                 exit 
                                
                        except ValueError:
                            print('ENTER CORRECT CHOICE!!!!!!!! ')
                            print()
                            print()
                except ValueError:
                        print('ENTER CORRECT CHOICE!!!!!!!! ')
                        print()
                        print()
                if ch==1:
                    add_records()
                elif ch==2:
                    delete_records()
                elif ch==3:
                    search_records()
                elif ch==4:
                    display_records()
                elif ch==5:
                    update_records()
                elif ch==6:
                    break
                if ch>6:
                    print('CHOICE DOES NOT EXIST')

        if ch==3:
            sys.exit()

    except ValueError:
        print('ENTER CORRECT CHOICE!!!!!!!! ')
        print()
        print()

