This is a Sample CAPM Project in SAP BTP landscape for Clound Foundry Environment -

- [Create CAPm Backend](https://github.com/sabarna17/btp-basics/blob/main/capm/readme.md#create-capm-backend)
- [Design UI for the CAP application](https://github.com/sabarna17/btp-basics/blob/main/capm/readme.md#design-ui-for-the-cap-application)
- [Add Custom Logics in CAPM Events](https://github.com/sabarna17/btp-basics/blob/main/capm/readme.md#add-custom-logics-in-capm-events)
- [Deploy your application in BTP](https://github.com/sabarna17/btp-basics/blob/main/capm/readme.md#deploy-your-application-in-btp)

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
**Note:** Install below libraries to avoid any dependency errors while deployment / run `npm i sqlite3 passport @sap/xssec`

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

9. Now enable draft functionality. The easy way to implement this is add the code `annotate PRCriticality with @odata.draft.enabled;` in the file `service.cds`.
   Then goto `schema.cds` and replace with the below code -
   ```
   using { cuid, managed, sap.common.CodeList } from '@sap/cds/common';
   namespace sap.swift.purchasing;
   entity PRCriticality: cuid, managed{
     PurchaseRequisition     : String(10) ;
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
You can try to click on Preview and see the sample application.
![image](https://github.com/sabarna17/btp-basics/assets/39834671/d14a0bed-3a45-4a00-af09-841ed4e5e40a)

You need to choose the option with `cds watch`

6. Then click on `Open Page Map`, here we can create the UI5 page designs -
![image](https://github.com/sabarna17/btp-basics/assets/39834671/cf6fd31d-1e11-48ed-b3ab-a3369061b8ea)

7. Then edit the first page -
![image](https://github.com/sabarna17/btp-basics/assets/39834671/5049160c-73cb-4756-bfcb-1a577156b235)

- Navigate to **PRCriticalityList>Table>Columns** Then Click on ` + ` button and select **Add Basic Column**
- Then select `Urgency/descr` and click **Add**
- Then change the Label to `PR Criticality` and click on the 🌐 icon
Now goto the app `/prcriticality/webapp/index.html?sap-ui-xx-viewCache=false` and here you can see the change in the Column header -
![image](https://github.com/sabarna17/btp-basics/assets/39834671/ef020d29-4aea-44fc-8d22-025ec4152b0f)

8. Now navigate to the Object Page and add Sections
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/f93b852e-7e38-4404-b23a-1669052f7e9e)

9. You can change the fields settings to mark editable and the set the criticality to the List output.
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/0dc7b65b-5654-491f-8da6-9a88575ebf60)
Now right click on the main application and click on preview to launch the application.
![image](https://github.com/sabarna17/btp-basics/assets/39834671/d72dff69-0c5b-45ec-b762-d69606bfbc35)

The Application screens are - 

**List Page**
![image](https://github.com/sabarna17/btp-basics/assets/39834671/bee49ae0-9c5c-4f37-af3f-ecb2386636de)

**Object Page**
![image](https://github.com/sabarna17/btp-basics/assets/39834671/f2d97c83-04f2-49ee-899b-7a5a5be93de5)


## Add Custom Logics in CAPM Events
1. Create a new file `service.js` under the folder `srv`
   
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/77bb9f23-1df4-433b-adcf-daa05c128ad8)

3. Add below logic -
   ```js
   const cds = require('@sap/cds')
   class ProcessorService extends cds.ApplicationService {
     init() {
        this.before(["CREATE","UPDATE"], "PRCriticality", (req) => this.onUpdate(req.data));
        return super.init();
    }
    
    async onUpdate (data) {
        const PurchaseRequisitions = Array.isArray(data) ? data : [data];
        PurchaseRequisitions.forEach((PurchaseRequisition) => {
            if(PurchaseRequisition){
                PurchaseRequisition.PurchaseRequisitionText = 'Hello'
            }
        });
      }    
    }
   module.exports = ProcessorService;
   ```
This above logic will default the Purchase Requisition description while changing / adding the entry.
Try to edit a single entry and save it directly, you can see the Purchase Requisition Text will be defaulted as below - 
![image](https://github.com/sabarna17/btp-basics/assets/39834671/e32d5822-279b-4f89-a21a-9dce5eae9ece)

## Deploy your application in BTP
   **Note**
   *This is not a production scenario. Hence used SQLite for demo purpose. 
   For Production enviroment, use PostgreSQL or SAP HANA DB and create connections with package.json file.
   Go through this [url](https://cap.cloud.sap/docs/get-started/in-a-nutshell#deploying-persistent-databases) for further details.*
   
1. Add a SQLite DB for your in-memory data persistence.
   `npm add @cap-js/sqlite -D`
2. Then execute the below command to deploy the data in local sqlitedb -
   `cds deploy --to sqlite:db/my.swift.db`

Now you will be able to see a new file created, marked with an arrow. Also use the command `sqlite3 my.sqlite .dump` to see the sql operation dumps.
![image](https://github.com/sabarna17/btp-basics/assets/39834671/9d318b93-3096-44d6-9e38-48b310d40375)

3. Add the below code in `package.json`:
   ```
   "cds": {
    "requires": {
      "db": {
        "kind": "sqlite",
        "credentials": {
          "database": "db/my.swift.db"
        }
      },
      "auth": {
        "kind": "basic",
        "users": {
          "sabarna17": {
            "password": "sapbtpcapm2023"
          }
        }
      }
    }
   ```

4. Install the npm packages to remove the dependencies using command `npm i passport sqlite @sap/xssec`

The next step is deploying your application to the SAP BTP Cloud Foundry Environment.

4. The api endpoint for CF environment can be found in BTP Cockpit -

![image](https://github.com/sabarna17/btp-basics/assets/39834671/7c82c628-eafa-4618-bfea-adf9a7b126fc)

5. Use command `cf login -a https://api.cf.us10-001.hana.ondemand.com/` in BAS terminal.
6. Then enter Email ID and password and press enter. Then the below details will appear.
![image](https://github.com/sabarna17/btp-basics/assets/39834671/2c777ace-d812-450f-bf86-9e4900a90745)
7. Use the command `cds add cf-manifest` to add a manifest file for your CAPM Project.
8. Then change the file path to `./` and remove the properties - `serices` and from the terminal execute `cf push`
