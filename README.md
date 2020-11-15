# Remote Control of PSA car
### This is a python program to control a psa car with connected_car v4 api. Using android app to retrieve credentials.
I test it with a Peugeot e-208 but it should work with others PSA vehicles.

With this app  you will be able to :
 - get the status of the car (battery level for electric vehicle, position ... )
 - start and stop the charge
 - set a charge threshold to limit the battery level to a certain percentage
 - set a stop hour to charge your vehicle only on off-peak hours
 - control air conditioning
 - control lights and horn if your vehicle is compatible (mine isn't) 

## I. Get all credendtials
1. Backup MyPeugeot app

    1.1 MyPeugeot app doesn't allow backup by default so you need to modify it.
    To do that you can follow this guide: https://forum.xda-developers.com/android/software-hacking/guide-how-to-enable-adb-backup-app-t3495117  
    
    1.2 Uninstall the original app
    
    1.3 Install the modified app
    
    1.4 Enable developer mode on your android phone 
    
    1.5 enable password for backup in developer option of your android phone (for some smartphone it is mandatory to sucessfuly backup app)
    
    1.6 backup MyPeugeot app : 
    
    ``` adb backup -f backup.ab -noapk com.psa.mym.mypeugeot ```
    
2. Retrieve credentials in the backup

    ```
   python3 app_decoder.py  backup.ab <backup_password>
   Calculated MK checksum (use UTF-8: true): XXXXXXXXXXXXX
    0% 1% 2% 3% 4% 5% 6% 7% 8% 9% 10% 11% 12% 13% 14% 15%  25% 26% 100% 
    235687424 bytes written to backup.tar.
    mypeugeot email: <write your mypeugeot email>
    mypeugeot password: <write your mypeugeot password>
    What is the car api realm : clientsB2CPeugeot, clientsB2CDS, clientsB2COpel, clientsB2CVauxhall
    clientsB2CPeugeot
    save config change

    Your vehicles: {'VINNUBMER': {'id': 'vehicule id'}} 
      ``` 
 3. If it works you will have VIN of your vehicles and there ids in the last line. The script generate a test.json file with all credentials needed.
 
 ## II. Use the app
  1. start the app:
   ``python3 server.py -f test.json`` 
  
  2. Test it 
  
    2.1 Get the car state :
    http://localhost:5000/get_vehiculeinfo/YOURVIN
    
    2.2 Stop charge
    http://localhost:5000/charge_now/YOURVIN/0
    
    2.3 Set hour to stop the charge to 6am
    http://localhost:5000/charge_control?vin=yourvin&hour=6&minute=0 
    
    2.4 Change car charge threshold to 80 percent
    http://localhost:5000/charge_control?vin=YOURVIN&percentage=80 
           