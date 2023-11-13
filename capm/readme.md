![image](https://github.com/sabarna17/btp-basics/assets/39834671/4e1b1e39-c8e4-415f-aad8-89ba452a03c0)This is a Sample CAPM Project

## Create CAPM backend:
1. Create a blank CAPM Template using `cds init purchase-req-importance`
2. Create a file `schema.cds` in the folder `db` and add the below code 
  > using { sap.common.CodeList } from '@sap/cds/common';
  > namespace sap.swift.purchasing;
  > entity PRCriticality {
> PurchaseRequisition     : String(10);
> PurchaseRequisitionText: String(40);
> Plant: String(4);
> PurchasingOrganization: String(4);
> PurchasingGroup: String(3);
> Urgency: Association to Urgency;
> }
> entity Urgency : CodeList {
> key code: String enum {
>     high = 'H';
>     medium = 'M';
>     low = 'L';
> };
> }
