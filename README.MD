# **ALGORITMA - CAPSTONE PROJECT - API WITH PYTHON**

## **METHOD**

### **GET / ENDPOINTS**


* **/sales/by/bulan**
```
    - Endpoint ini akan menarik produksi invoice per bulan
    - Contoh response yang akan didapatkan :
    
      {
          "Total":{
              "April":198.14,
              "August":198.1,
              "December":189.1,
              "February":187.2,
              "January":201.12,
              "July":190.1,
              "June":201.1,
              "March":195.1,
              "May":193.1,
              "November":186.24,
              "October":193.1,
              "September":196.2
            }
        }
    
```
* **/sales/by/kuartal**
```
    - Endpoint ini akan mengembalikan penjualan per kuartal
    - Contoh response yang akan dikembalikan :
    ```
    {
        "Total":
        {
            "1":583.42,
            "2":592.34,
            "3":584.4,
            "4":568.44
        }
    }
    ```
