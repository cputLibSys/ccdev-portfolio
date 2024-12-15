from Log import Log

class Datum():
        data=None
        type=None
        limit=None
        null=True
        
        def __init__(self, data, type, limit=60, null=True):
            self.type=type
            self.limit=limit
            self.null=null
            if type=='string':
                self.data = str(data)
            elif type=='integer':
                self.data = int(data)
            elif type=='float':
                self.data = float(data)
            elif type=='dict':
                self.data=data
            elif type=='date':
                self.data=str(data)

        def __repr__(self):
            return str({
                'data': self.data,
                'type':self.type,
                'limit': self.limit,
                'null': self.null
            })

class Table():
   
    def __init__(self, new_tb=False, tb_data=None, table=None):
     
        self.ROWS=[]
        self.PATH=table
        if new_tb:
            with open(table, 'w+') as tb:
                cols=[]
                for k,v in tb_data[0].items():
                    cols.append('{}{};["{}", {}, {}]{}'.format('{', k, v['type'], v['limit'], v['null'],'}'))

                cols='#'.join(cols)
                tb.write(cols+'\n')

                for row in  tb_data[1]:
                    tb.write('#'.join(row)+'\n')
                tb.close()
        else:
            with open(table, 'r') as tb:
                
                row_c=0
                for row in tb:
                    lst=[]
                    data=row.replace('\n', '')
                    data=data.split('#')  
                    if row_c==0:
                        #print(data)
                        for col in data:
                            _cl=col[1:-1].split(';')

                            params=eval(_cl[1])
                            cl=Datum(_cl[0], params[0], params[1], params[2])
                     
                            lst.append(cl)
                            
                        self.ROWS.append(lst)

                    else:            
                        #print(table, self.ROWS[0])

                        self.ROWS.append({
                            self.ROWS[0][i].data: data[i] for i in range(0, len(data))
                        })

                        #print(self.ROWS)
                 
                    row_c+=1

                tb.close()  
 
       

            

    def addRow(self, **kwargs):
        cols=[True for kw in kwargs if kw in self.ROWS[0]]
        new_data=None
        if all(cols):
            new_data = {
                kw: kwargs[kw] for kw in kwargs for i in range(len(kwargs))
            }
            self.ROWS.append(new_data)
        else:
            return 'Error: One or more column names do not exist in the table.'

    def updateRow(self, conditions={}, **kwargs):
        '''
        if conditions:
            row_c=1
            for row in self.ROWS[1:]:
                conds=[True for condition in conditions if condition in row else False]
                if all(conds):
                    for kw in kwargs:
                        self.ROWS[row_c][kw]=kwargs[kw]
        '''        

            


    @property
    def rows(self):
        return self.ROWS

    @property
    def row_count(self):
        return len(self.ROWS[1:])

    @property
    def path(self):
        return self.PATH

    def __repr__(self):
        
        return self.__str__()

    def __str__(self):
        #get max length of column names
    
        maxs=[len(i.data) for i in self.ROWS[0]]
        _max=max(maxs)
        table=('{}|{}'.format(' '*int(_max), ' '*int(_max))).join(list(map(lambda a: Log.OKCYAN+str(a.data)+Log.ENDC,self.ROWS[0])))
        for row in self.ROWS[1:]:
            new_r=(' '*(_max+4)).join(list(val for key, val in row.items()))
            table+='\n{}'.format(new_r)

        return table

    def __iter__(self):
        for row in self.ROWS[1:]:
            yield row