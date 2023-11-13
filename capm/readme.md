This is a Sample CAPM Project in SAP BTP landscape for Clound Foundry Environment -

- Create CAPm Backend
- Design UI for the CAP application
- Add S4 HANA onpremise ODATA
- Deploy your application in BTP 

## Create CAPM backend:
**Overview** 
Create a backend data model to store the data.

1. Create a blank CAPM Template using `cds init purchase-req-importance`
2. Create a file `schema.cds` in the folder `db` and add the below script
  ```js
  using { sap.common.CodeList } from '@sap/cds/common';
  namespace sap.swift.purchasing;
  entity PRCriticality {
    PurchaseRequisition     : String(10);
    PurchaseRequisitionText: String(40);
    Plant: String(4);
    PurchasingOrganization: String(4);
    PurchasingGroup: String(3);
    Urgency: Association to Urgency;
  }
  entity Urgency : CodeList {
    key code: String enum {
      high = 'H';
      medium = 'M'; 
      low = 'L'; 
    };
  }
  ```

3. Then create a new file `service.cds` in the folder `srv` and add the below code:
  ```js
  using { sap.swift.purchasing as my } from '../db/schema';
    service ProcessorService { 
      entity PRCriticality as projection on my.PRCriticality;
      entity Urgency as projection on my.Urgency;
    }
  ```

4. Now use the script `cds add data` to create dummy csv files. Once executed, the below files will be created automatically:
![image](https://github.com/sabarna17/btp-basics/assets/39834671/d45d41ca-ea52-4d44-8a3b-3236701649f5)
 
5. Next use the code `cds watch` and you will be able to see the
   ```bash
   /> successfully deployed to in-memory database.
   [cds] - using authentication: { kind: 'mocked' } 
   [cds] - serving ProcessorService { path: '/odata/v4/processor' }
   [cds] - server listening on { url: 'http://localhost:4004' }
   [cds] - launched at 11/13/2023, 1:22:52 PM, version: 7.3.1, in: 1.216s
   [cds] - [ terminate with ^C ]
   ```
6. Test the url - `http://localhost:4004`
7. Add the below data in the files
   for file `sap.swift.purchasing-Urgency.csv` -
   ```csv
    code;descr
    H;High
    M;Medium
    L;Low
   ```
   for file `sap.swift.purchasing-PRCriticality.csv` -
   ```csv
   PurchaseRequisition,PurchaseRequisitionText,Plant,PurchasingOrganization,PurchasingGroup,Urgency_code
   10000000,,1007,1000,103,H
   10000001,,1007,,103,M
   10000010,,1000,,127,L
   ```
8. Now Execute the ODATA entities and see the outptut `/odata/v4/processor/PRCriticality`, `/odata/v4/processor/Urgency`

## Design UI for the CAP application
**Overview** 
Create UI patterns and use predefined floorplans

1. Goto `View > Command Palette` and then select `Fiori: Open Application Generator`
2. Choose `List Report Page` and click on **Next**
3. Then select the below options for fields *Data Source* and *Choose your CAPM Project*. Then click on **Next**.
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/02e90b9d-6459-4c3e-b972-29a2a22a838d)
4. Set `PRCriticality` as Main Entity.
5. Then set the below attributes and click on **Finish**
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/db57d5f2-a27b-4bf8-ae8b-39157e62a0b8)

Now you have a cool low-code environment to develop a business-standard Fiori UI application.
