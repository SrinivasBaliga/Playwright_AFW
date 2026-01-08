import openpyxl

class Utility:

    @staticmethod
    def read_xl(xl_path,sheet_name,row,col):
        value=""
        try:
            wb = openpyxl.load_workbook(xl_path)
            value = wb[sheet_name].cell(row,col).value
            wb.close()
            # print('able to read data from xl')
        except:
            print('error while reading data from xl')

        return value