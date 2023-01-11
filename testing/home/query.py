from sqlalchemy.engine import create_engine
from sqlalchemy.sql.expression import select
from django.db import connections
import pandas 

#from testing.home.views import query



def get_result(search_value,option_value,condition,output_filter,r_value,r_value1):
    # DIALECT = 'oracle'
    # SQL_DRIVER = 'cx_oracle'
    # USERNAME = 'system' #enter your username
    # PASSWORD = 'orcl' #enter your password
    # HOST = 'localhost' #enter the oracle db host url
    # PORT = 1521 # enter the oracle port number
    # SERVICE = 'ORCL1' # enter the oracle db service name
    # ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

    # engine = create_engine(ENGINE_PATH_WIN_AUTH)
    # print(search_value)
    # list=search_value.split(',')
    # print(list)
    with connections['Datacurate'].cursor() as c:
        # df =(c.execute(pandas.DataFrame('CRS',columns=['{option_value}'])))
        # print(df)
        #output_filter = ['abcd', 'efgh', 'ijkl']
        columns = ""
        for i in range(len(output_filter)) :
            if(i == len(output_filter) - 1) :
                columns = columns + output_filter[i]
            else :
                columns = columns + output_filter[i] + ", "

        #print(columns)
        c.execute(f"Select DATA_TYPE from user_tab_columns where table_name='CRS' and column_name='{option_value}'")
        
       
        if condition == 'EQUALS_TO':
            a=next(iter(c.fetchall()[0]))
            if 'VARCHAR2' in a:
                list=search_value.split(',')
                search_value=""
                for i in range(len(list)):
                    if i==(len(list))-1:

                        search_value=search_value+"'"+list[i]+"'"
                    else:
                        search_value=search_value+"'"+list[i]+"',"
                        

            query=(f"select {option_value},{columns} from CRS where ({option_value} IN ({search_value}))")

        elif condition== 'RANGE':

            query=(f"select {option_value},{columns} from CRS where ({option_value} BETWEEN {r_value} and {r_value1})")

        else:
            query=(f"select {option_value},{columns}  from CRS where ({option_value} LIKE ('{search_value}%'))")


       


        
        #print(search_value,'1234')
        c.execute(query)
        return (c.fetchall())

    #x=engine.execute(f"select PRODUCT_CD,RECPT_BRANCH_CD,DEPARTMENT_CODE,BRANCH_OFF_CODE,OFFICE_NAME from CRS_MART where ({option_value} IN ({search_value}))")
    #return (x.fetchall())


#get_result(engine,'TXT_MOBILE',9999999999)