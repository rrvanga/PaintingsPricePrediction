import csv, os, errno

try:
    os.remove('temp1.csv')
except OSError:
    pass

try:
    os.remove('temp2.csv')
except OSError:
    pass

try:
    os.remove('temp3.csv')
except OSError:
    pass

try:
    os.remove('Final_Input.csv')
except OSError:
    pass


with open('Input.csv', 'r') as csvinput:
    with open('temp1.csv', 'w+') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('size')
        all.append(row)


        for item in reader:
            h = float (item[5])
            w = float (item[6])
            size = h * w
            item.append(size)
            all.append(item)



        writer.writerows(all)

with open('temp1.csv', "r") as csvinput:
    with open('temp2.csv', "w+") as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('orientation')
        all.append(row)


        for item in reader:
            h = float (item[5])
            w = float (item[6])
            if h > w :
                orientation = "portrait"
            elif h < w :
                orientation = "landscape"
            else :
                orientation = "square"

            item.append(orientation)
            all.append(item)


        writer.writerows(all)

with open('temp2.csv', "r") as csvinput:
    with open('temp3.csv', "w+") as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('size category')
        all.append(row)


        for item in reader:
            h = float (item[5])
            w = float (item[6])
            l = h
            if h > w :
                l = h
            elif h < w :
                l = w
            else :
                l = h

            if l <= 20 :
                size = "S"
            elif l > 20 and l <= 38 :
                size = "M"
            elif l > 38 and l <= 60 :
                size = "L"
            elif l > 60 :
                size = "XL"

            item.append(size)
            all.append(item)


        writer.writerows(all)

with open('temp3.csv', "r") as csvinput:
    with open('Final_Input.csv', "w+") as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('price bracket')
        all.append(row)


        for item in reader:
            price = float (item[7])
            pricebracket = 1
            if price <= 150 :
                pricebracket = 1
            elif price > 150 and price <= 200 :
                pricebracket = 2
            elif price > 200  :
                pricebracket = 3
#            elif price > 200 and price <= 500 :
#                pricebracket = 4
#            elif price > 500 :
#                pricebracket = 5

            item.append(pricebracket)
            all.append(item)


        writer.writerows(all)

try:
    os.remove('temp1.csv')
except OSError:
    pass

try:
    os.remove('temp2.csv')
except OSError:
    pass

try:
    os.remove('temp3.csv')
except OSError:
    pass
