# RAP developments in ABAP on Cloud Trial Environment

This is a basic RAP project guide with RAP Generator. I have created a List Report applicationusing this.

## Setup the environment
1. Create an ABAP instance in SAP BTP and create a service key. Note: while creating the instance, use 'email' parameter with the same.
This is a secret file:
```json
{
  "uaa": {
    "tenantmode": "dedicated",
    "sburl": "https://internal-xsuaa.authentication.ap21.hana.ondemand.com",
    "subaccountid": "d77b0a8f-8dbb-4550-bb17-bda5960f0a8c",
    "credential-type": "binding-secret",
    "clientid": "sb-08332394-fcc0-4460-9963-0aacdfe0f224!b22931|abap-trial-service-broker!b18767",
    "xsappname": "08332394-fcc0-4460-9963-0aacdfe0f324!b22931|abap-trial-service-broker!b18767",
    "clientsecret": "352d707c-ff3b-4784-b881-b3e04b0d85c4$nA-ki9aFb_1v4EUgtUM-ricVKhExK1pS_OTgQdvgc4M=",
    "url": "https://d4600ac1trial.authentication.ap21.hana.ondemand.com",
    "uaadomain": "authentication.ap21.hana.ondemand.com",
    "verificationkey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAw7AXcVPRCdW+A4SwDww+\nLpDsfy1CW7NGfmm+YeiSD2O+2t2iIGRVULIRmC9BC2SheJRW8dgn9ogqIf+e1XbP\nlyCtNOHdfmxcXHAYIOrmZSo/5ARa1sN5mpD2gnn8gVCYxr16nWW0Rvi15NGY+3bQ\nM1jD6umJq60QkF6HbKBCdel6Ctpj8tcFAdNJj8qJQrI13Si+KVwzxqhQvhkQ+6au\nM90jEOACy4awz5lgUxfztMqBPJ3RqYgXHK2vSeGnFSrUkUUfSeclis77iFPlX1JZ\nHpFDV/zYNgkxwrPVvRYayqfBqbIFXNtPK+fY2kasYoeOYrWFriCFcFKh9IQLu2y9\nFQIDAQAB\n-----END PUBLIC KEY-----",
    "apiurl": "https://api.authentication.ap21.hana.ondemand.com",
    "identityzone": "d4600ac1trial",
    "identityzoneid": "d77b0a8f-8dbb-4550-bb17-bda5960f0a8c",
    "tenantid": "d77b0a8f-8dbb-4550-bb17-bda5960f0a8c",
    "zoneid": "d77b0a8f-8dbb-4550-bb17-bda5960f0a8c"
  },
  "url": "https://8581cf25-e4bd-4b31-a78e-2d30182dcc48.abap.ap21.hana.ondemand.com",
  "sap.cloud.service": "com.sap.cloud.abap",
  "systemid": "TRL",
  "endpoints": {
    "abap": "https://8581cf25-e4bd-4b31-a78e-2d30182dcc48.abap.ap21.hana.ondemand.com"
  },
  "catalogs": {
    "abap": {
      "path": "/sap/opu/odata/IWFND/CATALOGSERVICE;v=2",
      "type": "sap_abap_catalog_v1"
    }
  },
  "binding": {
    "env": "cf",
    "version": "1.0.1.1",
    "type": "oauth",
    "id": "352d707c-ff3b-4784-b881-b3e04b0d85c4"
  },
  "preserve_host_header": true
}
```
2. Then use eclipse editor to configure the ABAP environment -
   
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/9c73b333-319f-47e7-9a23-0afbc1476185)

   Then select the below option and click next. Then copy paste the service key created from step 1.
   
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/875628e6-88bd-4836-bedc-3bf095c2a07f)

## RAP development
1. Create a package `ZBTP_ABAP_DEMO_XX` and create a dictionary table using the below code:
   ```abap
   @EndUserText.label : 'SAP BTP Registration'
   @AbapCatalog.enhancement.category : #EXTENSIBLE_ANY
   @AbapCatalog.tableCategory : #TRANSPARENT
   @AbapCatalog.deliveryClass : #A
   @AbapCatalog.dataMaintenance : #ALLOWED
   define table ztest_incubation {
     key client         : abap.clnt not null;
     key user_uuid      : sysuuid_x16 not null;
     email              : abap.char(128) not null;
     fullname           : abap.char(100) not null;
     training           : abap.char(50);
     comments           : abap.char(300);
     created_at         : abp_creation_tstmpl;
     created_by         : abp_creation_user;
     last_changed_at    : abp_lastchange_tstmpl;
     last_changed_by    : abp_lastchange_user;
     local_last_changed : abp_locinst_lastchange_tstmpl;
   }
   ```
2. Then right click on the ABAP Table and select the below option and click next:
   
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/d3cf5a8c-1e22-4e4d-832e-55660132f136)

3. Select the below option:
   
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/5e79529e-f505-498e-9089-74a3091959a4)

4. Follow to the last and click on publish. Once your ODATA artifacts are ready, you will see below screen:
5. 
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/5bddd5d3-7683-4b4d-aa54-11acf49a4a92)

6. Now click on preview to see the application. The RAP application will be launched.
7. 
   ![image](https://github.com/sabarna17/btp-basics/assets/39834671/82c8f548-9aae-4156-b717-29320f0c2e3e)

**Note:**

1. After creating the ABAP trial instance, you might face an authorization issue while setting up the system from ADT(Eclipse).
   Try to create the ABAP instance from a different subaccount situated in a different region.

2. This RAP generator works only for the draft scenario. Hence, the below fields are mandatory to use RAP generators.
   ```
   created_at         : abp_creation_tstmpl;
   created_by         : abp_creation_user;
   last_changed_at    : abp_lastchange_tstmpl;
   last_changed_by    : abp_lastchange_user;
   local_last_changed : abp_locinst_lastchange_tstmpl;
   ```
3. Go through these blogs to get more insights on ABAP on Cloud developments -
   - [AI Powered Invoice Management with SAP RAP and ABAP on Cloud](https://blogs.sap.com/2023/06/16/ai-powered-invoice-management-with-sap-rap-and-abap-on-cloud/)
   - [Calling ABAP on Cloud Trial V4 ODATA from SAP S4 HANA On-premise Using ABAP – SM59](https://blogs.sap.com/2023/06/19/calling-abap-on-cloud-trial-v4-odata-from-sap-s4-hana-on-premise-using-abap-sm59/)
   
