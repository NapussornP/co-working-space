
    in_time=input('Enter in time:(xx.xx)')
    out_time=input('Enter out time:(xx.xx)')
    
def calprice(in_time,out_time):
    in_hr = eval(in_time[0:2])
    in_min = eval(in_time[3:5])
    out_hr = eval(out_time[0:2])
    out_min = eval(out_time[3:5])
    total = (out_hr * 60 + out_min)-(in_hr * 60 + in_min)
    if total % 60 == 0:
        hr = total / 60
    else:
        hr = total // 60 + 1
    
    if 7 <= in_hr <= 24 and 7 <= out_hr <= 24 and 0 <= in_min <= 60 and o <= out_min <= 60:
        if hr <= 2:
            print('Total price:{} THB'.format(2 * 60))
            print('Total hour(s):{} Hour(s) '.format(hr))
        elif 2 < hr <= 4:
            print('Total price:{} THB'.format((2 * 60) + ( hr - 2 * 45)))
            print('Total hour(s):{} Hour(s) '.format(hr))
        elif 4 < hr <= 6:
            print('Total price:{} THB'.format((2 * 60) + ( 2 * 45) + (hr - 4 * 40)))
            print('Total hour(s):{} Hour(s) '.format(hr))
        else:
            print('ราคาเหมาสอบถามหน้าเคาท์เตอร์')

   
    



