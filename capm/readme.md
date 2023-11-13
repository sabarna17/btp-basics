This is a Sample CAPM Project in SAP BTP landscape for Clound Foundry Environment -


## Create CAPM backend:
1. Create a blank CAPM Template using `cds init purchase-req-importance`
2. Create a file `schema.cds` in the folder `db` and add the below script
  ```
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
   ```using { sap.swift.purchasing as my } from '../db/schema';

service ProcessorService { 
  entity PRCriticality as projection on my.PRCriticality;
  entity Urgency as projection on my.Urgency;
}
   ```
