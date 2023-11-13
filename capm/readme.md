This is a Sample CAPM Project in SAP BTP landscape for Clound Foundry Environment -


## Create CAPM backend:
1. Create a blank CAPM Template using `cds init purchase-req-importance`
2. Create a file `schema.cds` in the folder `db` and add the below script
  ```js[5]
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
  ```js[5]
  using { sap.swift.purchasing as my } from '../db/schema';
    service ProcessorService { 
      entity PRCriticality as projection on my.PRCriticality;
      entity Urgency as projection on my.Urgency;
    }
  ```

4. Now use the script `cds add data` to create dummy csv files. Once executed, the below files will be created automatically:
![image](https://github.com/sabarna17/btp-basics/assets/39834671/d45d41ca-ea52-4d44-8a3b-3236701649f5)
 
